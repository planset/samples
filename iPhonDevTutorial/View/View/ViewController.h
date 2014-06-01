//
//  ViewController.h
//  View
//
//  Created by Daisuke Igarashi on 2013/01/03.
//  Copyright (c) 2013年 Daisuke Igarashi. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController
@property (weak, nonatomic) IBOutlet UIImageView *imageView;
- (IBAction)changeImage:(UIButton *)sender;
@property (weak, nonatomic) IBOutlet UILabel *label;
- (IBAction)display:(UITextField *)sender;
- (IBAction)flick:(UISwitch *)sender;
- (IBAction)showValue:(UISlider *)sender;

- (IBAction)showAlertView;

@end
