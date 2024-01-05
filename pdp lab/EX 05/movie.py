'''
Sadakopa Ramakrishnan
ex 5 pdp lab qn 3
Implement the classes Movie() and MovieList() as described in the above figure. Override the 
appropriate functions so that the MovieList is generated based on the genre assigned in the instance 
variable when first object is created. For example, if the genre is defined as thriller, the list accepts only 
thriller movies. 
When two lists are given as input, the list with more number of movies are returned
'''

class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def __str__(self):
        return "Movie name: {}\nGenre: {}".format(self.name, self.genre)

class MovieList(list):
    def __init__(self, genre):
        super().__init__()
        self.genre = genre

    def append(self, movie):
        if not isinstance(movie, Movie) or movie.genre != self.genre:
            raise TypeError("Only movies of the same genre can be added to the list")
        super().append(movie)

    def __str__(self):
        return "\nMovie list Genre: {}\nList: {}".format(self[0].genre, super().__str__())

    def __gt__(self, other):
        if not isinstance(other, MovieList):
            raise TypeError("Only MovieList objects can be compared")
        return self if len(self) >= len(other) else other

if __name__ == "__main__":

    crime_mov_1 = Movie("The Dark Knight", "Crime Thriller")  
    crime_mov_2 = Movie("Heat", "Crime Thriller")             
    adven_mov_1 = Movie("Indiana Jones and the Last Crusade", "Adventure")  
    adven_mov_2 = Movie("Jurassic Park", "Adventure")          

    crime_mov_lst = MovieList("Crime Thriller")
    crime_mov_lst.append(crime_mov_1)
    crime_mov_lst.append(crime_mov_2)

    adven_mov_lst = MovieList("Adventure")
    adven_mov_lst.append(adven_mov_1)
    adven_mov_lst.append(adven_mov_2)

    print("\nMovie List:")
    print(crime_mov_lst)
    print(adven_mov_lst)

    print("Greater > :")
    print(crime_mov_lst > adven_mov_lst)