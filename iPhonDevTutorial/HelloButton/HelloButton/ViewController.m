//
//  ViewController.m
//  HelloButton
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


- (IBAction)showHello:(UIButton *)sender {
    
    self.label.text = @"こんにちは";
    
}


@end
