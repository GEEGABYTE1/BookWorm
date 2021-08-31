from Tree import*
import time
from hashmap import HashMap
from data import dictionaries
from bfs import bfs

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
                prompted_genre = prompted_genre.strip(" ")
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
                prompted_title = prompted_title.strip(" ")
                formatted_trees = self.genre_title()[1]
                formatted_dictionary = self.genre_title()[0]
                corres_genre = None
                for genre, titles in formatted_dictionary.items():
                    for title in titles:
                        if prompted_title in title:
                            corres_genre = genre 
                            break 
                        else:
                            continue 
                    if corres_genre == None:
                        continue 
                    else:
                        break
                
                if corres_genre == None:
                    time.sleep(0.5)
                    print("Sorry, that title does not seem to be in our program!")
                else:
                    corres_genre = corres_genre.title()
                    root_node = None
                    for tree in formatted_trees:
                        if tree.value == corres_genre:
                            root_node = tree
                            break

                    title_path = bfs(root_node, prompted_title)
                    desired_result = title_path[-1].value 
                    print("Title: {}".format(desired_result[0]))
                    print("Genre: {}".format(corres_genre))
                    print("Author: {}".format(desired_result[1]))
                    print("Price: {}".format(desired_result[-1]))



            elif prompt == "/search_author":
                prompted_author = str(input("Please enter a name of an author you would like to search: "))
                prompted_author = prompted_author.title()
                prompted_author = prompted_author.strip(" ")
    
    def genre_title(self):
        updated_dicts = {}
        counter = 0
        for genre in self.book_choices:
            updated_dicts[genre] = []
        
        for dictionary in dictionaries:
            for title, info in dictionary.items():
                genre = updated_dicts.get(self.book_choices[counter])
                genre.append([title, info[0], info[-1]])
            
            counter += 1
        
        trees = []
        for genre, titles in updated_dicts.items():
            root_node = TreeNode(genre)
            for title in titles:
                root_node.add_child(TreeNode(title))
            trees.append(root_node)
        
        return updated_dicts,trees


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
