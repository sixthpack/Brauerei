#!/bin/python3
# -*- coding: utf-8 -*-
import curses, time
from datetime import datetime
from threading import Thread

class Display:
    
    global sensor1, sensor2, sensorWindow, logWindow, timerWindow
    global BLACK_AND_RED, BLACK_AND_WHITE, GREEN_AND_BLACK
    global log
    global timeThread

    def showTime(self):
        while True:
        # for i in range(100):
            # self.timerWindow.clear()
            self.timerWindow.refresh()
            self.timerWindow.addstr(1, 1, datetime.now().time().strftime("%H:%M:%S"), curses.A_BOLD)
            self.timerWindow.refresh()
            time.sleep(0.1)
            # datetime.now().time().strftime("%H:%M:%S")

    def __init__(self):
        sensorWindowHeight, sensorWindowWidth = 14, 15
        sensorWindowY, sensorWindowX = 2, 2
        self.sensorWindow = curses.newwin(sensorWindowHeight, sensorWindowWidth, sensorWindowY, sensorWindowX)
        logWindowY = sensorWindowY
        logWindowX = sensorWindowX + sensorWindowWidth
        logWindowHeight = sensorWindowHeight
        logWindowWidth = 40
        self.logWindow = curses.newwin(logWindowHeight, logWindowWidth, logWindowY, logWindowX)
        timerWindowHeight = 3
        timerWindowWidth = 9
        timerWindowY = logWindowY
        timerWindowX = logWindowX + 30
        self.timerWindow = curses.newwin(timerWindowHeight, timerWindowWidth, timerWindowY, timerWindowX)
        
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.BLACK_AND_RED = curses.color_pair(1)
        self.BLACK_AND_WHITE = curses.color_pair(2)
        self.GREEN_AND_BLACK = curses.color_pair(3)
        self.sensor1 = 0
        self.sensor2 = 0
        self.repaintSensors()
        self.log = []
        self.repaintLog()

        self.timeThread = Thread(target=self.showTime, args=());
        self.timeThread.setDaemon(True)
        self.timeThread.start()
        
    def repaintSensors(self):
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
                    self.sensorWindow.addstr(i+3, x1+j, " ", self.BLACK_AND_WHITE)
                else:
                    self.sensorWindow.addstr(i+3, x1+j, " ", self.BLACK_AND_RED)

        for i in range(10):
            for j in range(6):
                if i*10 < 100-self.sensor2:
                    self.sensorWindow.addstr(i+3, x2+j, " ", self.BLACK_AND_WHITE)
                else:
                    self.sensorWindow.addstr(i+3, x2+j, " ", self.BLACK_AND_RED)
        

        self.sensorWindow.box()
        self.sensorWindow.refresh()

    def setSensorValues(self, s1, s2):
        self.sensor1 = s1
        self.sensor2 = s2
        self.repaintSensors()
    
    def repaintLog(self):
        self.logWindow.clear()
        self.logWindow.refresh()
        y = 1
        self.logWindow.addstr(y, 1, "Log:", curses.A_BOLD)
        i = 1
        for line in self.log:
            self.logWindow.addstr(y+i, 1, line, self.GREEN_AND_BLACK)
            i = i + 1
        self.logWindow.box()
        self.logWindow.refresh()

    def addLog(self, msg):
        time = datetime.now().time().strftime("%H:%M:%S")
        if len(self.log) < 11:
            self.log.append(f"[{time}] {msg}")
        else:
            self.log = self.log[1:] + [self.log[0]]
        self.log[len(self.log) - 1] = f"[{time}] {msg}"
        self.repaintLog()
    
    def clearLog(self):
        self.log = []
        self.repaintLog()
        
