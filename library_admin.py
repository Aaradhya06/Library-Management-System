def addBook():
    while True:
        name=input("Enter Book Name: ").strip()
        if name:
            break
        else:
            print("Book Name can't be empty")
    author=input("Enter Author Name: ").strip()
    
    while True:
        year=input("Enter Publication Year: ")
        if year.isdigit():
            year=int(year)
            break
        else:
            print("Year must be an Integer")
    genre=input("Enter Book Genre: ").strip()

    while True:
        availability = input("Is the book available? (Y/N): ").lower()
        if availability in ["y", "n"]:
            availability=availability=="y"
            break
        else:
            print("only Y/N can be entered")
    bookId=f"BK{len(books)+1:03}"

    book={
        "id":bookId,
        "name":name,
        "author":author,
        "year":int(year),
        "genre":genre,
        "available":availability=='y'
    }
    books.append(book)
    print("Book added successfully!\n")

def listBooks():
    if not books:
        print("No books found.")
        return

    for idx, book in enumerate(books):
        if book["available"]:
            status="Available"
        else:
            status="Not Available"
        print(f"""\t\tIndex: {idx}
                ID: {book['id']}
                Title: {book['name']}
                Author: {book['author']}
                Status: {status}""")

def searchBook():
    if not books:
        print("No books available")
        return

    search=input("Enter the Book name to Search: ").lower()
    found=False

    for book in books:
        if (search in book["name"].lower()):
            print(f"""\t\tID: {book['id']}
                Title: {book['name']}
                Author: {book['author']}""")
            found=True
    if not found:
        print("No matching results were found.")

def viewBook():
    if not books:
        print("No books available.")
        return

    idx=int(input("Enter book index: "))
    if 0<= idx <len(books):
        book=books[idx]
        for key, value in book.items():
            print(f"{key}: {value}")
    else:
        print("Invalid index.")

def updateBook():
    if not books:
        print("No books Available")
        return
    
    idx = int(input("Enter book index: "))
    if 0<= idx <len(books):
        book=books[idx]
        name=input(f"Enter new Title ({book['name']}): ")
        author=input(f"Emter new Author ({book['author']}): ")
        genre=input(f"Enter new Genre ({book['genre']}): ")

        if name:
            book["name"]=name
        if author:
            book["author"]=author
        if genre:
            book["genre"]=genre
        print("Book updated successfully!")
    else:
        print("Invalid index.")

def deleteBook():
    if not books:
        print("No books Available")
        return
    
    idx=int(input("Enter book index: "))
    if 0<= idx <len(books):
        books.pop(idx)
        print("Book Successfully Deleted")
    else:
        print("Invalid index")

books=[]

print("Welcome to Library Admin CLI")
while True: 
    print("Choose [a]dd,[l]ist,[s]earch,[v]iew,[u]pdate,[d]elete or [q]uit")
    ip=input("Enter your choice: ").lower()

    if(ip=='a'):
        addBook()
    elif(ip=='l'):
        listBooks()
    elif(ip=='s'):
        searchBook()
    elif(ip=='v'):
        viewBook()
    elif(ip=='u'):
        updateBook()
    elif(ip=='d'):
        deleteBook()
    elif(ip=='q'):
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")