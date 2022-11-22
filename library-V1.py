import random
import sys

filmy = {}
class Movie:
    def __init__(self, title, publish, type):
        self.title = title
        self.publish = publish
        self.type = type
        
    def get_movie(self):
        num = int(input("Ilość filmów"))
        
        for i in range(num):
            roll= i+1
            Tytuł = input("Podaj tytuł ")
            Data_wydania = input("Data produkcji ")
            typ = input("Typ: ")
            filmy[roll]= [[Tytuł],[Data_wydania],[typ]]
        
        
class Series:
    def __init__(self, title, publish, type, sezon, episode):
        self.title = title
        self.publish = publish
        self.type = type
        self.sezon = sezon
        self.episode = episode
        
    def get_series(self):
        num = int(input("Ilość Elementów "))
        
        for i in range(num):
            roll= i+1
            Tytuł = input("Podaj tytuł ")
            Data_wydania = input("Data produkcji ")
            typ = input("Typ: ")
            sezon = input("Sezon:")
            odcinek = input("odcinek")
            filmy[roll]= [[Tytuł],[Data_wydania],[typ],[sezon],[odcinek]]
        
class Library(Movie, Series):
    def __init__(self):
        self.lst = {"Tytul":[]}
        self.choices = {
            "1":self.see,
            "2":self.get_movie,
            "3":self.get_series,
            "4":self.search,
            "5":self.generate_view
        }
        
    def display_menu(self):
         print("""Biblioteka filmów:
                1. Pokaz liste seriali
                2. Dodaj film
                3. Dodaj serial
                4. Szukaj
                5. Losowanie
                """)
         
    def run(self):
        while True:
            self.display_menu()
            choice = input("Wybierz co chcesz zrobić ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} wybierz jeszcze raz".format(choice))
                
    def see(self):
        print(filmy)
        anykay = input("wciśnij dowolny klawisz żeby wejść do menu")
        Library()
    
    def search(self):
        s = input("Co chcesz znalezc: ")
        if s in filmy:
            print("\n Jest na liscie ")
        else:
            print("\n Nie ma na liscie")
            
    def generate_view(self):
        if len(filmy) == 0:
            print('Lista jest pusta')
        else:
            n = 2
            los = random.sample(list(filmy.values()), k=n)
            print(los)
        
if __name__ == "__main__":  
    Library().run()  
    print (Library.see())
    print (Library.get_movie())
    print (Library.get_series())
    print (Library.search)
    print (Library.generate_view())
    
    