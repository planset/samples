//
//  ViewController.m
//  HelloWorld
//
//  Created by 高橋京介 on 2012/11/01.
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
    int num;
    num = 2;
    if (num > 0) {
        NSLog(@"%dは正の数です。", num);
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
