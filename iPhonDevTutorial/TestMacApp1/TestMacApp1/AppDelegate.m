//
//  AppDelegate.m
//  TestMacApp1
//
//  Created by Daisuke Igarashi on 2013/01/04.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import "AppDelegate.h"
#import "MyItem.h"

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    // Insert code here to initialize your application
}

- (IBAction)addItem:(NSButton *)sender {

    [self.items add: [[MyItem alloc] initWithTitle:@"aaa"]];

}
- (IBAction)displayCount:(NSButton *)sender {
    NSLog(@"%@", self.items.selectedObjects[0]);
    
}
@end
