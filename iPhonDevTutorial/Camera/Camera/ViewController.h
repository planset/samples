//
//  ViewController.h
//  Camera
//
//  Created by Daisuke Igarashi on 2013/01/05.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController
    <UIImagePickerControllerDelegate, UINavigationControllerDelegate>

- (IBAction)showImagePicker:(id)sender;
@property (weak, nonatomic) IBOutlet UIImageView *imageView;

@end
