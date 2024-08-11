#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:47:35 2024

@author: Alex Czerniewski
"""

from ui import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
import serial
import os

class Main(qtw.QMainWindow):    
    def __init__(self):        
        super(Main,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)    
        print ("show GUI")
               
        self.ui.btn_set_attenuation.clicked.connect(self.set_att)
        
    def set_att(self):
        os.system("sudo chmod 666 /dev/ttyS0")  # replace with your port
        ser=serial.Serial(
            port='/dev/ttyS0', # replace with your port
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1    
        ) 
        
        attenuation = self.ui.dsbox_attenuation.text()

        if float(attenuation) < 10:
            attenuation = attenuation.replace(".","")
            cmd="wv00"+attenuation+"\n"
            cmd=cmd.encode()
        else:
            attenuation = str(attenuation).replace(".","")
            cmd="wv0"+str(attenuation)+"\n"
            cmd=cmd.encode()
            
        ser.write(cmd)
        
if __name__=='__main__':
    
    app=qtw.QApplication([])
    
    widget=Main()
    widget.show()
    
    
    app.exec_()
