#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ComputerArt/Helpers/helpers.py
curl -s -o Helpers/fractals.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/Fractals/Helpers/helpers.py
curl -s -o Helpers/turtle.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/Turtle/turtle.py
curl -s -o Helpers/turtleCanvas.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/Turtle/turtleCanvas.py

echo "Done"
