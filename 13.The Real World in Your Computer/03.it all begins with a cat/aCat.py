class Cat : 
    name = ""
    species = ""
    weight = 0
    color = ""

    def sleep(self) :
        print ( self.name + " is sleeping")
    def show(self) :
        print(self.species + " is the species of " + self.name)
    def eat(self, food) :
        print( self.name + " is eating " + food)

tom = Cat()
tom.name = "Tom"
tom.species = "Tabby"
tom.weight = 2
tom.color = "Orange"
tom.sleep()
tom.show()
tom.eat("croquettes")

athena = Cat()
athena.name = "Athena"
athena.species = "Siamese"
athena.weight = 1.5
athena.color = "Brown"
athena.sleep()

print("Athena is a " + athena.species + " cat.")
print("But Tom is a " + tom.species + " cat.")