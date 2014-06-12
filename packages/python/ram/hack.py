import ext.vision
import ram.motion.seek
import time

B = None

def handleLight(event):
    global B
    B.setState(event.azimuth, 0, 0)
#    B.setState(event.azimuth, event.elevation, event.range)

def setup(hub):
    global B
    B = ram.motion.seek.PointTarget(0,0,0)
    motion = ram.motion.seek.SeekPoint(B)
    hub.subscribeToType(ext.vision.EventType.LIGHT_FOUND, handleLight)
    return motion

def slowDive(controller, depth):
    for i in xrange(0, depth * 10):
        controller.setDepth(i/10.0)
        time.sleep(1)
