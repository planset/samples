//
//  ViewController.m
//  Localization
//
//  Created by 高橋京介 on 2012/11/02.
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

- (IBAction)showHello {
    
    self.label.text = NSLocalizedString(@"hello", nil);
}
@end
