# Grayscale library demo
# https://github.com/Timendus/thumby-grayscale
#
# Shows six different screens, then reboots. Cycle through the screens by
# pressing A or B.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


# Fix import path so it can find a local grayscale library if present
from sys import path as syspath
syspath.insert(0, '/Games/GrayscaleTest')

# Import dependencies
from thumbyButton import actionPressed
from machine import reset
from time import sleep_ms
from utime import ticks_us, sleep_us, ticks_diff
from thumbyGrayscale import display, Sprite

# Helper function

def waitKey():
    while actionPressed(): pass
    while not actionPressed(): pass
    while actionPressed(): pass

# Directly writing to the buffers

for s in range(4):
    if s & 1:
        m1 = 0xff
    else:
        m1 = 0
    if s & 2:
        m2 = 0xff
    else:
        m2 = 0
    sx = s * 18
    for y in range(5):
        sy = y * 72
        for x in range(18):
            display.buffer[sy + sx + x] = m1
            display.shading[sy + sx + x] = m2
display.show()
waitKey()

# Drawing primitives

display.drawFilledRectangle(0, 0, 72, 40, display.WHITE)
display.drawFilledRectangle(0, 0, 62, 30, display.LIGHTGRAY)
display.drawFilledRectangle(0, 0, 52, 20, display.DARKGRAY)
display.drawFilledRectangle(0, 0, 42, 10, display.BLACK)
display.drawText("Hello", 2, 31, display.LIGHTGRAY)
display.drawText("world!", 37, 31, display.DARKGRAY)
display.update()
waitKey()

# Sprites as full screen images

girlSprite = Sprite(72, 40, (bytearray([
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,68,21,106,149,74,41,2,120,254,254,255,255,255,255,127,127,127,126,126,120,48,64,0,0,0,0,0,0,0,0,2,1,4,18,9,38,217,36,84,160,80,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,0,128,
    218,248,230,255,127,191,252,254,244,250,249,194,227,224,240,168,176,40,0,0,0,0,0,0,0,0,0,0,0,0,3,20,43,68,186,69,40,160,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,224,240,119,31,31,63,59,57,54,121,63,127,191,255,31,239,
    23,73,130,0,0,0,0,0,0,0,64,0,0,0,0,40,128,0,0,0,0,2,1,22,9,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,240,248,248,252,254,254,255,255,255,235,0,224,248,254,78,0,1,28,13,15,2,11,2,1,0,0,0,128,192,64,0,0,0,88,2,0,0,0,0,0,55,64,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,128,128,252,255,255,255,255,255,255,255,127,255,127,62,63,31,7,0,0,0,128,192,224,224,240,240,240,240,248,246,255,250,253,60,252,28,253,30,160,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
]), bytearray([
    128,4,160,8,130,32,8,162,0,40,130,8,160,10,64,39,63,255,255,255,255,255,255,255,255,255,175,211,45,215,181,203,191,87,255,127,255,255,255,254,232,218,144,96,1,131,7,15,31,63,255,255,255,255,255,255,254,253,234,225,148,64,8,130,32,8,162,0,40,
    2,144,4,0,84,0,18,64,136,2,168,2,80,10,64,10,160,5,168,1,85,135,31,191,127,127,231,255,126,247,255,250,255,255,255,255,119,255,119,247,255,255,255,255,255,255,255,216,32,193,160,112,208,248,243,239,159,127,255,255,255,255,255,255,254,248,200,
    130,32,10,160,5,80,4,0,0,149,32,133,80,8,66,40,2,169,4,81,8,162,8,146,36,129,40,130,232,53,186,255,255,255,255,127,255,255,255,255,246,255,253,255,255,255,255,255,255,255,255,255,107,206,63,255,222,127,71,241,255,255,244,0,3,15,63,127,255,255,
    255,255,16,74,0,74,32,5,168,1,2,80,10,160,10,81,4,145,34,136,33,74,208,122,216,62,134,42,83,139,85,250,255,143,240,95,255,255,87,63,127,127,63,127,191,191,255,223,255,255,255,255,251,254,255,232,255,255,87,217,255,255,255,255,254,232,0,162,
    0,81,4,147,35,136,37,144,69,16,37,128,42,64,160,21,64,20,66,17,136,34,200,18,68,17,63,40,87,128,117,138,245,218,245,235,255,251,252,63,95,151,33,212,73,34,40,21,26,18,15,14,95,191,255,255,255,255,247,239,255,255,255,223,191,255,127,255,255,
    255,122,136,66,41,4,80,10,32,138,32,74,17,68,18,64,21,
])))

