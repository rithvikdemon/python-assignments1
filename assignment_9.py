#Queston 1

class Circle():
   
   def __init__(self,r):
      self.radius = r
      
   def getArea(self):
      return(3.14*self.radius*self.radius)
     
   def getCircumference(self):
      return(2*3.14*self.radius)

x = Circle(4)
print("Area: ", x.getArea())
print("Circumference: ", x.getCircumference())


#Question 2

class Student():

   def __init__(self,n,r):
      self.name = n
      self.roll_no = r

   def display(self):
      print("Name: ",self.name)
      print("Roll no: ",self.roll_no)

x = Student('shilpa',87)
x.display()

#Question 3

class Temperature():

   def __init__(self,c,f):
      self.celsius = c
      self.fahrenheit = f

   def convertFahrenheit(self):
      return(self.celsius*1.8+32)

   def convertCelsius(self):
      return((self.fahrenheit-32)/1.8)

x = Temperature(54,28)
print("Fahrenheit from Celsius: ", x.convertFahrenheit())

print("Celsius from Fahrenheit: ", x.convertCelsius())

#Question 4

class MovieDetails:

    def __init__(self,MovNa,ArtNa,YOR,Rat):

        self.MovieName = MovNa

        self.ArtistName = ArtNa

        self.YearOfRelease = YOR

        self.Ratings = Rat

    def display(self):

        print("Movie Name-> %s\nArtist Name-> %s\nYear Of Release-> %d\nRatings-> %d"%(self.MovieName,self.ArtistName,self.YearOfRelease,self.Ratings))

    def update(self,MNa,ANa,YR,R):

        self.MovieName = MNa

        self.ArtistName = ANa

        self.YearOfRelease = YR

        self.Ratings = R



movie = MovieDetails("Batman","bat",2008,10)

movie.display()

movie.update("superman","Super",2009,10)

movie.display()


#Question 5


class Expenditure():

   def __init__(self,e,s):
      self.expenditure = e
      self.savings = s

   def display(self):
      print("Expenditure: ", self.expenditure)
      print("Savings: ",self.savings)

   def calc(self):
      self.total_salary = self.expenditure+self.savings

   def displaySalary(self):
      print("Total salary: ",self.total_salary)
      
x = Expenditure(40000,30000)
x.display()
x.calc()
x.displaySalary()

