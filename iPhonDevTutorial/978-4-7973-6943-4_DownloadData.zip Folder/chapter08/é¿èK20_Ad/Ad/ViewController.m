//
//  ViewController.m
//  Ad
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

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];
    CGRect bannerFrame = self.bannerView.frame;
    bannerFrame.origin.y = self.view.frame.size.height;
    self.bannerView.frame = bannerFrame;
}

- (void)bannerViewDidLoadAd:(ADBannerView *)banner
{
    CGRect bannerFrame = banner.frame;
    bannerFrame.origin.y
        = self.view.frame.size.height - banner.frame.size.height;
    
    [UIView animateWithDuration:1.0
                     animations:^{
                         banner.frame = bannerFrame;
                     }];
    NSLog(@"広告在庫あり");
}

- (void)bannerView:(ADBannerView *)banner
        didFailToReceiveAdWithError:(NSError *)error
{
    CGRect bannerFrame = banner.frame;
    bannerFrame.origin.y = self.view.frame.size.height;
    
    [UIView animateWithDuration:1.0
                     animations:^{
                         banner.frame = bannerFrame;
                     }];
    NSLog(@"広告在庫なし");
}

@end
