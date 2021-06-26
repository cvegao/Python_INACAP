class Animal:
    def __init__(self):
        self.name = None
        self.age = 0
        self.health_level = 0
        self.happiness_level = 0

    def display_info(self):
        print("Name: " + self.name)
        print("Health level: " + str(self.health_level))
        print("Happiness level: " + str(self.happiness_level) + "\n\n")
        return self

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self


class Lion(Animal):
    def __init__(self, name, age, favorite_food, health_level=20, happiness_level=10):
        super().__init__()
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
        self.favorite_food = favorite_food

    def feed(self):
        self.health_level += 5
        self.happiness_level += 15
        return self


class Tiger(Animal):
    def __init__(self, name, age, health_level=30, happiness_level=25):
        super().__init__()
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self):
        self.health_level += 10
        self.happiness_level += 5
        return self


class Bear(Animal):
    def __init__(self, name, age, health_level=20, happiness_level=10):
        super().__init__()
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self):
        self.health_level += 20
        self.happiness_level += 20
        return self


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age, favorite_food):
        self.animals.append(Lion(name, age, favorite_food))
        return self

    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))
        return self

    def add_bear(self, name, age):
        self.animals.append(Bear(name, age))
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

    # BONUS
    def interactive_adding_animals_sys(self):
        while True:
            print("Which type of animal do you want to add to the Zoo?\n1. Lion\n2. Tiger\n3. Bear\n0. Exit")
            option = input("Write the corresponding number here: ")
            if option == "1":
                name = input("Name: ")
                age = input("Age: ")
                favorite_food = input("Favorite food: ")
                self.add_lion(name, age, favorite_food)
            elif option == "2":
                name = input("Name: ")
                age = input("Age: ")
                self.add_tiger(name, age)
            elif option == "3":
                name = input("Name: ")
                age = input("Age: ")
                self.add_bear(name, age)
            elif option == "0":
                exit()
            else:
                print("Invalid option\n\n")


# lion = Lion("Leon", 10, "Gazelle")
# tiger = Tiger("Tigre", 5)
# bear = Bear("Oso", 1)
# lion.feed().display_info()

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 2, "Giraffe")
zoo1.add_lion("Simba", 12, "Zebra")
zoo1.add_tiger("Rajah", 4)
zoo1.add_tiger("Shere Khan", 3)
zoo1.print_all_info()

zoo1.interactive_adding_animals_sys()
zoo1.print_all_info()
