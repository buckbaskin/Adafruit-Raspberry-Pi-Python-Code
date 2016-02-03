In rainbowCycle, line 73:

setpixelcolor(pixels, i, Wheel( ((i * 256 / len(pixels)) + j) % 256) )

The division i * 256 / len(pixels) is intended to be integer division.

In Python2, this works. In Python3, the single division (/) does floating division.

The fix to this is to use i * 256 // len(pixels).

This will do integer division in both versions of Python.