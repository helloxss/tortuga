import time
import ram.ai.new.utilClasses as utilClasses
import searchPatterns as search
import ram.ai.new.utilStates as utilStates
import ram.ai.new.motionStates as motionStates
import ram.ai.new.approach as approach
import ram.ai.new.motionStates as motionStates

import ram.ai.new.gate as gate
import ram.ai.new.Buoy2014 as buoy
import ram.ai.new.Torp2014 as torp
import ram.ai.new.SonarManip2014 as sonarm
import ram.ai.new.uprights as uprights

from state import *
from stateMachine import *

import ext.math as math
import ram.motion as motion
from ram.motion.basic import Frame

#a terrible pun
def reverseFun(fun):
    def rev():
        return not fun()
    return rev

class TestMachine(StateMachine):
    def __init__(self):
        super(TestMachine, self).__init__()

        buoy = utilClasses.BuoyVisionObject(self.getLegacyState())
        pipe = utilClasses.PipeVisionObject(self.getLegacyState())
        
        start = self.addState('start',utilStates.Start())
        end = self.addState('end',utilStates.End())
        start.setTransition('next','test')
        test = self.addState('test', utilStates.NestedState(sonarm.PogoMotion(4,4,.5,6)))
        
        #upRightsTask = self.addState('uprights', 
        #                             uprights.UprightsTask(buoy, pipe, 
        #                                                   8, 4, 2, 2,
        #                                                   1, 1, 1.5,
        #                                                   'end', 'yaw', 
        #                                                   300))
        #yaw = self.addState('yaw', motionStates.Turn(30))
        #start.setTransition('next', 'uprights')

        #yaw.setTransition('next', 'end')
        #print 'testing'
