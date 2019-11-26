#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))  
dogLeft = visual.ImageStim(win, image='dog/1.jpg',pos=(.5,0))
dogRight = visual.ImageStim(win, image='dog/2.jpg',pos=(-.5,0))
myText = visual.TextStim(win, text="Please select which one is cuter. a for left, d for Right", color="red",pos=(0,-.4) , height=(.03))

# then draw all stimuli
dogLeft.draw()
dogRight.draw()
myText.draw()

# then flip your window
win.flip()

event.globalKeys.add(key='q',func=core.quit)

# then record your responses
keys = event.waitKeys()
keyList=('a', 'd')

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
