from Tree import*
import time
from hashmap import HashMap
from data import dictionaries
from bfs import bfs
from bfs_author import bfs_author
from bfs_price import bfs_price

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
                    print("\n")
                    print("-"*24)
                    print("Title: {}".format(desired_result[0]))
                    print("Genre: {}".format(corres_genre))
                    print("Author: {}".format(desired_result[1]))
                    print("Price: {}".format(desired_result[-1]))
            

            elif prompt == "/search_author":
                prompted_author = str(input("Please enter a name of an author you would like to search: "))
                prompted_author = prompted_author.title()
                prompted_author = prompted_author.strip(" ")
                author_tree = self.author_title()
                author_tree_root_node = self.author_title()
                author_search = bfs_author(author_tree_root_node, prompted_author)
                if author_search == None:
                    print("Oops, looks like that author is not registered on our software!")
                else:
                    desired_author = author_search[-1]
                    author_name = desired_author.value[0]
                    titles = desired_author.value[-1]
                    time.sleep(0.3)
                    print("\n")
                    print("-"*24)
                    print("Author: {}".format(author_name))
                    for title in titles:
                        title_name = title[0]
                        title_price = title[-1]
                        print("-"*24)
                        print("Title: {}".format(title_name))
                        print("Price: ${}".format(title_price))

            elif prompt == "/search_price":
                prompted_price = int(input("Please enter a price you would like to search by: "))
                price_tree = self.price_title()
                root_node = self.price_title()
                search_result = bfs_price(root_node, prompted_price)
                if search_result == None:
                    print("Oops, there is no book under the price you have listed yet! ")
                else:
                    price = search_result[-1].value[0]
                    books_info = search_result[-1].value[-1]
                    
                    print("\n")
                    print("-"*24)
                    print("Price: ${}".format(price))
                    for book in books_info:
                        print("-"*24)
                        print("Title: {}".format(book[0]))
                        print("Author: {}".format(book[1]))
                        print("Genre: {}".format(book[-1]))
            
            else:
                print("That command seems to be invalid!")
                        
    def price_title(self):
        updated_dicts = {}
        counter = 0 
        for dictionary in dictionaries:
            for title, book_info in dictionary.items():
                price = book_info[-1]
                price_status = updated_dicts.get(price, None)
                if price_status == None:
                    genre = self.book_choices[counter]
                    updated_dicts[price] = [[title, book_info[0], genre]]
                else:
                    updated_dicts[price].append([title, book_info[0], price])
            counter += 1

        price_tree = TreeNode("Prices")
        for price, book_info in updated_dicts.items():
            combined_tree_info  = (price, book_info)
            temp_tree_node = TreeNode(combined_tree_info)
            price_tree.add_child(temp_tree_node)
        
        return price_tree
        

    def author_title(self):
        updated_dicts = {}
        for dictionary in dictionaries:
            for title, book_info in dictionary.items():
                author_name = book_info[0]
                price = book_info[-1]
                author_status = updated_dicts.get(author_name, None)
                if author_status == None:
                    updated_dicts[author_name] = [[title, price]]
                else:
                    updated_dicts[author_name].append([title, price])
        
        author_tree = TreeNode("Authors")
        for author, title in updated_dicts.items():
            combined_author_info = (author, title)
            temp_tree_node = TreeNode(combined_author_info)
            author_tree.add_child(temp_tree_node)
        
        return author_tree
        
    
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
