from flask import Flask, render_template
import board
import datetime
import neopixel

pixels = neopixel.NeoPixel(board.D18, 69)

app = Flask(__name__)

@app.route("/")
def off():
    pixels.fill((0, 0, 0))

@app.route("/green")
def green():
    pixels.fill((0,40,0))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
