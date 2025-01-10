#!/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import curses, time

class Display:
    
    global sensor1, sensor2, stdscr

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def repaint(self):
        # stdscr = curses.initscr()
        # curses.curs_set(False)
        curses.start_color()
        curses.init_pair( 1, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair( 2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        x1 = int ( (curses.COLS - 5 )/2)
        x2 = int ( (curses.COLS + 5 )/2)

        self.stdscr.clear()
        self.stdscr.refresh()
        temp1 = self.sensor1.split('.')[0]
        temp2 = self.sensor2.split('.')[0]
        self.stdscr.addstr(4, x1, temp1+"°C", curses.A_BOLD)
        self.stdscr.addstr(4, x2, temp2+"°C", curses.A_BOLD)
        
        v1 = int(temp1)
        v2 = int(temp2)
        
        for i in range(10):
            for j in range(4):
                if i*10 < 100-v1:
                    self.stdscr.addstr(5+i, x1+j, " ", curses.color_pair(2))
                else:
                    self.stdscr.addstr(5+i, x1+j, " ", curses.color_pair(1))

        for i in range(10):
            for j in range(4):
                if i*10 < 100-v2:
                    self.stdscr.addstr(5+i, x2+j, " ", curses.color_pair(2))
                else:
                    self.stdscr.addstr(5+i, x2+j, " ", curses.color_pair(1))

        self.stdscr.refresh()

    def setSensorValues(self, s1, s2):
        self.sensor1 = int(s1)#s1.split('.')[0]
        self.sensor2 = int(s2)#s2.split('.')[0]
        self.repaint();
