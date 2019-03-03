from flask import Flask, render_template
import board
import datetime
import neopixel
from random import randint
import time

app = Flask(__name__)

NUMLEDS = 69
pixels = neopixel.NeoPixel(board.D18, NUMLEDS)
colors = {
    'red'  : (40, 0, 0),
    'green': (0, 40, 0),
    'blue' : (0, 0, 40),
    'off'  : (0, 0, 0)
}

def on(color):
    """
    Turn on each LED sequentially
    :param color: str, color of LED
    """
    for led in range(NUMLEDS):
        pixels[led] = color

def random():
    """
    Turn on each LED sequentially with random color
    """
    for led in range(NUMLEDS):
        pixels[led] = (randint(20, 150), randint(20, 150), randint(20, 150))

def wheel(pos):
    """
    From Adafruit NeoPixel Library Documentation
    """
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    
    return (r, g, b)

def rainbow_cycle(wait):
    """
    From Adafruit NeoPixel Library Documentation
    """
    for led_int in range(255):
        for led in range(NUMLEDS):
            pixel_index = (led * 256 // NUMLEDS) + led_int
            pixels[led] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def off():
    """
    Turn off each LED sequentially 
    """
    for led in reversed(range(NUMLEDS)):
        pixels[led] = colors['off']

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/off")
def all_off():
    off()
    return render_template('index.html')

@app.route("/green")
def green():
    on(colors['green'])
    return render_template('index.html')

@app.route("/red")
def red():
    on(colors['red'])
    return render_template('index.html')

@app.route("/blue")
def blue():
    on(colors['blue'])
    return render_template('index.html')

@app.route("/rainbow")
def rainbow():
    rainbow_cycle(0.05)
    return render_template('index.html')

@app.route("/random")
def all_random():
    random()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
