#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
import curses
import locale

def helloworld(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 1, "波浪ワールド", curses.A_BOLD)
    stdscr.refresh()

    while True:
        if stdscr.getch() == 0x1b:
            break
        curses.flash()


class Window(object):
    def __init__(self, curses_window, title):
        self.title = title
        self.window = curses_window
        self.panel = curses.panel.new_panel(curses_window)

    def show(self):
        self.window.border()
        self.window.addstr(0, 2, "[ %s ]" % self.title)
        self.refresh()

def panel_sample(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.refresh()

    hello_window = Window(curses.newwin(15, 40, 2, 2), "Hello world")
    hello_window.window.addstr("Hello wolrld " * 20)
    hello_window.show()

    spam_window = Window(curses.newwin(12, 40, 10, 30), "Ham Spam Egg")
    spam_window.window.addstr("Spam! " * 20)
    spam_window.show()

    window_queue = queue.Queue()
    window_queue.put(hello_window)

    current_window = spam_window

    while True:
        c = stdscr.getch()
        if (c == 0x1b) or (c == ord("q")):
            break

        elif c == 0x20:
            window_queue.put(current_window)
            current_window = window_queue.get()
            current_window.panel.top()
            curses.panel.update_panels()
            stdscr.refresh()

        else:
            curses.flash()



if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    curses.wrapper(panel_sample)
    #curses.wrapper(helloworld)
    #curses.wrapper は以下のコードを実行して渡してくれる。
    #それ以外にも例外時の端末モードの復帰なども行ってくれる。
    #stdscr = curses.initscr()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

