import json

files_to_read = [
    'Data/01_philosophers_stone.txt',
    'Data/02_chamber_of_secrets.txt',
    'Data/03_prisoner_of_azkaban.txt',
    'Data/04_goblet_of_fire.txt',
    'Data/05_order_of_the_phoenix.txt',
    'Data/06_half_blood_prince.txt',
    'Data/07_deathly_hallows.txt'
]

chapters_file = 'Data/chapters.json'

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

def load_chapter_names():
    with open(chapters_file) as input_file:
        chapters = json.load(input_file)
    return chapters

def load_chapters(book, chapter_names):
    book_chapters = []
    current_chapter = chapter_names[0]
    current_chapter_location = len(current_chapter) + 1
    for chapter in chapter_names[1:]:
        # find where next chapter starts
        if chapter in book:
            next_chapter_location = book.index(chapter)
        elif f'-\n{chapter.lower()}' in book.lower():
            next_chapter_location = book.lower().index(f'-\n{chapter.lower()}')
        elif f': {chapter.lower()}' in book.lower():
            next_chapter_location = book.lower().index(f': {chapter.lower()}')
        else:
            next_chapter_location = book.lower().index(f'\n{chapter.lower()}\n')
        # get chapter text -- all text from the location of current chapter till the start of the next chapter
        book_chapters.append(book[current_chapter_location:next_chapter_location])
        # move start pointer to the next chapter
        current_chapter_location = next_chapter_location + len(chapter)
        # save next chapter name
        current_chapter = chapter
    # don't forget the last chapter
    book_chapters.append(book[current_chapter_location:])
    return book_chapters

def load_book_1_chapters():
    book_1 = load_book_1()
    chapter_names = load_chapter_names()
    return load_chapters(book_1, chapter_names[0]), chapter_names[0]

def load_book_2_chapters():
    book_2 = load_book_2()
    chapter_names = load_chapter_names()
    return load_chapters(book_2, chapter_names[1]), chapter_names[1]

def load_book_3_chapters():
    book_3 = load_book_3()
    chapter_names = load_chapter_names()
    return load_chapters(book_3, chapter_names[2]), chapter_names[2]

def load_book_4_chapters():
    book_4 = load_book_4()
    chapter_names = load_chapter_names()
    return load_chapters(book_4, chapter_names[3]), chapter_names[3]

def load_book_5_chapters():
    book_5 = load_book_5()
    chapter_names = load_chapter_names()
    return load_chapters(book_5, chapter_names[4]), chapter_names[4]

def load_book_6_chapters():
    book_6 = load_book_6()
    chapter_names = load_chapter_names()
    return load_chapters(book_6, chapter_names[5]), chapter_names[5]

def load_book_7_chapters():
    book_7 = load_book_7()
    chapter_names = load_chapter_names()
    return load_chapters(book_7, chapter_names[6]), chapter_names[6]

def load_all_chapters():
    book_chapters = []
    chapter_names = load_chapter_names()
    for book_number, book in enumerate(load_all_books()):
        chapters = load_chapters(book, chapter_names[book_number])
        book_chapters.append(chapters)
    return book_chapters, chapter_names
