//
//  ViewController.m
//  Dictionary
//
//  Created by Daisuke Igarashi on 2013/01/03.
//  Copyright (c) 2013年 Daisuke Igarashi. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)searchBarSearchButtonClicked:(UISearchBar *)searchBar
{
    NSString *term = searchBar.text;
    UIReferenceLibraryViewController *controller = [[UIReferenceLibraryViewController alloc] initWithTerm:term];
    [self presentViewController:controller
                       animated:YES
                     completion:NULL];
    [searchBar resignFirstResponder];
}
@end
