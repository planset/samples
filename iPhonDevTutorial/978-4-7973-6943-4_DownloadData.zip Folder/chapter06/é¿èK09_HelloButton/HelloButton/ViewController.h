//
//  ViewController.h
//  HelloButton
//
//  Created by 高橋京介 on 2012/12/13.
//  Copyright (c) 2012年 mycompany. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *label;
- (IBAction)showHello;
@end
