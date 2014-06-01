//
//  ViewController.h
//  Taiko
//
//  Created by Daisuke Igarashi on 2013/01/05.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <AVFoundation/AVFoundation.h>
#import <AudioToolbox/AudioToolbox.h>


@interface ViewController : UIViewController
@property AVAudioPlayer *taiko;
- (IBAction)playSound;


@end
