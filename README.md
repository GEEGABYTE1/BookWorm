 # BookWorm 🪱

A book recommendation software for passionate readers! 

Readers can search books up based on genres, authors, prices, and titles. Moreover, they can save their desired books to their "bookshelf", for later reference if needed. Users can view the book's author, title, genre, and price relative to amazon *CAD*.

# Commands 🕹
*Note*: Some commands maybe valid only after another command has been typed.

 - `/view_genre`: Allows the user to view books from a specific genre 
 - `/search_title`: Allows the user to view information about a certain book.
 - `/search_author`: Allows the user to view various information about the book(s) from the desired author.
 - `/search_price`: Allows the user to view book(s) and their information based off a desired price.
 - `/search_by_highest`: Outputs books and their information from the *highest to lowest*.
 - `/search_by_lowest`: Outputs books and their information from *lowest to highest*.
 - `/view_bookshelf`: Allows the user to view their bookshelf, where all their saved books lie.
 - `/delete_book`: Prompts the user to delete a desired book from their bookshelf.
 - `/quit`: Quits the program

 ## Semi-Commands 🚚
 While the user may view a book(s) with a specific parameter, they will be prompted if they want to add the book to their bookshelf. They must type what's illustrated in the program (i.e, `yes` or `no`), otherwise, the program will deny the argument.
 
 The commands that are affected by this:
 - `/search_title`
 - `/search_author`
 - `/search_price`
 - `/search_by_highest`
 - `/search_by_lowest`
 

# Software Information 💻

## Database

The software has integrated a hashmap as the database for all the books. Each genre's tree is stored under a hashcode, which then gets retrieved when prompted by the user's command in constant time. 

## Genres 

The genres are integrated in trees. However, in `data.py` (where all the data is set), the genres are formatted as: `{title: [author, price]...}`. We stored each dictionary as a separate tree in order for easy breadth-first traversal when searching for a specific parameter. 

## Traversal (BFS)
All traversals were made using BFS. Notice that each paramter has it's own BFS algorithm. Though, the implementation is the same, however, our target and our search refernce changes for each parameter (i.e, price, title, author). 

The helper functions: `.price_title()`, `.author_title()`, and `genre_title()` are all functions that have re-formatted the dictionary for BFS traversal. For our base graph in `data.py`, we can see how the title of the book is set as the key. However, our helper functions re-format the dictionary where our specified parameter (author, title, or price) beacomes the key and the rest of the information (value) becomes the actual value. We do this for every time a search command is typed with a specific parameter. Moreover, to make the new re-formatted dictionary an eligible paramter for the algorithm, we re-create a new tree that reflects the dictionary. This will make our dictionary eligible for the algorithm, and just like every genre, there is now a tree for the specified parameter.

Time Complexity of re-factoring the dictionary and creation of the tree: `O(n^2)`
Time Complexity of BFS: `O(n)`

## Sorting
To allow the user to search by the highest or lowest price, we take the re-formatted dictionary from `price_title()` (read "Traversal" for more information about the function), and we implement the quicksort algorithm. We take the list of keys, which are the prices of each book and sort them accordingly, depending on what the user typed (highest or lowest). After sorting is done, we iteratively call each key in the list to it's value and print the value. 

In `data.py` we store separate lists of titles, authors, prices, and genres for printing reference. To know which piece of information is what, we reference these lists in order to annotate our return results for our users.

Time Complexity of Quicksort: `O(n log n)`


