//
//  ViewController.h
//  Browser
//
//  Created by Daisuke Igarashi on 2013/01/03.
//  Copyright (c) 2013年 Daisuke Igarashi. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController
- (IBAction)showWebSite:(UITextField *)sender;
@property (weak, nonatomic) IBOutlet UIWebView *webView;

@end
