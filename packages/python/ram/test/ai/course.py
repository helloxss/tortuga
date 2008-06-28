# Copyright (C) 2008 Maryland Robotics Club
# Copyright (C) 2008 Joseph Lisee <jlisee@umd.edu>
# All rights reserved.
#
# Author: Joseph Lisee <jlisee@umd.edu>
# File:  packages/python/ram/test/ai/course.py

"""
This module tests the ram.ai.course state Machine
"""

# Python Imports
import unittest

# Project Imports
import ram.ai.course as course
import ram.ai.gate as gate
import ram.ai.pipe as pipe
import ram.ai.light as light
import ram.ai.bin as bin

import ram.test.ai.support as support

class PipeTestCase(support.AITestCase):
    def checkStart(self, currentState):
        self.assertCurrentState(currentState)
        self.assertCurrentBranches([pipe.Searching])
        
    def checkSettled(self, nextState = None):
        self.injectEvent(pipe.Centering.SETTLED, sendToBranches = True)
        if not (nextState is None):
            self.assertCurrentState(nextState)
        
        # Make sure the gate.Dive branch is gone
        self.assertFalse(self.machine.branches.has_key(pipe.Searching))
        
        # Make sure we are not moving
        self.assertEqual(0, self.controller.speed)
        self.assertEqual(0, self.controller.sidewaysSpeed)
        
        # For the time being this is off
        self.assertFalse(self.visionSystem.pipeLineDetector)


class TestGate(support.AITestCase):
    def setUp(self):
        support.AITestCase.setUp(self)
        self.machine.start(course.Gate)
        
    def testStart(self):
        self.assertCurrentState(course.Gate)
        
        # Make sure we branched to the right state machine
        self.assertCurrentBranches([gate.Dive])
        
    def testGateComplete(self):
        # Make sure we have moved onto the next state
        self.injectEvent(gate.COMPLETE, sendToBranches = True)
        self.assertCurrentState(course.Pipe1)
        
        # Make sure the gate.Dive branch is gone
        self.assertFalse(self.machine.branches.has_key(gate.Dive))
        
class TestPipe1(PipeTestCase):
    def setUp(self):
        PipeTestCase.setUp(self)
        self.machine.start(course.Pipe1)
        
    def testStart(self):
        """
        Make sure that when we start we are doing the right thing
        """
        PipeTestCase.checkStart(self, course.Pipe1)
        self.assert_(self.visionSystem.pipeLineDetector)
        
    def testSettled(self):
        """
        Make sure that we move onto the light once we get over the pipe
        """
        PipeTestCase.checkSettled(self, course.Light)
        
class TestLight(support.AITestCase):
    def setUp(self):
        support.AITestCase.setUp(self)
        self.machine.start(course.Light)
        
    def testStart(self):
        """
        Make sure that when we start we are doing the right thing
        """
        self.assertCurrentState(course.Light)
        
        self.assertCurrentBranches([light.Searching])
        self.assert_(self.visionSystem.redLightDetector)
        
    def testLightHit(self):
        """
        Make sure that we move on once we hit the light
        """
        
        self.injectEvent(light.LIGHT_HIT, sendToBranches = True)
        self.assertCurrentState(course.Pipe2)
        
        # Make sure the light seeking branch is gone
        self.assertFalse(self.machine.branches.has_key(light.Searching))
        self.assertFalse(self.visionSystem.redLightDetector)
        
    def testTimeout(self):
        """
        Make sure that the timeout works properly
        """
        # Restart with a working timer
        self.machine.stop()
        self.machine.start(course.Light)
        
        # Release timer
        self.releaseTimer(course.Light.TIMEOUT)
        
        # Test that the timeout worked properly
        self.assertCurrentState(course.Pipe2)
        self.assertFalse(self.machine.branches.has_key(light.Searching))
        self.assertFalse(self.visionSystem.redLightDetector)
        
class TestPipe2(PipeTestCase):
    def setUp(self):
        PipeTestCase.setUp(self)
        self.machine.start(course.Pipe2)
        
    def testStart(self):
        """
        Make sure that when we start we are doing the right thing
        """
        PipeTestCase.checkStart(self, course.Pipe2)
        self.assert_(self.visionSystem.pipeLineDetector)
        
    def testSettled(self):
        """
        Make sure that we move onto the light once we get over the pipe
        """
        PipeTestCase.checkSettled(self, course.Bin)
        
class TestBin(support.AITestCase):
    def setUp(self):
        support.AITestCase.setUp(self)
        self.machine.start(course.Bin)
        
    def testStart(self):
        """
        Make sure that when we start we are doing the right thing
        """
        self.assertCurrentState(course.Bin)
        
        self.assertCurrentBranches([bin.Searching])
        self.assert_(self.visionSystem.binDetector)
        
    def testComplete(self):
        """
        Make sure that we move on once we hit the light
        """
        
        self.injectEvent(bin.COMPLETE, sendToBranches = True)
        self.assertCurrentState(course.Pipe3)
        
        # Make sure the light seeking branch is gone
        self.assertFalse(self.machine.branches.has_key(bin.Searching))
        self.assertFalse(self.visionSystem.binDetector)
        
    def testTimeout(self):
        """
        Make sure that the timeout works properly
        """
        # Restart with a working timer
        self.machine.stop()
        self.machine.start(course.Bin)
        
        # Release timer
        self.releaseTimer(course.Bin.TIMEOUT)
        
        # Test that the timeout worked properly
        self.assertCurrentState(course.Pipe3)
        self.assertFalse(self.machine.branches.has_key(bin.Searching))
        self.assertFalse(self.visionSystem.binDetector)
        
class TestPipe3(PipeTestCase):
    def setUp(self):
        PipeTestCase.setUp(self)
        self.machine.start(course.Pipe3)
        
    def testStart(self):
        """
        Make sure that when we start we are doing the right thing
        """
        PipeTestCase.checkStart(self, course.Pipe3)
        self.assert_(self.visionSystem.pipeLineDetector)
        
    def testSettled(self):
        """
        Make sure that we move onto the light once we get over the pipe
        """
        PipeTestCase.checkSettled(self) # End of course
        self.assert_(self.machine.complete)

        