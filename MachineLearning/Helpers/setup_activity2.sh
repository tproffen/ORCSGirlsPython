#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Data
curl -o Data/Fruit.csv https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/MachineLearning/Data/Fruit.csv
echo "Done"
