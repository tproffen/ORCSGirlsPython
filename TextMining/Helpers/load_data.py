
files_to_read = [
    'Data/01_philosophers_stone.txt',
    'Data/02_chamber_of_secrets.txt',
    'Data/03_prisoner_of_azkaban.txt',
    'Data/04_goblet_of_fire.txt',
    'Data/05_order_of_the_phoenix.txt',
    'Data/06_half_blood_prince.txt',
    'Data/07_deathly_hallows.txt'
]

def load_book(book_path):
    with open(book_path) as input_file:
      return input_file.read()

def load_book_1():
    return load_book(files_to_read[0])

def load_book_2():
    return load_book(files_to_read[1])

def load_book_3():
    return load_book(files_to_read[2])

def load_book_4():
    return load_book(files_to_read[3])

def load_book_5():
    return load_book(files_to_read[4])

def load_book_6():
    return load_book(files_to_read[5])

def load_book_7():
    return load_book(files_to_read[6])

def load_all_books():
    books = []
    for file_to_read in files_to_read:
        books.append(load_book(file_to_read))
    return books
