//
//  ConfigViewController.m
//  NewsReader
//
//  Created by Daisuke Igarashi on 2013/01/06.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import "ConfigViewController.h"

@interface ConfigViewController ()

@end

@implementation ConfigViewController

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view.
    
    [self _loadConfig];
    
}
- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (IBAction)saveConfig:(UIBarButtonItem *)sender {
    
    [self _saveConfig];
    [self.textURL resignFirstResponder];
    
}

- (IBAction)didEndOnExit:(UITextField *)sender {
    [self _saveConfig];
}

- (void)_loadConfig
{
    NSUserDefaults* defaults = [NSUserDefaults standardUserDefaults];
    NSURL *url = [defaults URLForKey:@"RSSURL"];
    if(url != Nil){
        self.textURL.text = url.absoluteString;
    }else{
        self.textURL.text = @"http://www.apple.com/jp/main/rss/hotnews/hotnews.rss";
        [self _saveConfig];
    }
}

- (void)_saveConfig
{
    
    // save configs
    NSUserDefaults* defaults = [NSUserDefaults standardUserDefaults];
    NSURL *url = [[NSURL alloc] initWithString:self.textURL.text];
    [defaults setURL: url forKey:@"RSSURL"];
}


@end
