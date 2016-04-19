#!/usr/bin/python
import RPi.GPIO as GPIO
import subprocess as sp
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

proc = None
while True:
    high_goal= GPIO.input(23) 
    low_goal= GPIO.input(17)
    input_state = GPIO.input(18)
    auto = GPIO.input(27)
    defenses = GPIO.input(22)
    #if not proc:
        #proc = sp.Popen(['omxplayer', 'Pit.mp4'], stdin=sp.PIPE)
    if input_state == False:
        if proc:
            proc.communicate('q')
        proc = sp.Popen(['omxplayer', 'Intakes.m4v'], stdin=sp.PIPE)
        #os.system("omxplayer Intakes.m4v")
        print('Button Pressed')
        time.sleep(0.2)
    if high_goal == False:
        if proc:
            proc.communicate('q')
        proc = sp.Popen(['omxplayer', 'HighGoal.m4v'], stdin=sp.PIPE)
        #os.system("omxplayer HighGoal.m4v")
        print('Button Pressed')
        time.sleep(0.2)
    if low_goal == False:
        if proc:
            proc.communicate('q')
        proc = sp.Popen(['omxplayer', 'LowGoal.m4v'], stdin=sp.PIPE)
        #os.system("omxplayer LowGoal.mp4")
        print('Button Pressed')
        time.sleep(0.2)
    if auto == False:
        if proc:
            proc.communicate('q')
        proc = sp.Popen(['omxplayer', 'Autonomous.m4v'], stdin=sp.PIPE)
        #os.system("omxplayer Autonomous.m4v")
        print('Button Pressed')
        time.sleep(0.2)
    if defenses == False:
        if proc:
            proc.communicate('q')
        proc = sp.Popen(['omxplayer', 'Defenses.m4v'], stdin=sp.PIPE)
        #os.system("omxplayer Defenses.m4v")
        print('Button Pressed')
        time.sleep(0.2)
    
