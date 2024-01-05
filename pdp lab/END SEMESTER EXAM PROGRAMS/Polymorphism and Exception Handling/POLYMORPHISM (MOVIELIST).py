class Movie:

    def __init__(self,title,genre):
        self.title=title
        self.genre=genre

    def __str__(self):
        return f"{self.title} ({self.genre})"


class MovieList(list):

    def __init__(self,genre):
        super().__init__()
        self.genre=genre

    def append(self,movie):
        if movie.genre==self.genre:
            super().append(movie)

    def __gt__(self,other):
        return len(self)>len(other)

movie1=Movie('ironman','action')
movie2=Movie('batman','thriller')
movie3=Movie('spiderman','action')

list1=MovieList('action')
list2=MovieList('thriller')


list1.append(movie1)
list2.append(movie2)
list1.append(movie3)

if list1>list2:
    print('action movies list is bigger')
else:
    print('thriller movie list is bigger')

for i in list1:
    print(i)

for i in list2:
    print(i)
