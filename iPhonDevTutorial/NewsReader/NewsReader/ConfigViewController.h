//
//  ConfigViewController.h
//  NewsReader
//
//  Created by Daisuke Igarashi on 2013/01/06.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ConfigViewController : UIViewController
@property (weak, nonatomic) IBOutlet UITextField *textURL;

- (IBAction)saveConfig:(UIBarButtonItem *)sender;

- (IBAction)didEndOnExit:(UITextField *)sender;


@end
