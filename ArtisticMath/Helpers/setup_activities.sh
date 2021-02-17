#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ArtisticMath/Helpers/helpers.py
curl -s -o Helpers/turtle.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ArtisticMath/Helpers/turtle.py
curl -s -o Helpers/turtleCanvas.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ArtisticMath/Helpers/turtleCanvas.py

echo "Done"
