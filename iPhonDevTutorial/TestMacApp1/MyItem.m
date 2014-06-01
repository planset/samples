//
//  MyItem.m
//  TestMacApp1
//
//  Created by Daisuke Igarashi on 2013/01/04.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import "MyItem.h"

@implementation MyItem

- (id)initWithTitle: (NSString *)title
{
    self = [super init];
    if (self) {
        self.title = title;
    }
    return self;
}

@end
