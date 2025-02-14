class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        """Display the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print()

book1 = Book("Defend Me, Attorney", "Josh Gonzales", 2021)
book2 = Book("Convict Me, Attorney", "Josh Gonzales", 2022)
book3 = Book("Kill Me, Attorney", "Josh Gonzales", 2023)

book1.describe()
book2.describe()
book3.describe()

