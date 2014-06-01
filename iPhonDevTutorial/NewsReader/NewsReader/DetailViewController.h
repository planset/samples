//
//  DetailViewController.h
//  NewsReader
//
//  Created by Daisuke Igarashi on 2013/01/06.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController

@property (strong, nonatomic) id detailItem;


@property (weak, nonatomic) IBOutlet UITextView *textView;
@end
