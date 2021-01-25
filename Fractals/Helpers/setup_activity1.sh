#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/Fractals/Helpers/helpers.py

# Getting Turtle extension from Artistic Math!
curl -s -o Helpers/turtle.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/ArtisticMath/Helpers/turtle.py

echo "Done"
