#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/mysterious_list.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/mysterious_list.py
echo "Done"
