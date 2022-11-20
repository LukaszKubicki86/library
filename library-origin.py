import random
import sys

filmy = {}
class Movie:
    def __init__(self, title, publish, type):
        self.title = title
        self.publish = publish
        self.type = type
       
    def cos(self):
        print(filmy)
    
    def cos2(self):
        num = int(input("Ilość Elementów"))
        
        for i in range(num):
            roll= i+1
            Tytuł = input("Podaj tytuł ")
            Data_wydania = input("Data produkcji ")
            typ = input("Typ: ")
            filmy[roll]= [[Tytuł],[Data_wydania],[typ]]
        
    def cos3(self):
        s = input("Co chcesz znalezc: ")
        if s in filmy:
            print("\n Jest na liscie ")
        else:
            print("\n Nie ma na liscie")
    def cos4(self):
        n = 2
        print(random.sample(filmy, k=n))

class Series:
    def __init__(self, title, publish, type, sezon, episode):
        self.title = title
        self.publish = publish
        self.type = type
        self.sezon = sezon
        self.episode = episode
       
    def cos(self):
        print (filmy)  
        
    def cos2(self):
        num = int(input("Ilość Elementów"))
        
        for i in range(num):
            roll= i+1
            Tytuł = input("Podaj tytuł ")
            Data_wydania = input("Data produkcji ")
            typ = input("Typ: ")
            sezon = input("Sezon:")
            odcinek = input("odcinek")
            filmy[roll]= [[Tytuł],[Data_wydania],[typ],[sezon],[odcinek]]
        
    def cos3(self):
        s = input("Co chcesz znalezc: ")
        if s in filmy:
            print("\n Jest na liscie ")
        else:
            print("\n Nie ma na liscie")
    def cos4(self):
        n = 2
        print(random.sample(filmy, k=n))



class library(Movie,Series):
    def __init__(self):
        self.lst = {"Tytul":[]}
        self.choices = {
            "1":self.see,
            "2":self.dodaj,
            "3":self.search,
            "4":self.losowanie,
            "5":self.quit
            
        }
    def display_menu(self):
        print("""library Menu
1. Pokaz liste
2. Add 
3. Search
4. Random
5. Quit""")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Wybierz co chcesz zrobić ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def see(self):
        print (library.cos(self))
        
        print (library.cos(self))
        anykay = input("Enter anything to return to main menu")
        library()
        
    def dodaj(self):
        library.cos2(self)
        library.cos2(self)
        anykay= input("Enter anything to return to main menu")
        library()
        
    def search(self):
        library.cos3(self)
        anykay= input("Enter anything to return to main menu")
        library()
        
    def losowanie(self):
        library.cos4(self)
        anykay = input("Enter anything to return to main menu")
        library()
        
    def quit(self):
        print("Dziekuje za skorzystanie z biblioteki")
        sys.exit(0)
    

if __name__ == "__main__":
    library().run()            
    