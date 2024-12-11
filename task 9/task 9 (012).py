class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

class Book(Document):
    def __init__(self,title,author,genre=None,pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages
    def display_info(self):
        if self.genre and self.pages:
            return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Pages: {self.pages}"
        else:
            return f"Title: {self.title}, Author: {self.author}"
    def initialize(self,title,author,genre=None,pages=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
    def display_book_info(self):
        return self.display_info()

class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi
    def display_info(self):
        if self.journal and self.doi:
            return f"Title: {self.title}, Author: {self.author}, Journal: {self.journal}, DOI: {self.doi}"
        else:
            return f"Title: {self.title}, Author: {self.author}"
    def initialize(self,title,author,journal=None,doi=None):
        self.title = title
        self.author = author
        self.journal = journal
        self.doi = doi
    def display_article_info(self):
        return self.display_info()

def save_document_to_file(filename, document):
    with open(filename, 'a') as file:
        file.write(f"{document.title}, {document.author}")
        if isinstance(document, Book):
            file.write(f", {document.genre}, {document.pages}\n")
        elif isinstance(document, Article):
            file.write(f", {document.journal}, {document.doi}\n")
def read_documents_from_file(filename):
    try:
        with open(filename, 'r') as file:
            documents = file.readlines()
        return documents
    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []
def display_documents_from_file(filename):
    documents = read_documents_from_file(filename)
    if documents:
        for document in documents:
            print(document.strip())
    else:
        print("No documents found in the file.")
def main():
    filename = "documents.txt"
    
    while True:
        print("\nMenu:")
        print("1. Add new book")
        print("2. Add new article")
        print("3. Display all documents")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre (or press Enter to skip): ")
            pages = input("Enter number of pages (or press Enter to skip): ")
            genre = genre if genre else None
            pages = int(pages) if pages else None
            book = Book(title, author, genre, pages)
            save_document_to_file(filename, book)
            print("Book added successfully.")
        elif choice == '2':
            title = input("Enter article title: ")
            author = input("Enter article author: ")
            journal = input("Enter journal name (or press Enter to skip): ")
            doi = input("Enter DOI (or press Enter to skip): ")
            journal = journal if journal else None
            doi = doi if doi else None
            article = Article(title, author, journal, doi)
            save_document_to_file(filename, article)
            print("Article added successfully.")
        elif choice == '3':
            display_documents_from_file(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
