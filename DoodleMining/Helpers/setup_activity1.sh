#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/DoodleMining/Helpers/helpers.py

# Getting Turtle extension from Artistic Math!
curl -s -o Helpers/turtle.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ArtisticMath/Helpers/turtle.py
curl -s -o Helpers/turtleCanvas.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ArtisticMath/Helpers/turtleCanvas.py

# Getting updated QuickDraw Python API (for now)
mkdir -p Helpers/quickdraw
curl -s -o Helpers/quickdraw/data.py https://raw.githubusercontent.com/tproffen/quickdraw_python/fix-for-Python-3.7/quickdraw/data.py
curl -s -o Helpers/quickdraw/names.py https://raw.githubusercontent.com/tproffen/quickdraw_python/fix-for-Python-3.7/quickdraw/names.py

echo "Done"
