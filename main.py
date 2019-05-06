# CircuitPython demo - NeoPixel
import time
import board
import neopixel
from datetime import datetime

pixel_pin = board.D18
num_pixels = 275
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.RGB)


# Initialize Pixel Map
i2c = [0]*180
c2i = []
for i in range(20):
	c2i.append([0]*9)

counter = 0
for x in range(20):
	for y in range(9):
		if x % 2:
			i2c[counter] = (x, y)
			c2i[x][y]=counter
		else:
			i2c[counter] = (x, 8-y)
			c2i[x][8-y]=counter
		counter += 1



def wheel(pos):
	# Input a value 0 to 255 to get a color value.
	# The colours are a transition r - g - b - back to r.
	if pos < 0 or pos > 255:
		return (0, 0, 0)
	if pos < 85:
		return (255 - pos * 3, pos * 3, 0)
	if pos < 170:
		pos -= 85
		return (0, 255 - pos * 3, pos * 3)
	pos -= 170
	return (pos * 3, 0, 255 - pos * 3)
 
 
def color_chase(color, wait):
	for i in range(num_pixels):
		pixels[i] = color
		time.sleep(wait)
		pixels.show()
	time.sleep(0.5)
 
 
def rainbow_cycle(wait):
	for j in range(255):
		for i in range(num_pixels):
			rc_index = (i * 256 // num_pixels) + j
			pixels[i] = wheel(rc_index & 255)
		pixels.show()
		time.sleep(wait)

def rainbow_seed(seed):
	for i in range(num_pixels):
		rc_index = (i * 256 // num_pixels) + seed
		pixels[i] = wheel(rc_index & 255)

def rainbow_single(wait):
	for j in range(255):
		for i in range(num_pixels-1, num_pixels):
			rc_index = (i * 256 // num_pixels) + j
			pixels[i] = wheel(rc_index & 255)
		pixels.show()
		time.sleep(wait)
 
 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 




DRAWMAP = {
	0:[(0, 0), (1, 0), (2, 0),
	   (0, 1),         (2, 1),
	   (0, 2),         (2, 2),
	   (0, 3),         (2, 3),
	   (0, 4), (1, 4), (2, 4)],

	1:[(0, 0), (1, 0),
	     	   (1, 1),
	     	   (1, 2),
	     	   (1, 3),
	   (0, 4), (1, 4), (2, 4)],

	2:[(0, 0), (1, 0), (2, 0),
					   (2, 1),
	   (0, 2), (1, 2), (2, 2),
	   (0, 3),
	   (0, 4), (1, 4), (2, 4)],

	3:[(0, 0), (1, 0), (2, 0),
					   (2, 1),
	   (0, 2), (1, 2), (2, 2),
					   (2, 3),
	   (0, 4), (1, 4), (2, 4)],

	4:[(0, 0),         (2, 0),
	   (0, 1),         (2, 1),
	   (0, 2), (1, 2), (2, 2),
					   (2, 3),
					   (2, 4)],

5:[(0, 0), (1, 0), (2, 0),
	 (0, 1),
	 (0, 2), (1, 2), (2, 2),
									 (2, 3),
	 (0, 4), (1, 4), (2, 4)],

6:[(0, 0), (1, 0), (2, 0),
	 (0, 1),
	 (0, 2), (1, 2), (2, 2),
	 (0, 3),         (2, 3),
	 (0, 4), (1, 4), (2, 4)],

7:[(0, 0), (1, 0), (2, 0),
									 (2, 1),
									 (2, 2),
									 (2, 3),
									 (2, 4)],

8:[(0, 0), (1, 0), (2, 0),
	 (0, 1),         (2, 1),
	 (0, 2), (1, 2), (2, 2),
	 (0, 3),         (2, 3),
	 (0, 4), (1, 4), (2, 4)],

9:[(0, 0), (1, 0), (2, 0),
	 (0, 1),         (2, 1),
	 (0, 2), (1, 2), (2, 2),
									 (2, 3),
	 (0, 4), (1, 4), (2, 4)],
}


OFFSETS = [(2, 2), (6, 2), (11, 2), (15, 2)]

def getTimeIndicies():
	timeIndicies = []
	timestr = datetime.now().strftime('%I%M')
	for t, o in zip(timestr, OFFSETS):
		for x in range(20):
			for y in range(9):
				if (x, y) in DRAWMAP[int(t)]:
					timeIndicies.append(c2i[x+o[0]][y+o[1]])
	return timeIndicies

def setIndicies(indicies, color):
	for i in range(num_pixels):
		if i in indicies:
			pixels[i] = color

def maskNonIndicies(indicies, color):
	for i in range(num_pixels):
		if i not in indicies:
			pixels[i] = color

while True:
	for seed in range(255):
		rainbow_seed(seed)  # Increase the number to slow down the rainbow
		timeIndicies = getTimeIndicies()
		maskNonIndicies(timeIndicies, BLACK)
		# setIndicies(timeIndicies, BLACK)
		pixels.show()
		time.sleep(0.1)


