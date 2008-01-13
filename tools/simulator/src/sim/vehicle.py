# Copyright (C) 2007 Maryland Robotics Club
# Copyright (C) 2007 Joseph Lisee <jlisee@umd.edu>
# All rights reserved.
#
# Author: Joseph Lisee <jlisee@umd.edu>
# File:  tools/simulator/src/sim/vehicle.py

"""
This module implements the ext.core.IVehicle interface in python using a 
simulation robot.
"""

# Library Imports
import ogre.renderer.OGRE as ogre

# Project Imports
import ext.core as core
import ext.vehicle as vehicle
import ext.vehicle.device as device
import ext.math as math
import math as pmath
import numpy as numpy

def convertToVector3(vType, vector):
    return vType(vector.x, vector.y, vector.z)

def convertToQuaternion(qType, quat):
    return qType(quat.x, quat.y, quat.z, quat.w)

class SimThruster(core.EventPublisher, device.IThruster):
    def __init__(self, name, simThruster):
        core.EventPublisher.__init__(self)
        device.IThruster.__init__(self)
        
        self._simThruster = simThruster
        self._name = name
                
    @property
    def relativePosition(self):
        return convertToVector3(math.Vector3, self._simThruster._force_pos)
                
    @property
    def forceDirection(self):
        return convertToVector3(math.Vector3, self._simThruster.direction)
                
    def getName(self):
        return self._name
    
    def setForce(self, force):
        self._simThruster.force = force
        
        event = core.Event()
        event.force = force
        self.publish(device.IThruster.FORCE_UPDATE, event)
    
    def getForce(self):
        return self._simThruster.force
    
    @property
    def maxForce(self):
        return self._simThruster.max_force
                
    def update(self, timestep):
        pass
    

class SimVehicle(vehicle.IVehicle):
    def __init__(self, config, deps):
        vehicle.IVehicle.__init__(self, config.get('name', 'SimVehicle'))
        sim = deps[0]
        self.robot = sim.scene._robots['AUT']
        self._devices = {}
    
        # Add Sim Thruster objects
        self._addThruster('PortThruster', self.robot.parts.left_thruster)
        self._addThruster('StartboardThruster', self.robot.parts.right_thruster)
        self._addThruster('AftThruster', self.robot.parts.aft_thruster)
        self._addThruster('ForeThruster', self.robot.parts.front_thruster)
        self._addThruster('TopThruster', self.robot.parts.top_thruster)
        self._addThruster('BotThruster', self.robot.parts.bot_thruster)

    def _addThruster(self, name, simThruster):
        self._devices[name] = SimThruster(name, simThruster)
    
    def getThrusters(self):
        thrusters = []
        for name in self.getDeviceNames():
            device = self.getDevice(name)
            if isinstance(device, vehicle.device.IThruster):
                thrusters.append(device)
        return thrusters
    
    def getDevice(self, name):
        return self._devices[name]
    
    def getDeviceNames(self):
        return self._devices.keys()
    
    def getDepth(self):
        # Down is positive for depth
        return -1 * self.robot._main_part._node.position.z
    
    def quaternionFromMagAccel(self, mag, accel):
        """
        Just here for reference, will be moved in the future
        """
        if accel == math.Vector3(0,0,0):
            accel = math.Vector3(0, 0, 0.084214)
        accel = accel + math.Vector3(0,0,-9.8);
        mag.normalise();
        
        n3 = accel * -1;
        n3.normalise();
        n2 = mag.crossProduct(accel);
        n2.normalise();
        n1 = n2.crossProduct(n3);
        n1.normalise();
        
        return math.Quaternion(n1,n2,n3);

    def getOrientation(self):
        return self._getActualOrientation()
        #return self.quaternionFromMagAccel(self.getMag(), self.getLinearAcceleration())
    
    def _getActualOrientation(self):
        return convertToQuaternion(math.Quaternion,
                                  self.robot._main_part._node.orientation)

    def getLinearAcceleration(self):
        baseAccel = convertToVector3(math.Vector3,
                                     self.robot._main_part.acceleration)
        # Add in gravity
        return baseAccel + math.Vector3(0, 0, -9.8)
    
    def getMag(self):
        return self._getActualOrientation() * math.Vector3(0.5, 0, -1);
    
    def getAngularRate(self):
        return convertToVector3(math.Vector3,
                                self.robot._main_part.angular_accel)   
    
    def _vectorToNumpyArray(self, vec):
        return numpy.array([vec.x, vec.y, vec.z])
    
    def applyForcesAndTorques(self, force, torque):
        thrusters = self.getThrusters()
        m = len(thrusters)
        A = numpy.zeros([6, m])
        
        for i in range(m):
            thruster = thrusters[i]
            maxThrusterForce = thruster.forceDirection * thruster.maxForce
            A[0:3,i] = self._vectorToNumpyArray(maxThrusterForce)
            A[3:6,i] = self._vectorToNumpyArray(thruster.relativePosition.crossProduct(maxThrusterForce))
        
        b = numpy.array([force.x, force.y, force.z, torque.x, torque.y, torque.z])
        (p, residuals, rank, s) = numpy.linalg.lstsq(A, b)
        
        for i in range(m):
            thruster = thrusters[i]
            thruster.setForce(thruster.maxForce * p[i])
    
    def backgrounded(self):
        return False
    
    def unbackground(self, join = True):
        pass
    
    def update(self, timeSinceUpdate):
        pass

core.SubsystemMaker.registerSubsystem('SimVehicle', SimVehicle)
