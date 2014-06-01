//
//  ViewController.h
//  Level
//
//  Created by 高橋京介 on 2012/11/03.
//  Copyright (c) 2012年 mycompany. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <CoreMotion/CoreMotion.h>

@interface ViewController : UIViewController
@property CMMotionManager *motionManager;
@property (weak, nonatomic) IBOutlet UIImageView *bubble;
@end
