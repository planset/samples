//
//  ViewController.h
//  Taiko
//
//  Created by 高橋京介 on 2012/11/03.
//  Copyright (c) 2012年 mycompany. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <AVFoundation/AVFoundation.h>
#import <AudioToolbox/AudioToolbox.h>

@interface ViewController : UIViewController
@property AVAudioPlayer *taiko;
- (IBAction)playSound;
@end
