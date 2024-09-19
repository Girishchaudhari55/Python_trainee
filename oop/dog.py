class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}."
dog1 = Dog("Buddy", 3)
print(dog1.description())  
print(dog1.speak("Woof!"))  

fork=Dog("fork",5)
print(fork.description())
print(fork.spaek("woof "))


dogs=[dog1, fork]
from functools import reduce
age_sum=reduce((lambda s, dog:s+dog.age), dogs, 0)
print(age_sum)

nums=[10,20,30,41]
nums_sum=reduce((lambda s,dog: s+ dog.age),dogs,0)