from gntp import notifier
#import logging
#logging.basicConfig(level=logging.CRITICAL)

#notifier.mini("Here's a quick message")

# More complete example
growl = notifier.GrowlNotifier(
    applicationName = "My Application Name",
    notifications = ["New Updates","New Messages"],
    defaultNotifications = ["New Messages"],
    #hostname = "10.1.2.242",
    #password = ""
)
growl.register()

# Send one message
growl.notify(
    noteType = "New Messages",
    title = "You have a new message",
    description = "A longer message description",
    icon = "http://example.com/icon.png",
    sticky = False,
    priority = 1,
)

# Try to send a different type of message
# This one may fail since it is not in our list
# of defaultNotifications
growl.notify(
    noteType = "New Updates",
    title = "There is a new update to download",
    description = "A longer message description",
    icon = "http://example.com/icon.png",
    sticky = False,
    priority = -1,
)
