# Design Your Own Class!

class Production_House:
    def __init__(self, name, yr_founded, location):
        self._name = name                 # Protected attribute
        self._yr_founded = yr_founded     # Protected attribute
        self._location = location         # Protected attribute

    # Getter methods (Encapsulation)
    def get_name(self):
        return self._name

    def get_year_founded(self):
        return self._yr_founded

    def get_location(self):
        return self._location

    # Setter methods (Encapsulation)
    def set_location(self, new_location):
        self._location = new_location

    # Method to be overridden (Polymorphism)
    def display_info(self):
        print(f"Production House: {self._name}")
        print(f"Founded: {self._yr_founded}")
        print(f"Location: {self._location}")


# Child Class
class Movies(Production_House):
    def __init__(self, prod_name, yr_founded, location, movie_name, year, genre, director):
        super().__init__(prod_name, yr_founded, location)  # Inheritance
        self.__movie_name = movie_name      # Private attribute
        self.__year = year
        self.__genre = genre
        self.__director = director

    # Getter and Setter for private attributes
    def get_movie_name(self):
        return self.__movie_name

    def set_movie_name(self, new_name):
        self.__movie_name = new_name

    # Overriding method (Polymorphism)
    def display_info(self):
        super().display_info()  # Call parent version
        print(f"Movie: {self.__movie_name}")
        print(f"Year: {self.__year}")
        print(f"Genre: {self.__genre}")
        print(f"Director: {self.__director}")


# Example usage
movie1 = Movies("Skybound Entertainment", 2010, "California, USA",
                "Invincible", 2021, "Animation", "Jeff Allen")

movie2 = Movies("Amazon Studios", 2010, "California, USA",
                "The Boys", 2021, "Thriller", "Eric Kripke")

movie1.display_info()
print(" " * 30)
movie2.display_info()


# --------------------------
# 2. Polymorphism Challenge!

# Parent class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Child classes with different move() implementations
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water...")

# Create objects
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism
for v in vehicles:
    v.move()
