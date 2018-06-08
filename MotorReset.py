#!/usr/bin/python2.7.13
# PDSP Extract Maker GUI
# Reset Motors
# Author: Jamin Liu
# Shut off motors immediately for testing

import piplates.MOTORplate as MOTOR
import RPi.GPIO as GPIO
import time
import os
import string
from Tkinter import *
import tkFont


MOTOR.RESET(0)
GPIO.cleanup()