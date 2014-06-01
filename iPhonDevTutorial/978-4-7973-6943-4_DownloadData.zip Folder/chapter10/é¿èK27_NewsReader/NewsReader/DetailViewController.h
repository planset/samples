//
//  DetailViewController.h
//  NewsReader
//
//  Created by 高橋京介 on 2012/11/03.
//  Copyright (c) 2012年 mycompany. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController

@property (strong, nonatomic) id detailItem;


@property (weak, nonatomic) IBOutlet UITextView *textView;
@end
