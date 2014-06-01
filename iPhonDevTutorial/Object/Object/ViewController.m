//
//  ViewController.m
//  Object
//
//  Created by Daisuke Igarashi on 2013/01/02.
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
    Animal *dog;
    dog = [Animal alloc];
    dog = [dog init];
    dog.voice = @"ワン！";
    [dog speak];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
