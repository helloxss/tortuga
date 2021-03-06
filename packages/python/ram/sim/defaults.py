# Copyright (C) 2007 Maryland Robotics Club
# Copyright (C) 2007 Joseph Lisee <jlisee@umd.edu>
# All rights reserved.
#
# Author: Joseph Lisee <jlisee@umd.edu>
# File:  packages/python/ram/sim/defaults.py

"""
Constains default values for things settings the simulation
"""

import ogre.renderer.OGRE as Ogre

# Physics Defaults
gravity = Ogre.Vector3(0, 0, -9.8)

# Scene defaults
scene_log_config = {'name' : 'Unknown Scene', 'level': 'INFO'}
input_log_config = { 'name' : 'Input', 'level': 'INFO'}

# Ogre Defaults
camera_up_vector = Ogre.Vector3()

# Simulation defaults
ogre_plugins = ['RenderSystem_GL', 'Plugin_ParticleFX', 
                         'Plugin_OctreeSceneManager']

ogre_plugin_search_path = \
    ['C:\Libraries\PythonOgre\plugins',
     'C:\Developement\PythonOgre\plugins',
     '$MRBC_SVN_ROOT/deps/local/lib/OGRE',
     '/home/jlisee/projects/mrbc/trunk/deps/local/lib/OGRE']
    
render_system = 'OpenGL'

render_system_options = \
    [('Display Frequency', 'N/A'),
     ('FSAA', '0'),
     ('RTT Preferred Mode', 'FBO'),
     ('VSync', 'No')]

simulation_log_config = {'name' : 'Simulation', 'level': 'INFO'}

scene_search_path = 'data/scenes'
