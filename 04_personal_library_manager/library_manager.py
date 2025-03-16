import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Library:
    def __init__(self):
        self.books = self.load_from_file()

    def load_from_file(self):
        try:
            with open("libraryDb.txt", "r") as file:
                books = []
                for line in file.readlines():
                    title, author, year, genre, read_status = line.strip().split("|")
                    books.append({
                        "Title": title,
                        "Author": author,
                        "Year": int(year),
                        "Genre": genre,
                        "ReadStatus": read_status.lower() == 'true'
                    })
                return books
        except FileNotFoundError:
            return []

    def add_book(self):
        clear()
        
        title = input("Enter the title of the book: ")
        author = input("Enter the author's name: ")
        year = int(input("Enter the publication year: "))
        genre = input("Enter the genre: ")
        read_status = input("Have you read the book? (y/n): ")
        read_status = read_status.lower() == 'y'

        self.books.append({
            "Title": title,
            "Author": author,
            "Year": year,
            "Genre": genre,
            "ReadStatus": read_status
        })

        print("Book added successfully!")
        input("Press Enter to continue...")
        clear()

    def remove_book(self):
        clear()
        title = input("Enter the title of the book to remove: ")
        for book in self.books:
            if book["Title"].lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!")
                return
        print("Book not found!")

    def search_book(self):
        clear()
        print("""Search by:
                    1. Title
                    2. Author:  """)
        search_by = int(input("Enter your choice: "))
        if search_by == 1:
            title = input("Enter the title of the book: ")
            for book in self.books:
                if book["Title"].lower() == title.lower():
                    clear()
                    print("\nFound the book!")
                    print(f"""\n\t\tTitle: {book['Title']},
                              Author: {book['Author']},
                              Year: {book['Year']},
                              Genre: {book['Genre']},
                              Read Status: {book['ReadStatus']}""")
                    return
            print("Book not found!")
        elif search_by == 2:
            author = input("Enter the author's name: ")
            for book in self.books:
                if book["Author"].lower() == author.lower():
                    print("Found the book!")
                    print(f"""Title: {book['Title']},
                              Author: {book['Author']},
                              Year: {book['Year']},
                              Genre: {book['Genre']},
                              Read Status: {book['ReadStatus']}""")
                    return
            print("Book not found!")

    def display_books(self):
        clear()
        print("All books:")
        for book in self.books:
            print(f"""Title: {book['Title']},
                      Author: {book['Author']},
                      Year: {book['Year']},
                      Genre: {book['Genre']},
                      Read Status: {book['ReadStatus']}""")

    def display_stats(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book['ReadStatus'])
        print("Total Books: ", total_books)
        print("Percentage Read: ", (read_books / total_books) * 100 if total_books > 0 else 0)

    def save_to_file(self):
        with open("libraryDb.txt", "w") as file:
            for book in self.books:
                file.write(f"{book['Title']}|{book['Author']}|{book['Year']}|{book['Genre']}|{book['ReadStatus']}\n")
        print("Library data saved to 'libraryDb.txt' successfully!")


def manage():
    library = Library()
    while True:
        
        print("""\n     Library Management System
                1. Add a book
                2. Remove a book
                3. Search for a book
                4. Display all books
                5. Display statistics
                6. Quit""")
        choice = int(input("\t\tEnter your choice: "))
        clear()
        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.remove_book()
            input("Press Enter to continue...")
        elif choice == 3:
            library.search_book()
            input("Press Enter to continue...")
        elif choice == 4:
            library.display_books()
            input("Press Enter to continue...")
        elif choice == 5:
            library.display_stats()
            input("Press Enter to continue...")
        elif choice == 6:
            library.save_to_file()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manage()
