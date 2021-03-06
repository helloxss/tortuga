/*
 * Copyright (C) 2009 Robotics at Maryland
 * Copyright (C) 2009 Joseph Lisee <jlisee@umd.edu>
 * All rights reserved.
 *
 * Author: Joseph Lisee <jlisee@umd.edu>
 * File:  packages/packages/vehicle/test/include/MockVelocitySensor.h
 */

#ifndef RAM_VEHICLE_MOCKVELOCITYSENSOR_06_24_2009
#define RAM_VEHICLE_MOCKVELOCITYSENSOR_06_24_2009

// Project Includes
#include "vehicle/include/device/IVelocitySensor.h"
#include "vehicle/include/device/Device.h"

class MockVelocitySensor : public ram::vehicle::device::IVelocitySensor,
                           public ram::vehicle::device::Device
{
public:
    MockVelocitySensor(ram::core::ConfigNode config,
                       ram::core::EventHubPtr eventHub,
                       ram::vehicle::IVehiclePtr vehicle) :
        ram::vehicle::device::IVelocitySensor(eventHub,
                                              config["name"].asString()),
        Device(config["name"].asString()),
        velocity(config["velocity"][0].asDouble(0),
                 config["velocity"][1].asDouble(0))
    {
    }

    MockVelocitySensor(std::string name) :
        Device(name),
        velocity(0.0, 0.0),
        location(ram::math::Vector3::ZERO)
    {}

    ram::math::Vector2 velocity;
    ram::math::Vector3 location;

    virtual ram::math::Vector2 getVelocity() { return velocity; }
    virtual ram::math::Vector3 getLocation() { return location; }

    void publishUpdate(ram::math::Vector2 update)
    {
        velocity = update;
        ram::math::Vector2EventPtr nevent(
            new ram::math::Vector2Event());
        nevent->vector2 = update;
        publish(ram::vehicle::device::IVelocitySensor::UPDATE, nevent);
    }
    
    virtual std::string getName() {
        return ram::vehicle::device::Device::getName();
    }

    virtual void setPriority(ram::core::IUpdatable::Priority) {};
    virtual ram::core::IUpdatable::Priority getPriority() {
        return ram::core::IUpdatable::NORMAL_PRIORITY;
    };
    virtual void setAffinity(size_t) {};
    virtual int getAffinity() {
        return -1;
    };
    virtual void update(double) {}
    virtual void background(int) {}
    virtual void unbackground(bool) {}
    virtual bool backgrounded() { return false; }
};

#endif // RAM_VEHICLE_MOCKVELOCITYSENSOR_06_24_2009
