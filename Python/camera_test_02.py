
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.image_effect = 'sketch'
    time.sleep(2)
    print('Say Cheese')
    camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/pics/camera_code_2_sketch.jpg')
    camera.image_effect = 'pastel'
    time.sleep(1)
    camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/pics/camera_code_2_pastel.jpg')
    camera.image_effect = 'washedout'
    time.sleep(1)
    camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/pics/camera_code_2_washedout.jpg')
    camera.image_effect = 'cartoon'
    time.sleep(1)
    camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/pics/camera_code_2_cartoon.jpg')
    camera.image_effect = 'oilpaint'
    time.sleep(1)
    camera.capture('/home/pi/Documents/Engineering_4_Notebook/Python/pics/camera_code_2_oilpaint.jpg')
    time.sleep(.5)
    print('Done')
    
