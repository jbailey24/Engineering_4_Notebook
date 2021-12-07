import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

lsm303 = Adafruit_LSM303.LSM303()

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))


draw = ImageDraw.Draw(image)



font = ImageFont.load_default()


while True:

  #reads accel values
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  

  shape_width = round(10+(int(abs(accel_y/105)))*7)
  shape_height =round(10+(int(abs(accel_x/105)))*7)
  top = (height/2)-(shape_height/2)
  bottom = (height/2)+(shape_height/2)
  left = (width/2)-(shape_width/2)
  right = (width/2)+(shape_width/2)

  
  draw.ellipse((left, top, right, bottom), outline=255, fill=0)
  
  disp.image(image)
  disp.display()
  
  time.sleep(0.05)
  
  #clears screen
  draw.rectangle((0,0,width,height), outline=0, fill=0)
