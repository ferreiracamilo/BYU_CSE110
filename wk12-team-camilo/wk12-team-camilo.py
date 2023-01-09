import os

def filter_by_scripture(scripture,bookListChapter):
    new_book_list = []
    for book in bookListChapter:
        #Scripture,Book,Chapter
        if book[1].lower() == scripture.lower():
            new_book_list.append(book)
    return new_book_list

def get_dictionary_by_scripture(bookListChapter):
    dict_obj = {}
    for book in bookListChapter:
        # if book[1] not in dict_obj.keys():
        if book[0] not in dict_obj:
            dict_obj.update({book[0]: 1})
            # dict_obj[book[1]] = 1
        else:
            qty_temp_value = dict_obj.get(book[0]) + 1
            dict_obj.update({book[0]: qty_temp_value})
    #Dictionary is counting by each scripture, in case does not exist create a new entry for dictionary, otherwise sum one unit
    return dict_obj

def max_chapter(bookListChapter):
    max_chapter = 0
    max_scripture = ""
    max_book = ""
    # Scripture: Old Testament, Book: Genesis, Chapters: 50
    max_return = []
    for book in bookListChapter:
        if bookListChapter[1] > max_chapter:
            max_chapter = bookListChapter[2]
            max_scripture = book[0]
            max_book = book[1]
    one_book = [max_scripture,max_book,max_chapter]
    return one_book

### GLOBAL VARIABLES ###
list_books = []
### GLOBAL VARIABLES ###

### LOAD FILE BEFORE ASKING INPUT - DONE JUST ONCE ###
dir_path = os.path.dirname(os.path.realpath(__file__)) #retrieve root folder for py file
file_name = "books_and_chapters.txt"
final_path = ""

#REVIEW THE DIR PATH TO DECIDE WHAT CHAIN CHARS or CHAR TO PLACE so can be executed on different operative systems
if dir_path.find("/") != -1:
    final_path = dir_path + "/" + file_name
elif dir_path.find("//") != -1:
    final_path = dir_path + "//" + file_name
elif dir_path.find("\\") != -1:
    final_path = dir_path + "\\" + file_name

with open(final_path) as data_file:
    for line in data_file:
        line = line.strip().split(":") #It is splitted as well doing the strip to remove unwanted/unexpeted blank spaces
        #It is easier to save each employee as a list within the general employees list, it will be stored as
        #Scripture,Book,Chapter
        one_book = [line[2],line[0],int(line[1])]
        list_books.append(one_book)

print("1-Display all books in following format: 'Scripture: Old Testament, Book: Genesis, Chapters: 50'")
print("2-Find the largest number of chapters in the scriptures")
print("3-Find the book that has the largest number of chapters in the scriptures.")
print("4-Change your program so that it only prints the books in the Book of Mormon.")
print("5-Find the book in the Book of Mormon that has the largest number of chapters.")
print("6-At the beginning of the program, ask the user which volume of scriptures they would like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). Then, find the book in that volume of scripture that has the largest number of chapters.")
