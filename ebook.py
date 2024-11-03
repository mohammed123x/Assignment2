
class EBook:
    def __init__(self, title, author, publication_date, language, price, pages):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__language = language
        self.__price = price
        self.__pages = pages

    def __str__(self):
        return "Title : {}\tAuthor : {}\tPublish Date : {}\tLanguage : {}\tPrice : {}\tPages : {}".format(self.get_title(),
                                                                                                          self.get_author(),
                                                                                                          self.get_publication_date(),
                                                                                                          self.get_language(),
                                                                                                          self.get_price(),
                                                                                                          self.get_pages())

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages

