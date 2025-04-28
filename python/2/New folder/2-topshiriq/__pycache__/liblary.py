from data import books
def show_books():
    for index,book in enumerate(books, start=1):
        print(f"{index}.{book}")
def add_book(book):
    books.append(book)
    print(f"{book}kitoblar orasiga qowildi")  
def remove_book(index):
    ochiriw = books.pop(index-1)
    print(f"{ochiriw}kitobi ochirili")
def search_book(keyword):
    qidiriw = [book for book in books if keyword.lower() in book.lower()]   
    if qidiriw:
        for book in qidiriw:
            print(book)
    else:
        print("kitob topilmadi")                   