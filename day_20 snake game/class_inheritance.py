class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
    
    def breathing(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    def swim(self):
        print("miving in water")
    def breathing(self):
        super().breathing()
        print("under water")
    

nemo = Fish()
nemo.breathing()