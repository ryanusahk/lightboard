# CircuitPython demo - NeoPixel
import time
import board
import neopixel
import random
 
pixel_pin = board.D18
num_pixels = 180
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.GRB)
 
 
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

def rainbow_single(wait):
    for j in range(255):
        for i in range(num_pixels-1, num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
 
def bpm(bpm):

    reps = 30000
    mpb = 1.0/(bpm*1.0 / (60*1000))
    spb = mpb/1000
    masterStartTime = time.time()
    # print(masterStartTime)
    for i in range(1,reps):
        timecheck = time.time()      
        elapsed = timecheck - masterStartTime
        delay = (i * spb) - elapsed

        time.sleep(delay)

        if 1-(i%2):
            fade_time = 0.05
            num_fades = int(int(spb / fade_time)/2)
            for i in range(num_fades):
                r1 = int(r1/1.2)
                g1 = int(g1/1.2)
                b1 = int(b1/1.2)
                pixels[:num_pixels//2] = [(r1, g1, b1)] * (num_pixels//2)

                r2 = int(r2/1.2)
                g2 = int(g2/1.2)
                b2 = int(b2/1.2)
                pixels[num_pixels//2:] = [(r2, g2, b2)] * (num_pixels//2)
                pixels.show()
                time.sleep(0.01)

        else:
            r1 = random.randint(0,255)
            g1 = random.randint(0,255)
            b1 = random.randint(0,255)
            pixels[:num_pixels//2] = [(r1, g1, b1)] * (num_pixels//2)

            r2 = random.randint(0,255)
            g2 = random.randint(0,255)
            b2 = random.randint(0,255)
            pixels[num_pixels//2:] = [(r2, g2, b2)] * (num_pixels//2)
            pixels.show()

        # if i%2:
        #     pixels.fill((0, 0, 0))
        #     pixels.show()

        # elapsed_time = (time.time() - masterStartTime) * 10
        # time.sleep(mpb/1000 - elapsed_time)

def learnBPM():
    times = []
    input(0)
    s = time.time()
    totalnum = 13
    for i in range(1, totalnum):
        input(str(i))
        now = time.time()
        times.append(now - s)
        s = now
    spb = sum(times)/(totalnum-1)
    # bpm = 2*(1/spb)*60
    bpm = (1/spb)*60
    print(bpm)
    return int(bpm)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
 
# b = learnBPM()
bpm(116)

# while True:
    # pixels.fill(RED)
    # pixels.show()
    # # Increase or decrease to change the speed of the solid color change.
    # time.sleep(1)
    # pixels.fill(GREEN)
    # pixels.show()
    # time.sleep(1)
    # pixels.fill(BLUE)
    # pixels.show()
    # time.sleep(1)
 
    # color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)
 	# rainbow_single(0.01)
    # rainbow_cycle(0.01)  # Increase the number to slow down the rainbow