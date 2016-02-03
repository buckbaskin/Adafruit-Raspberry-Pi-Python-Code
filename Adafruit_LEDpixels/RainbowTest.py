import unittest
from Adafruit_LEDpixels import Color, Wheel

print(Color(255,0,0))
print(Color(0,255,0))
print(Color(0,0,255))

for j in range(0,256):
    for i in range(25):
        print(str(i)+', '+str(j)+', '+str(Wheel( ((i * 256 / 25) + j) % 256)))