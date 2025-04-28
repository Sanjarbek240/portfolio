from liblary import show_books, add_book, remove_book, search_book

while True:
    print("Menyu:")
    print("kitoblar korish")
    print("qoshish")
    print("ochirish")
    print("qidirish")
    print("Chiqish")
    
    choice = input("tanlang (1-5): ")

    if choice == '1':
        show_books()
    elif choice == '2':
        new_book = input("kitob nomi: ")
        add_book(new_book)
    elif choice == '3':
        index = int(input("indeks kiriting: "))
        remove_book(index)
    elif choice == '4':
        keyword = input("kalit sozi: ")
        search_book(keyword)
    elif choice == '5':
        print("toxtadi")
        break
    else:
        print("xato")
