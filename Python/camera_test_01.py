import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('Say Cheese')
    camera.capture('camera_code_1.jpg')
    time.sleep(.5)
    print('Done')
    
