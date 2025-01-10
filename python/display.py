#!/bin/python3
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import curses, time

class Display:
    
    global sensor1, sensor2, sensorWindow

    def __init__(self):
        height, width = 14, 15
        start_y, start_x = 2, 2
        self.sensorWindow = curses.newwin(height, width, start_y, start_x)
        
    def repaintSensors(self):
        #.sensorWindow = curses.initscr()
        # curses.curs_set(False)
        curses.start_color()
        curses.init_pair( 1, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair( 2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair( 3, curses.COLOR_WHITE, curses.COLOR_BLACK)
        BLACK_AND_RED = curses.color_pair(1)
        BLACK_AND_WHITE = curses.color_pair(2)
        WHITE_AND_BLACK = curses.color_pair(3)

        x1 = 1
        x2 = 8

        self.sensorWindow.clear()
        self.sensorWindow.refresh()
        
        self.sensorWindow.addstr(1, 2, "Temperatur:", curses.A_BOLD)
        self.sensorWindow.addstr(2, x1, str(self.sensor1)+"°C", curses.A_BOLD)
        self.sensorWindow.addstr(2, x2, str(self.sensor2)+"°C", curses.A_BOLD)
        
        for i in range(10):
            for j in range(6):
                if i*10 < 100-self.sensor1:
                    self.sensorWindow.addstr(i+3, x1+j, " ", BLACK_AND_WHITE)
                else:
                    self.sensorWindow.addstr(i+3, x1+j, " ", BLACK_AND_RED)

        for i in range(10):
            for j in range(6):
                if i*10 < 100-self.sensor2:
                    self.sensorWindow.addstr(i+3, x2+j, " ", BLACK_AND_WHITE)
                else:
                    self.sensorWindow.addstr(i+3, x2+j, " ", BLACK_AND_RED)
        

        self.sensorWindow.box()
        self.sensorWindow.refresh()

    def setSensorValues(self, s1, s2):
        self.sensor1 = s1
        self.sensor2 = s2
        self.repaintSensors();
