/*
 * Copyright (C) 2007 Robotics at Maryland
 * Copyright (C) 2007 Joseph Lisee <jlisee@umd.edu>
 * All rights reserved.
 *
 * Author: Joseph Lisee <jlisee@umd.edu>
 * File:  packages/vision/src/Vehicle.cpp
 */

// STD Includes
#include <iostream>

// Library Includes
#include <boost/foreach.hpp>

// Project Includes
#include "vehicle/include/Vehicle.h"
#include "vehicle/include/device/IDevice.h"
#include "sensorapi/include/sensorapi.h"

namespace ram {
namespace vehicle {

Vehicle::Vehicle(core::ConfigNode config) :
    m_config(config),
    m_sensorFD(-1),
    m_markerNum(0),
    m_depthCalibSlope(m_config["depthCalibSlope"].asDouble()),
    m_depthCalibIntercept(m_config["depthCalibIntercept"].asDouble()),
    m_calibratedDepth(false),
    m_depthOffset(0)
{
    std::string devfile =
        m_config["sensor_board_file"].asString("/dev/sensor");
    
    m_sensorFD = openSensorBoard(devfile.c_str());
    syncBoard(m_sensorFD);

    if (m_sensorFD < -1)
        std::cout << "Could not open sensor board\n";
    else
        unsafeThrusters();

    // Allocate space for temperate readings
    m_state.temperatures.reserve(NUM_TEMP_SENSORS);
}

Vehicle::~Vehicle()
{
    // Remove all references to the devices, will cause them to be destructed
    // this will cause the Thruster objects to be deleted and set the 
    // thrusters to nuetral.  The lone problem here is that these objects are
    // reference counted, so we can't be sure that there are not any 
    // references  floating around keeping the object from being destoryed.
    m_devices.clear();

    safeThrusters();
}
    
device::IDevicePtr Vehicle::getDevice(std::string name)
{
    return m_devices[name];
}

double Vehicle::getDepth()
{
    core::ReadWriteMutex::ScopedReadLock lock(m_state_mutex);
    return m_state.depth;
}

std::vector<std::string> Vehicle::getTemperatureNames()
{
    std::vector<std::string> names;

    // No current way to get actual sensor names
    for (int i = 0; i < NUM_TEMP_SENSORS; ++i)
        names.push_back("Unknown");
    
    return names;
}

std::vector<int> Vehicle::getTemperatures()
{
    core::ReadWriteMutex::ScopedReadLock lock(m_state_mutex);
    return m_state.temperatures;
}
    
void Vehicle::safeThrusters()
{
    boost::mutex::scoped_lock lock(m_sensorBoardMutex);
    
    if (m_sensorFD >= 0)
    {
        // Todo, check whether these succeed
        thrusterSafety(m_sensorFD, CMD_THRUSTER1_OFF);
        thrusterSafety(m_sensorFD, CMD_THRUSTER2_OFF);
        thrusterSafety(m_sensorFD, CMD_THRUSTER3_OFF);
        thrusterSafety(m_sensorFD, CMD_THRUSTER4_OFF);
    }
}

void Vehicle::unsafeThrusters()
{
    boost::mutex::scoped_lock lock(m_sensorBoardMutex);
    
    if (m_sensorFD >= 0)
    {
        // todo check whether these succeed
        thrusterSafety(m_sensorFD, CMD_THRUSTER1_ON);
        thrusterSafety(m_sensorFD, CMD_THRUSTER2_ON);
        thrusterSafety(m_sensorFD, CMD_THRUSTER3_ON);
        thrusterSafety(m_sensorFD, CMD_THRUSTER4_ON);
    }
}

void Vehicle::dropMarker()
{
    boost::mutex::scoped_lock lock(m_sensorBoardMutex);
    ::dropMarker(m_sensorFD, m_markerNum);
}

int Vehicle::startStatus()
{
    core::ReadWriteMutex::ScopedReadLock lock(m_state_mutex);
    return m_state.startSwitch;   
}

void Vehicle::printLine(int line, std::string text)
{
    if (m_sensorFD >= 0)
    {
        boost::mutex::scoped_lock lock(m_sensorBoardMutex);
        displayText(m_sensorFD, line, text.c_str());
    }
}
    
void Vehicle::getState(Vehicle::VehicleState& state)
{
    core::ReadWriteMutex::ScopedReadLock lock(m_state_mutex);
    state = m_state;
}

void Vehicle::setState(const Vehicle::VehicleState& state)
{
    core::ReadWriteMutex::ScopedReadLock lock(m_state_mutex);
    m_state = state;
}

void Vehicle::_addDevice(device::IDevicePtr device)
{
    m_devices[device->getName()] = device;
}

void Vehicle::update(double timestep)
{
    if (m_sensorFD >= 0)
    {
        core::ReadWriteMutex::ScopedWriteLock lockState(m_state_mutex);
        boost::mutex::scoped_lock lockSensor(m_sensorBoardMutex);

        // Depth
        double rawDepth = readDepth(m_sensorFD);
        m_state.depth = (rawDepth - m_depthCalibIntercept) /
            m_depthCalibSlope - m_depthOffset;;

        // If we aren't calibrated, take values
        if (!m_calibratedDepth)
        {
            m_depthFilter.addValue(m_state.depth);

            // After five values, take the reading
            if (5 == m_depthFilter.getSize())
            {
                m_calibratedDepth = true;
                m_depthOffset = m_depthFilter.getValue();
            }
        }
        
        //m_state.depth = rawDepth;
        // Status register
        int status = readStatus(m_sensorFD);
        m_state.startSwitch = status & STATUS_STARTSW;

        // Temperatures
        unsigned char temps[NUM_TEMP_SENSORS];
        readTemp(m_sensorFD, temps);

        // Copy the contents of temps into the temperature state
        std::copy(temps, &temps[NUM_TEMP_SENSORS - 1] + 1,
                  m_state.temperatures.begin());
    }
}

void Vehicle::calibrateDepth()
{
    m_depthFilter.clear();
    m_calibratedDepth = false;
}
    
} // namespace vehicle
} // namespace ram
