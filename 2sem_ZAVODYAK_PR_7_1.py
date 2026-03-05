class HomeLibrary:

    def __init__(self):
        self.books = {}

    def add_book(self, number, info):
        self.books[number] = info

    def delete_book(self, number):
        if number in self.books:
            del self.books[number]

    def search_by_author(self, author):
        for number, book in self.books.items():
            if book['author'] == author:
                print(number, book)


    def search_by_year(self, year_of_publication):
        for number, book in self.books.items():
            if book['year'] == year:
                print(number, book)


    def get_book(self, number):
        print(self.books.get(number))


library = HomeLibrary()

library.add_book(1,{
    "author": "Stephen Kind",
    "nazva": "Кладовище домашніх тварин",
    "vudavnuztvo": "KCD",
    "genre": "horor",
    "year": 1936})


library.add_book(2,{
    "author": "Агата Крісті",
    "nazva": "Убивство по алфавіту",
    "genre": "детектив",
    "year": 1936})

library.search_by_author("Stephen Kind")

library.get_book(1)

library.delete_book(2)




