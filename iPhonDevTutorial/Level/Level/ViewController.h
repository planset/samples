//
//  ViewController.h
//  Level
//
//  Created by Daisuke Igarashi on 2013/01/06.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <CoreMotion/CoreMotion.h>

@interface ViewController : UIViewController
@property CMMotionManager *motionManager;
@property (weak, nonatomic) IBOutlet UIImageView *bubble;

@end
