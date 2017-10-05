import pyautogui
import time

def print_no_newline(string):
    import sys
    sys.stdout.write("\r")
    sys.stdout.write(string)
    sys.stdout.flush()
try:
    while True:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        ss = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        r = int(str(pixelColor[0]).rjust(3))
        g = int(str(pixelColor[1]).rjust(3))
        b = int(str(pixelColor[2]).rjust(3))
        hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
        hexstr=str(hex)
        res= ss + ' RGB: ('+ str(r) +','+ str(g) +','+ str(b) +') '+ 'HEX: '+ hexstr[:7] 
        print_no_newline(res)
        time.sleep(1.0)
except KeyboardInterrupt:
    print("\nDone...")