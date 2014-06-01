//
//  ViewController.h
//  Slider
//
//  Created by 高橋京介 on 2012/11/05.
//  Copyright (c) 2012年 mycompany. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *label;
- (IBAction)showValue:(UISlider *)sender;
@end
