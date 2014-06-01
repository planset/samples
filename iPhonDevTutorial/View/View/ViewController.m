//
//  ViewController.m
//  View
//
//  Created by Daisuke Igarashi on 2013/01/03.
//  Copyright (c) 2013年 Daisuke Igarashi. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)changeImage:(UIButton *)sender {
    
    NSString *nextImageFileName;
    NSString *nextTitle;
    
    if(sender.titleLabel.text == @"tapped"){
        nextImageFileName = @"SC103_L.jpg";
        nextTitle = @"button";
    }else{
        nextImageFileName = @"SC107_L.jpg";
        nextTitle = @"tapped";
    }
    
    self.imageView.image = [UIImage imageNamed:nextImageFileName];
    [sender setTitle:@"tapped" forState:UIControlStateNormal];
    
    
}
- (IBAction)display:(UITextField *)sender {
    
    //[self.label setText:sender.text];
    self.label.text = sender.text;
}

- (IBAction)flick:(UISwitch *)sender {
    if (sender.on) {
        self.label.text = @"on";
    } else {
        self.label.text = @"off";
    }
}

- (IBAction)showValue:(UISlider *)sender {
    self.label.text = [NSString stringWithFormat:@"%f", sender.value];
}

- (IBAction)showAlertView {
    
    UIAlertView *alertView = [[UIAlertView alloc] initWithTitle:@"title"
                                                        message:@"body"
                                                       delegate:nil
                                              cancelButtonTitle:@"Cancel"
                                              otherButtonTitles:@"OK" , nil];
    [alertView show];
}

- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex
{
    if(buttonIndex == 0){
        // cancel
        NSLog(@"cancle");
    }else if(buttonIndex == 1){
        // ok
        NSLog(@"OK");
    }
}

@end
