# Copyright (C) 2008 Maryland Robotics Club
# Copyright (C) 2008 Joseph Lisee <jlisee@umd.edu>
# All rights reserved.
#
# Author: Joseph Lisee <jlisee@umd.edu>
# File:  packages/python/ram/ai/pipe.py


"""
A state machine for following the pipeline
 - Searches for a pipe
 - Centers over the first pipe, and waits to settle
 - Drives forward until it doesn't see the pipe
 - Goes back to the first step
 
Requires the following subsystems:
 - timerManager - ram.timer.TimerManager
 - motionManager - ram.motion.MotionManager
 - controller - ext.control.IController
"""

# Project Imports
import ext.core as core
import ext.vision as vision
import ext.math

import ram.ai.state as state
import ram.motion as motion
import ram.motion.search
import ram.motion.pipe

class Searching(state.State):
    """When the vehicle is looking for a pipe"""
    @staticmethod
    def transitions():
        return { vision.EventType.PIPE_FOUND : Seeking }

    def enter(self):
        # Turn on the vision system
        self.visionSystem.pipeLineDetectorOn()

        # Create zig zag search to 
        zigZag = motion.search.ForwardZigZag(
            legTime = 15,
            sweepAngle = 60,
            speed = 5)

        self.motionManager.setMotion(zigZag)

    def exit(self):
        self.motionManager.stopCurrentMotion()

class Seeking(state.State):
    """When the vehicle is moving over the found pipe"""
    @staticmethod
    def transitions():
        return { vision.EventType.PIPE_LOST : Searching,
                 vision.EventType.PIPE_FOUND : Seeking,
                 vision.EventType.PIPE_CENTERED : Centering }

    def PIPE_FOUND(self, event):
        """Update the state of the light, this moves the vehicle"""
        self._pipe.setState(event.x, event.y, event.angle)

    def enter(self):
        self._pipe = ram.motion.pipe.Pipe(0,0,0)
        motion = ram.motion.pipe.Hover(pipe = self._pipe,
                                       maxSpeed = 5,
                                       maxSidewaysSpeed = 3)
        self.motionManager.setMotion(motion)

    def exit(self):
        #print '"Exiting Seek, going to follow"'
        self.motionManager.stopCurrentMotion()

class Centering(state.State):
    """
    When the vehicle is settling over the pipe
    
    @cvar SETTLED: Event fired when vehile has settled over the pipe
    """
    SETTLED = core.declareEventType('SETTLED')
    
    @staticmethod
    def transitions():
        return { vision.EventType.PIPE_LOST : Searching,
                 vision.EventType.PIPE_FOUND : Centering,
                 Centering.SETTLED : AlongPipe }
    
    def PIPE_FOUND(self, event):
        """Update the state of the light, this moves the vehicle"""
        self._pipe.setState(event.x, event.y, event.angle)

    def enter(self):
        self.timer = self.timerManager.newTimer(Centering.SETTLED, 5)
        self.timer.start()
        
        self._pipe = ram.motion.pipe.Pipe(0,0,0)
        motion = ram.motion.pipe.Hover(pipe = self._pipe,
                                       maxSpeed = 5,
                                       maxSidewaysSpeed = 3)
        self.motionManager.setMotion(motion)

    def exit(self):
        #print '"Exiting Seek, going to follow"'
        self.motionManager.stopCurrentMotion()
        self.timer.stop()

class AlongPipe(state.State):
    """
    When the vehicle is following along a visible pipe
    """
    FOUND_NEW_PIPE = core.declareEventType('FOUND_NEW_PIPE')
    
    @staticmethod
    def transitions():
        return { vision.EventType.PIPE_LOST : BetweenPipes,
                 vision.EventType.PIPE_FOUND : AlongPipe,
                 AlongPipe.FOUND_NEW_PIPE : Seeking }


    def PIPE_FOUND(self, event):
        """Update the state of the light, this moves the vehicle"""
        
        # Determine if a new pipe has appeared in the field of view
        newPipeLoc = ext.math.Vector3(event.x, event.y, 0)
        if self._lastPipeLoc is not None:
            if self._lastPipeLoc.distance(newPipeLoc) > 0.5:
                self.publish(AlongPipe.FOUND_NEW_PIPE, core.Event())
        self._lastPipeLoc = newPipeLoc
        
        # Update the targets state
        angle = 0
        if event.x < 0.5 and event.y < 0.5:
            angle = event.angle
        self._pipe.setState(event.x, event.y, angle)

    def enter(self):
        """Makes the vehicle follow along line outlined by the pipe"""
        self._lastPipeLoc = None
        self._pipe = ram.motion.pipe.Pipe(0,0,0)
        motion = ram.motion.pipe.Follow(pipe = self._pipe,
                                       maxSpeed = 5,
                                       maxSidewaysSpeed = 3)
        self.motionManager.setMotion(motion)

    def exit(self):
        self.motionManager.stopCurrentMotion()
       
class BetweenPipes(state.State):
    """
    When the vehicle is between two pipes, and can't see either.
    """
    LOST_PATH = core.declareEventType('LOST_PATH')
    
    @staticmethod
    def transitions():
        return {vision.EventType.PIPE_FOUND : Seeking,
                BetweenPipes.LOST_PATH : End }
    
    def enter(self):
        """We have driving off the 'end' of the pipe set a timeout"""
        self.timer = self.timerManager.newTimer(BetweenPipes.LOST_PATH, 15)
        self.timer.start()
        
        self.controller.setSpeed(5)
        
    def exit(self):
        self.controller.setSpeed(0)
        self.timer.stop()
        
class End(state.State):
    def enter(self):
        self.visionSystem.pipeLineDetectorOff()
        #print '"Pipe Follow"'