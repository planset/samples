import toga

def button_handler(widget):
    print("hello")

def build(app):
    container = toga.Container()

    button = toga.Button('Hello world', on_press=button_handler)

    container.add(button)

    container.constrain(button.TOP == container.TOP + 50)
    container.constrain(button.LEADING == container.LEADING + 50)
    container.constrain(button.TRAILING + 50 == container.TRAILING)
    container.constrain(button.BOTTOM + 50 < container.BOTTOM)

    return container

if __name__ == '__main__':
    app = toga.App('First App', 'org.dkpyn.sample1', startup=build)
    app.main_loop()



