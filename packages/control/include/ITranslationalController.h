/*
 * Copyright (C) 2008 Robotics at Maryland
 * Copyright (C) 2008 Joseph Lisee <jlisee@umd.edu>
 * All rights reserved.
 *
 * Author: Joseph Lisee <jlisee@umd.edu>
 * File:  packages/control/include/ITranslationalController.h
 */

#ifndef RAM_CONTROL_ITRANSLATIONALCONTROLLER_08_31_2008
#define RAM_CONTROL_ITRANSLATIONALCONTROLLER_08_31_2008

// Project Includes
#include "math/include/Vector2.h"
#include "math/include/Vector3.h"
#include "math/include/Quaternion.h"

// Must Be Included last
#include "control/include/Export.h"

namespace ram {
namespace control {

/** Defines the interface for controler which controls in plane motion */
class RAM_EXPORT ITranslationalController 
{
public:
    virtual ~ITranslationalController() {}

    /** Set the desired velocity in meters/second (vehicle frame)
     *
     *  Note this overrides speed based control, set a desired velocity will
     *  implicity set an internal speed, to be fed to the vehicle.
     */
    virtual void setVelocity(math::Vector2 velocity) = 0;  

    /** Get the current desired velocity */
    virtual math::Vector2 getVelocity() = 0;
    
    /** Set the current speed, clamped between -5 and 5
     *
     *  Setting this turns off the velocity based control, and gives direct
     *  speed based control.
     */
    virtual void setSpeed(double speed) = 0;

    /** Set how fast the vehicle is going side to side (positive = right) */
    virtual void setSidewaysSpeed(double speed) = 0;

    /** Gets the current speed, a value between -5 and 5 */
    virtual double getSpeed() = 0;

    /** Gets the current sideways speed
     *
     *  @return
     *      A value between -5 (left) and 5 (right)
     */
    virtual double getSidewaysSpeed() = 0;
};

/** Provides an interface for a implementation of a Translational Controller */
class RAM_EXPORT ITranslationalControllerImp : public ITranslationalController
{
  public:    
    virtual ~ITranslationalControllerImp() {}

    /** Gets the needed vehicle force based on current vehicle state */
    virtual math::Vector3 translationalUpdate(double timestep,
                                              math::Vector3 linearAcceleration,
                                              math::Quaternion orientation,
                                              math::Vector2 position,
                                              math::Vector2 velocity) = 0;
};
    
} // namespace control
} // namespace ram

#endif // RAM_CONTROL_ITRANSLATIONALCONTROLLER_08_31_2008
