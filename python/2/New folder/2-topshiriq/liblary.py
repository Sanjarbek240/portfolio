from data import books

def show_books():
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book}")

def add_book(book):
    books.append(book)
    print(f"'{book}' kitobi qoshildi.")

def remove_book(index):
    try:
        removed_book = books.pop(index - 1)
        print(f"'{removed_book}' kitobi ochdi.")
    except IndexError:
        print("indeks xato!")

def search_book(keyword):
    found_books = [book for book in books if keyword.lower() in book.lower()]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print("Kitob topilmadi.")