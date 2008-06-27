# Copyright (C) 2007 Maryland Robotics Club
# Copyright (C) 2007 Joseph Lisee <jlisee@umd.edu>
# All rights reserved.
#
# Author: Joseph Lisee <jlisee@umd.edu>
# File:  vehicle/sim/vehicle.py

# Python Imports
import warnings

# Project Imports
import event	
from core import Component, implements
from ram.module import IModule, Module, Component, ModuleManager

warnings.simplefilter('ignore', RuntimeWarning)
from ext.vision import VisionRunner as _Vision # Import C++ Vision
warnings.simplefilter('default', RuntimeWarning)

class VisionRunner(_Vision, Component):
    implements(IModule)
    
    def __init__(self, vehicle, config):
        # Create C++ super class
        _Vision.__init__(self)
        
        # Module variabls
        self.name = config['name']
        self.type = type(self)
        self._depends = []
        self._running = False
        self._devices = {}
        
        self._config = config
     
        
        # Create module base class, send off events
        print 'Initing'    
        event.send('MODULE_CREATED', self)
        ModuleManager.get().register(self)
        print 'Done'
        
    def start(self):
 #       self.background(self._config['update_interval'])
        event.send('MODULE_START', self)    
        
    def pause(self):
#        self.unbackground()
        self._running = False
        event.send('MODULE_PAUSE', self)
        
    def backgrounded(self):
	return True

    def update(self, timestep):
        pass

    def shutdown(self):
        self.pause()
        # Put more shutdown stuff here
        
        event.send('MODULE_SHUTDOWN',self)