parrotSprite = Sprite(72, 40, (bytearray([
    64,0,0,0,0,0,0,0,0,0,0,0,40,24,36,156,46,94,63,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,254,252,244,240,240,224,192,128,0,0,0,0,0,160,128,128,128,128,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,64,254,255,255,254,124,0,1,127,255,255,255,254,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,191,255,111,255,255,255,255,255,255,255,255,255,248,248,240,224,224,128,192,130,129,3,6,147,
    98,112,112,128,128,128,128,128,0,0,0,0,0,0,128,135,207,223,231,224,0,0,0,3,7,7,15,15,31,31,63,255,127,255,255,127,255,191,111,191,119,95,183,79,191,95,191,95,7,23,143,223,247,255,247,255,255,255,255,255,255,255,255,255,245,215,111,255,255,255,
    253,252,241,192,132,207,207,203,195,131,0,128,240,124,62,222,255,223,223,143,147,159,33,7,13,19,4,4,0,0,0,0,3,0,0,1,6,3,3,0,1,2,3,0,1,6,2,5,3,0,2,133,11,198,33,213,99,85,177,231,90,181,239,187,239,63,239,94,184,231,5,23,127,151,127,251,71,54,
    125,56,153,128,16,254,105,14,143,141,131,6,73,247,170,4,16,64,2,4,0,0,0,0,0,0,0,0,0,0,0,0,128,0,128,32,128,80,128,0,160,0,144,0,131,8,67,20,67,21,178,79,181,74,189,134,187,86,189,11,64,181,105,210,128,64,0,19,127,2,132,
]), bytearray([
    224,64,0,0,0,0,0,0,0,0,0,48,248,252,254,254,255,255,253,254,253,250,117,252,52,122,122,212,114,232,242,208,160,169,81,160,161,72,160,216,176,200,224,137,225,177,201,83,10,42,10,13,73,23,168,96,128,164,210,0,128,232,224,224,230,225,244,242,224,
    244,245,106,0,0,0,20,40,4,40,4,18,72,16,253,86,193,19,167,255,223,127,119,185,6,107,19,13,74,6,66,37,200,119,90,235,94,187,221,20,223,186,255,183,251,251,231,251,245,251,251,255,253,254,223,251,255,122,149,76,15,166,24,117,169,235,211,119,215,
    239,239,247,255,251,252,128,192,192,192,128,128,0,0,88,40,192,129,238,253,255,255,255,254,223,222,191,76,188,24,248,22,248,254,240,254,249,255,253,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,254,232,
    241,195,207,223,255,255,254,254,252,250,239,255,255,255,223,223,255,255,231,231,227,192,176,252,255,253,254,245,254,255,255,255,255,255,255,223,191,77,255,251,223,227,255,91,247,95,127,255,255,191,255,191,255,223,127,255,255,255,255,255,255,
    255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,253,195,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,223,253,239,191,250,231,155,79,192,211,253,239,253,255,
    255,253,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
])))

display.drawSprite(girlSprite)
display.update()
waitKey()

display.drawSprite(parrotSprite)
display.update()
waitKey()

# Cat animation using a sprite

background = Sprite(
    16, 16,            # Dimensions
    (
        bytearray([    # Layer 1 data
            255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
            255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255
        ]),
        bytearray([    # Layer 2 data
            2,32,0,16,97,128,112,8,0,18,0,0,32,0,8,0,
            0,0,17,0,8,0,64,0,2,12,16,76,2,0,16,0
        ])
    ),
    0, 0               # Position
)

cat = Sprite(
    12, 9,             # Dimensions
    (
        bytearray([    # Layer 1 data
            175,7,169,254,237,255,191,157,190,233,
            255,175,1,1,0,1,1,1,1,1,1,1,1,1,
        ]),
        bytearray([    # Layer 2 data
            80,248,254,249,238,252,188,222,189,238,
            248,80,0,0,1,1,1,1,1,1,1,1,0,0,
        ])
    ),
    30, 15             # Position
)

catMask = Sprite(
    12, 9,             # Dimensions
    bytearray([        # Mask bitmap data
        175,7,1,0,1,3,3,1,0,1,7,175,1,1,0,0,0,0,0,0,0,0,1,1
    ]),
    30, 15             # Position
)

dx = dy = 1
while True:
    display.fill(display.WHITE)
    for x in range(0, 72, 16):
        for y in range(0, 40, 16):
            background.x = x
            background.y = y
            display.drawSprite(background)
    display.drawSpriteWithMask(cat, catMask)
    cat.x += dx
    cat.y += dy
    catMask.x += dx
    catMask.y += dy
    cat.mirrorX = dx < 0
    if cat.x == 0 or cat.x == 60:
        dx = -dx
    if cat.y == 0 or cat.y == 31:
        dy = -dy
    display.update()
    sleep_ms(50)

    if actionPressed():
        break

# Wait for key release
while actionPressed(): pass

# Bounce animation using drawing primitives

fps = -1
dx = 1
dy = 0
x = y = 0
frame_rate = 30
frame_microsec = int(1000000.0 / frame_rate)
while not actionPressed():
    t0 = ticks_us()
    display.fill(display.WHITE)
    display.drawFilledRectangle(x, y+0, 12, 4, display.LIGHTGRAY)
    display.drawFilledRectangle(x, y+4, 12, 4, display.DARKGRAY)
    display.drawFilledRectangle(x, y+8, 12, 4, display.BLACK)

    display.setPixel(0, 0, display.BLACK)
    display.setPixel(71, 0, display.BLACK)
    display.setPixel(0, 39, display.BLACK)
    display.setPixel(71, 39, display.BLACK)
    display.drawText(str(fps >> 4), 2, 2, display.LIGHTGRAY)

    display.show()

    x += dx
    if x < 0 or x > 72-12:
        dx = -dx
    y += dy >> 16
    dy += 16384
    if y >= 30:
        dy = (-dy * 50000) >> 16

    td = ticks_diff(ticks_us(), t0)
    if td == 0:
        td = 1
    fpsn = (1000000<<4)//td
    if fps == -1:
        fps = fpsn
    else:
        fps += (fpsn - fps) >> 5
    sleep_ms((frame_microsec - ticks_diff(ticks_us(), t0)) >> 10)
    sleep_us(frame_microsec - ticks_diff(ticks_us(), t0) - 12)

# End of demo!

display.disableGrayscale()
reset()
