//
//  MasterViewController.m
//  NewsReader
//
//  Created by Daisuke Igarashi on 2013/01/06.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import "MasterViewController.h"

#import "DetailViewController.h"

@interface MasterViewController () {
    NSMutableArray *_items;
    Item *_item;
    NSXMLParser *_parser;
    NSString *_elementName;
}
@end

@implementation MasterViewController
//
//- (void)awakeFromNib
//{
//    [super awakeFromNib];
//}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    UIRefreshControl *refreshControl = [[UIRefreshControl alloc] init];
    [refreshControl addTarget:self
                       action:@selector(startDownload)
              forControlEvents:UIControlEventValueChanged];
    self.refreshControl = refreshControl;
    [self startDownload];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return _items.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:@"Cell" forIndexPath:indexPath];

    if (_items.count == 0){
        return nil;
    }
    Item *item = _items[indexPath.row];
    cell.textLabel.text = [item title];
    return cell;
}

- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([[segue identifier] isEqualToString:@"showDetail"]) {
        NSIndexPath *indexPath = [self.tableView indexPathForSelectedRow];
        Item *item = _items[indexPath.row];
        [[segue destinationViewController] setDetailItem:item];
    }
}

- (NSString *)_loadConfig
{
    NSUserDefaults* defaults = [NSUserDefaults standardUserDefaults];
    NSURL *url = [defaults URLForKey:@"RSSURL"];
    if(url != Nil){
        return url.absoluteString;
    }else{
        return @"http://www.apple.com/jp/main/rss/hotnews/hotnews.rss";
    }
}

- (void)startDownload
{
    NSString *feed = [self _loadConfig];
    NSURL *url = [NSURL URLWithString:feed];
    NSURLRequest *request = [NSURLRequest requestWithURL:url cachePolicy:NSURLRequestUseProtocolCachePolicy timeoutInterval:2];
    NSOperationQueue *queue = [[NSOperationQueue alloc] init];
    [NSURLConnection sendAsynchronousRequest:request
                                       queue:queue
                           completionHandler:
     ^(NSURLResponse *response, NSData * data, NSError *error){
        
         NSHTTPURLResponse * httpResponse = (NSHTTPURLResponse *) response;
         NSInteger statusCode = httpResponse.statusCode;
         
         if(statusCode != 200 || error != nil){
             [self.refreshControl endRefreshing];
             return;
         }
         
         _items = [[NSMutableArray alloc]init];
         _parser = [[NSXMLParser alloc ] initWithData:data];
         _parser.delegate =  self;
         [_parser parse];
         
//         if(error != nil){
//         }else{
////             error = nil;
////             data = [[NSData alloc] init];
////             _parser = [[NSXMLParser alloc ] initWithData:data];
////             _parser.delegate =  self;
////             [_parser parse];
////             UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"Error" message:@"Connection failed" delegate:nil cancelButtonTitle:nil otherButtonTitles:@"OK", nil];
////             [alertView show];
//         }
         
     }];
    
}



- (void)parser:(NSXMLParser *)parser
didStartElement:(NSString *)elementName
namespaceURI:(NSString *)namespaceURI
qualifiedName:(NSString *)qName
attributes:(NSDictionary *)attributeDict
{
    _elementName = elementName;
    if([_elementName isEqualToString:@"item"]){
        _item = [[Item alloc] init];
        _item.title = @"";
        _item.description = @"";
        _item.link = @"";
    }
}

- (void)parser:(NSXMLParser *)parser foundCharacters:(NSString *)string
{
    if([_elementName isEqualToString:@"title"]){
        _item.title = [_item.title stringByAppendingString:string];
    }else if([_elementName isEqualToString:@"description"]){
        _item.description = [_item.description stringByAppendingString:string];
    }else if([_elementName isEqualToString:@"link"]){
        _item.description = [_item.description stringByAppendingString:string];
    }
    
}

- (void)parser:(NSXMLParser *)parser
didEndElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName
{
    if([elementName isEqualToString:@"item"]){
        [_items addObject:_item];
    }
}

- (void)parserDidEndDocument:(NSXMLParser *)parser
{
    dispatch_async(dispatch_get_main_queue(), ^{
        [self.refreshControl endRefreshing];
        [self.tableView reloadData];
    });
}


@end
