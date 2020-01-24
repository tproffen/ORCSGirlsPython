
files_to_read = [
    'Data/Bonus/01_phantom_menace.txt',
    'Data/Bonus/02_attack_of_the_clones.txt',
    'Data/Bonus/03_revenge_of_the_sith.txt',
    'Data/Bonus/04_a_new_hope.txt',
    'Data/Bonus/05_the_empire_strikes_back.txt',
    'Data/Bonus/06_return_of_the_jedi.txt',
    'Data/Bonus/07_the_force_awakens.txt'
]

def load_movie(movie_path):
    with open(movie_path) as input_file:
      return input_file.read()

def load_movie_1():
    return load_movie(files_to_read[0])

def load_movie_2():
    return load_movie(files_to_read[1])

def load_movie_3():
    return load_movie(files_to_read[2])

def load_movie_4():
    return load_movie(files_to_read[3])

def load_movie_5():
    return load_movie(files_to_read[4])

def load_movie_6():
    return load_movie(files_to_read[5])

def load_movie_7():
    return load_movie(files_to_read[6])

def load_all_movies():
    movies = []
    for file_to_read in files_to_read:
        movies.append(load_movie(file_to_read))
    return movies
