#!/bin/bash
# Copy all needed files

echo "Fetching needed files .."
mkdir -p Helpers
curl -s -o Helpers/load_movies.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/load_movies.py
curl -s -o Helpers/plot_data.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/plot_data.py
curl -s -o Helpers/clean_data.py https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Helpers/clean_data.py
mkdir -p Data
curl -s -o Data/Bonus/01_phantom_menace.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/01_phantom_menace.txt
curl -s -o Data/Bonus/02_attack_of_the_clones.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/02_attack_of_the_clones.txt
curl -s -o Data/Bonus/03_revenge_of_the_sith.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/03_revenge_of_the_sith.txt
curl -s -o Data/Bonus/04_a_new_hope.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/04_a_new_hope.txt
curl -s -o Data/Bonus/05_the_empire_strikes_back.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/05_the_empire_strikes_back.txt
curl -s -o Data/Bonus/06_return_of_the_jedi.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/06_return_of_the_jedi.txt
curl -s -o Data/Bonus/07_the_force_awakens.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/Bonus/07_the_force_awakens.txt
curl -s -o Data/stopwords.txt https://raw.githubusercontent.com/tproffen/ORCSGirlsPython/master/TextMining/Data/stopwords.txt
echo "Done"
