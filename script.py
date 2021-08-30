from Tree import*
import time
from hashmap import HashMap
from data import dictionaries

class Running:
    book_database = HashMap(1000)
    book_database.setter("Math", math_tree)
    book_database.setter("Computer Science", com_sci_tree)
    book_database.setter("Physics", physics_tree)
    book_choices = ["Math", "Computer Science", "Physics"]

    def running(self):
        self.homepage()
        print("\n")
        print("Currently, there are only 3 genres of books you can search from:")
        time.sleep(0.5)
        print("Math, Computer, and Physics!")
        time.sleep(0.8)
        print("There will be new genres coming soon!")
        time.sleep(0.3)
        
        
        while True:
            print("\n")
            print("Please type in a command:")
            time.sleep(1.1)
            print("If you don't know the commands, please refer to the README file within the project directory")
            prompt = str(input(":"))

            if prompt == "/view_genre":
                prompted_genre = input("What genre of books would you like to view: ")
                prompted_genre = prompted_genre.title()
                if not prompted_genre in self.book_choices:
                    self.error()
                else:
                    returned_genre = self.book_database.retrieve(prompted_genre)
                    print("-"*23)
                    time.sleep(0.8)
                    returned_genre.traverse()

            elif prompt == "/search_title":
                prompted_title = str(input("Please enter a title of a book you would like to search for: "))
                prompted_title = prompted_title.title()
                formatted_dictionary = self.genre_title()
            
            elif prompt == "/search_author":
                prompted_author = str(input("Please enter a name of an author you would like to search: "))
                prompted_author = prompted_author.title()
    
    def genre_title(self):
        updated_dicts = {}
        counter = 0
        for genre in self.book_choices:
            updated_dicts[genre] = []
        
        for dictionary in dictionaries:
            for title in dictionary.keys():
                genre = updated_dicts.get(self.book_choices[counter])
                genre.append(title)
            
            counter += 1
        
        


    def homepage(self):
        print("-"*49)
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*" + "\n")
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*")
        print("\t" + "     Welcome to BookWorm!")
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*" + "\n")
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*" + "\n")
        print("-"*49)

    def error(self):
        print("Oops, that genre does not seem to be in our program yet!")
        time.sleep(1)
        print("Here are our current choices: ")
        for genre in self.book_choices:
            print(genre)

       





test = Running()

print(test.running())
