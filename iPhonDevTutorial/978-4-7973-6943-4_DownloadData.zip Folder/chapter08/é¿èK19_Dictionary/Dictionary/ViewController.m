//
//  ViewController.m
//  Dictionary
//
//  Created by 高橋京介 on 2012/11/03.
//  Copyright (c) 2012年 mycompany. All rights reserved.
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
    UIReferenceLibraryViewController *controller
        = [[UIReferenceLibraryViewController alloc] initWithTerm:term];
    [self presentViewController:controller
                       animated:YES
                     completion:NULL];
    [searchBar resignFirstResponder];
}

@end
