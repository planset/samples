//
//  ViewController.m
//  Level
//
//  Created by Daisuke Igarashi on 2013/01/06.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    [self startMoving];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)startMoving
{
    self.motionManager = [[CMMotionManager alloc] init];
    self.motionManager.accelerometerUpdateInterval = 1.0 / 60.0;
    
    NSOperationQueue *queue = [NSOperationQueue mainQueue];
    
    [self.motionManager startAccelerometerUpdatesToQueue:queue withHandler:
     ^(CMAccelerometerData *accelerometerData, NSError *error){
         CMAcceleration acceleration = accelerometerData.acceleration;
         float centerX;
         centerX = 160.0 - acceleration.x * 160.0;
         
         if(centerX < 80.0){
             centerX = 80.0;
         } else if(centerX > 240){
             centerX = 240.0;
         }
         self.bubble.center = CGPointMake(centerX, self.bubble.center.y);
     }];

}
@end
