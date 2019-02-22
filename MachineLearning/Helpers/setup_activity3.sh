#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
mkdir -p Data
curl -s -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/MachineLearning/Helpers/helpers.py
curl -s -o Data/Cats.csv https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/MachineLearning/Data/Cats.csv
echo "Done"
