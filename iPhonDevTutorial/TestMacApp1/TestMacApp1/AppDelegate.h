//
//  AppDelegate.h
//  TestMacApp1
//
//  Created by Daisuke Igarashi on 2013/01/04.
//  Copyright (c) 2013年 dkpyn. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface AppDelegate : NSObject <NSApplicationDelegate>

@property (assign) IBOutlet NSWindow *window;
- (IBAction)addItem:(NSButton *)sender;
@property (weak) IBOutlet NSScrollView *collectionView;

@property (weak) IBOutlet NSArrayController *items;
- (IBAction)displayCount:(NSButton *)sender;

@end
