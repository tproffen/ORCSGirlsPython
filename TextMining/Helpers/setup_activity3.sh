#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/load_data.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/load_data.py
curl -s -o Helpers/plot_data.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/plot_data.py
curl -s -o Helpers/clean_data.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/clean_data.py
mkdir -p Data
curl -s -o Data/01_philosophers_stone.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/01_philosophers_stone.txt
curl -s -o Data/02_chamber_of_secrets.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/02_chamber_of_secrets.txt
curl -s -o Data/03_prisoner_of_azkaban.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/03_prisoner_of_azkaban.txt
curl -s -o Data/04_goblet_of_fire.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/04_goblet_of_fire.txt
curl -s -o Data/05_order_of_the_phoenix.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/05_order_of_the_phoenix.txt
curl -s -o Data/06_half_blood_prince.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/06_half_blood_prince.txt
curl -s -o Data/07_deathly_hallows.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/07_deathly_hallows.txt
curl -s -o Data/stopwords.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/stopwords.txt
curl -s -o Data/chapters.json https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/chapters.json
echo "Done"
