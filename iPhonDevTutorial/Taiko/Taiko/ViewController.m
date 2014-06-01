//
//  ViewController.m
//  Taiko
//
//  Created by Daisuke Igarashi on 2013/01/05.
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
    NSString *path = [[NSBundle mainBundle] pathForResource:@"taiko" ofType:@"wav"];
    NSURL *url = [NSURL fileURLWithPath:path];
    self.taiko  = [[AVAudioPlayer alloc] initWithContentsOfURL:url error:NULL];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)playSound {
    
    if(self.taiko.playing){
        self.taiko.currentTime = 0.0;
    }else{
        [self.taiko play];
    }
    AudioServicesPlaySystemSound(kSystemSoundID_Vibrate);
    
}

@end
