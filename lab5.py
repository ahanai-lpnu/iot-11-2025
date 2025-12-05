class Book:
    total_books_created = 0

    def __init__(self, title="Назва відсутня", author="Невідомий", price=0.0, pages=0, quantity=0, sales=0):
        self.__title = title
        self.__author = author
        
        self.set_price(price)
        self.set_pages(pages)
        self.set_quantity(quantity)
        self.set_sales(sales)
        
        Book.total_books_created += 1

    def __del__(self):
        Book.total_books_created -= 1

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        if value < 0:
            self.__price = 0.0
        else:
            self.__price = float(value)

    def get_pages(self):
        return self.__pages

    def set_pages(self, value):
        if value < 0:
            self.__pages = 0
        elif value % 1 != 0:
            self.__pages = 0
        else:
            self.__pages = int(value)

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, value):
        if value < 0:
            self.__quantity = 0
        elif value % 1 != 0:
            self.__quantity = 0
        else:
            self.__quantity = int(value)

    def get_sales(self):
        return self.__sales

    def set_sales(self, value):
        if value < 0:
            self.__sales = 0
        elif value % 1 != 0:
            self.__sales = 0
        else:
            self.__sales = int(value)

    def __str__(self):
        return (f"Книга: «{self.__title}» | Автор: {self.__author} | "
                f"Ціна: {self.__price} грн | Стор.: {self.__pages} | "
                f"На складі: {self.__quantity} | Продано: {self.__sales}")

    def __repr__(self):
        return f"Book(title='{self.__title}', price={self.__price}, sales={self.__sales})"

    def lists(self):
        return [self.__title, self.__author, self.__price, self.__pages, self.__quantity, self.__sales]


class BookShop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.inventory = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.inventory.append(book)
            print(f"Книгу «{book.get_title()}» додано до магазину '{self.shop_name}'.")
        else:
            print("Помилка: Об'єкт не є книгою.")

    def remove_book(self, title):
        initial_count = len(self.inventory)
        self.inventory = [b for b in self.inventory if b.get_title() != title]
        
        if len(self.inventory) < initial_count:
            print(f"Книгу «{title}» видалено з асортименту.")
        else:
            print(f"Помилка: Книгу «{title}» не знайдено.")

    def show_top_by_price(self):
        print(f"\nтоп книжок за ціною (від найдорожчої) в '{self.shop_name}'")
        sorted_books = sorted(self.inventory, key=lambda x: x.get_price(), reverse=True)
        for book in sorted_books:
            print(f"{book.get_title()} - {book.get_price()} грн")

    def show_top_by_sales(self):
        print(f"\nтоп книжок за продажами (бестселери) в '{self.shop_name}'")
        sorted_books = sorted(self.inventory, key=lambda x: x.get_sales(), reverse=True)
        for book in sorted_books:
            print(f"{book.get_title()} - продано {book.get_sales()} шт.")

    def show_all_books(self):
        print(f"\nВесь асортимент '{self.shop_name}'")
        for book in self.inventory:
            print(book)


def main():

    b1 = Book("Кобзар", "Т. Шевченко", 450.50, 720, 10, 500)
    b2 = Book("Тигролови", "І. Багряний", 320.00, 280, 5, 120)
    b3 = Book("Погана книжка", "Невідомський", -100, 100, 10, 0)
    b4 = Book("Половинка", "Дівак", 150, 50.5, 10, 0)
    b5 = Book("Супер топ топ книгга", "Хтось", 500, 200, 50, 1000.7)

    print("\nперевірочка\n")
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)

    shop = BookShop("Книгарня Є")
    
    shop.add_book(b1)
    shop.add_book(b2)
    shop.add_book(b3)
    shop.add_book(b4)
    shop.add_book(b5)

    shop.show_top_by_price()
    shop.show_top_by_sales()

    print("\nтест видалення")
    shop.remove_book("Супер топ топ книгга")
    
    shop.show_all_books()

    print(f"\nЗагальна кількість створених об'єктів Book: {Book.total_books_created}\n")

    print('Додаткове завдання:\n')
    all_books = [b1, b2, b3, b4]

    avg_pages = sum(b.get_pages() for b in all_books) / len(all_books)

    print('Нижче середнього всі книги:')
    print(f'Середнє сторінок серед книжок, до речі: {avg_pages}')
    for f in all_books:
        if f.get_pages() < avg_pages:
            print(f.get_title(), f.get_price())

if __name__ == "__main__":
    main()