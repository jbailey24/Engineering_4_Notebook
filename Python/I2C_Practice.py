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

padding = 2
top = padding
x = padding

font = ImageFont.load_default()


while True:

  #reads accel values
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel

  #prints and scales
  #105 was chosen because it scales z value to approximately 9.8 when flat and at rest
  draw.text((x, top), 'ACCEL DATA:', font=font, fill=255)
  draw.text((x, top+12),    'X: '+ str(round(accel_x/105, 2)),  font=font, fill=255)
  draw.text((x, top+24), 'Y: '+ str(round(accel_y/105, 2)), font=font, fill=255)
  draw.text((x, top+36), 'Z: '+ str(round(accel_z/105, 2)), font=font, fill=255)

  disp.image(image)
  disp.display()
  
  time.sleep(1)
  
  #clears screen
  draw.rectangle((0,0,width,height), outline=0, fill=0)

