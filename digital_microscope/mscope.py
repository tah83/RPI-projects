import picamera
from time import sleep


camera = picamera.PiCamera()
#camera.resolution = (1280, 720)
camera.resolution = (2592, 1944)   
camera.framerate = 15
camera.preview_fullscreen=False
camera.preview_window=(30, 26, 800, 600)

camera.led = False
camera.vflip=False
camera.hflip=False
camera.exposure_mode = 'auto'

zSize = 1
xPos = 0
yPos = 0

camera.start_preview()
camera.annotate_text = "Hello"
#camera.zoom = (0.0, 0.0, 1.0, 1.0)
camera.resolution = (2592, 1944)

while True:
    inkey = raw_input()
    try:  
        if inkey == "+":
            zSize -= 0.1
            if zSize < 0.2:
                zSize = 0.2 
        if inkey == "-":
            zSize +=0.1
            if zSize > 1:
	            zSize = 1
        if inkey == "d":
            xPos += 0.1
        if inkey == "a":
            xPos -= 0.1
            if xPos < 0:
                xPos = 0.0
        if inkey == "w":
            yPos -= 0.1
            if yPos <= 0:
                yPos = 0
        if inkey == "s":
            yPos += 0.1
        if yPos >=1-zSize:
            yPos = 1-zSize
        if xPos > 1-zSize:
            xPos = 1-zSize
        
        camera.annotate_text = "Zoom: %i%%" % (100-zSize*100)
        camera.zoom = (xPos,yPos,zSize,zSize)
        sleep(0.1)	
    except KeyboardInterrupt:
        camera.stop_preview()
        break

