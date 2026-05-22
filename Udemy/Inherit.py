# Day 21 - 100 Days of Code

class Animal: # Super Class
    def __init__(self):
        self.eyes = 2
    
    def breathe(self):
        print("Inhale & Exhale!")

class Fish(Animal): # Sub Class
    def __init__(self):
        super().__init__() # Inheritance
    
    def breathe(self):
        super().breathe()
        print("Underwater!")
    
    def swim(self):
        print("\nMoves in water!")

nemo = Fish()
# nemo.swim()
nemo.breathe()
# print(nemo.eyes)