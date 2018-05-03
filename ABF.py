#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:44:25 2018

@author: alanmontarras
"""

from neo.io import AxonIO 
import numpy as np

class ABF:
    
    def __init__(self,filename):
        
        self.reader=AxonIO(filename)
        
        self.block=self.reader.read_block()
        
        self.nb_swp=len(self.block.segments)
        
        dt=self.block.rec_datetime
        self.rec_time=(dt.hour*60)+dt.minute # recording time in minutes
        
        self.rate=self.block.segments[0].analogsignals[0].sampling_rate # sampling rate of recordings in Hz.
        
    def sweep (self,swp_nb):
        
        return self.block.segments[swp_nb]

    def ana0(self,swp_nb): 

        return self.block.segments[swp_nb].analogsignals[0]
    
    def ana1(self,swp_nb): 

        return self.block.segments[swp_nb].analogsignals[1]
    
    @staticmethod   # return the time array of an analog signal (in milliseconds).// always start at 0 ms //
    def time(ana):
        
        t=ana.times-ana.t_start # substract the start time to initialize start of array to 0.
        
        return np.array(t*1000)
    
    def p(self,tps): #return the index point of a recording from the time in millisecond

        return np.int((self.rate*tps)/1000)

    def t(self,pt):  #return the time in millisecond  of a recording from the index point

        return np.float((pt/self.rate)*1000)
