#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -P Helpers
curl -s -o Helpers/helpers.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/Algorithms/Helpers/helpers.py

echo "Done"
