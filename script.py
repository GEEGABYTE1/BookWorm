from Tree import*
import time

class Running:

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
            prompt = str(input(":"))
    
    def homepage(self):
        print("-"*49)
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*" + "\n")
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*")
        print("\t" + "     Welcome to BookWorm!")
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*" + "\n")
        print("*"  + "\t" +  "\t" + "\t" +  "\t" +  "\t" +  "\t" + "*" + "\n")
        print("-"*49)
       





test = Running()

print(test.running())
