class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1

    def cound_down(self):
        self.value -= 1

    def __str__(self):
        return f"Count={self.value}"
    
    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception("Invalid type")

# count1 = Counter()
# count2 = Counter()

# count1.count_up()
# count2.count_up()

# print(count1, count2)
# print(count1 + count2)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Car(make={self.year}, model={self.model}, year={self.year})"
    

# mycar = Car('Tyota', 'Corolla', 2011)

# print(str(mycar))
# print(repr(mycar))

class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(name='{self.name}, quantity={self.quantity}')"

    def __add__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        
    def __sub__(self, other):
        ...
    
    def __mul__(self, factor):
        ...

    def __eq__(self, other):
        ...
        
    
# item1 = InventoryItem("Apple", 50)
# item2 = InventoryItem("Apple", 30)

# item3 = item1 + item2
# print(item3)