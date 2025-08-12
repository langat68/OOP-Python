class Dog:
    def __init__(self,name, breed):
        self.name = name  #attributes
        self.breed = breed #attributes

    def bark(self):      # method
        print(f"{self.name}, says :woof!")    

my_dog = Dog("Buddy","Golden retriever") 
my_dog.bark()       
        