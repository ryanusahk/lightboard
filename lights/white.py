# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel
 

pixel_pin = board.D18
 
# The number of NeoPixels
num_pixels = 60
ORDER = neopixel.GRB
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False,
                           pixel_order=ORDER)

while True:

	pixels.fill((240, 240, 240))
	pixels.show()
	time.sleep(0.1)

# while True:
#     for i in range(256):
#         pixels.fill((i, i, i))
#         pixels.show()
#         time.sleep(.1)