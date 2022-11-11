import random

class Movie:
    def __init__(self , title ,publish , type ,play_counter) -> None:
        self.title = title
        self.publish = publish
        self.type = type
        self.play_counter = play_counter = 0
    
    def __repr__(self):
        return f"{self.title}  {self.publish}  {self.type} {self.play_counter}"
    
    
    def play(self ):
        self.play_counter += 1
        
  
    def generate_views(self ):
        self.play_counter *=10
    
class Series(Movie):
    def __init__(self , title , publish , type , play_counter , sezon , episode):
        super().__init__( title , publish , type , play_counter )
        self.sezon = sezon
        self.episode = episode
    def __repr__(self):
        return f" {self.title} {self.publish}  {self.type} {self.play_counter} {self.sezon} {self.episode} "
    
     


class Library:

    def __init__(self):
        self.library =[]
        

    def add(self, object):
        if not (type(object) == Movie or type(object) == Series): raise ValueError("To musi być film lub serial")
        self.library.append(object)
       
        
    def get_movies(self):
          return [i for i in self.library if type(i) == Movie]         
    
    def get_series(self):
          return [i for i in self.library if type(i) == Series]
    
m = Movie("Incepcja" , 2010 , "science-fiction" , 0)
s = Series("Dom z papieru", 2017 , "sensacyjny", 0 , "E02" ,"S1")
x = Library()
x.add(m)
x.add(s)

print(f'Film: {x.get_movies()}')
print(f'Serial: {x.get_series()}')