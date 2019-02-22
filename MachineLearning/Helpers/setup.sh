#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
mkdir -p Data
curl -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/MachineLearning/Helpers/helpers.py
curl -o Data/Fruit.csv https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/MachineLearning/Data/Fruit.csv
curl -o Data/Cats.csv https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/MachineLearning/Data/Cats.csv

echo "Done"
