class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def print_details(self):
        print(f"The Title of the book is {self.title} and the author name is {self.author}")

book1=book("'Girte Sitaare'","'N.K.Nayak'")
book1.print_details()