# _______Iterator_______

s = 'String'
s_itr = iter(s)

# Iterator has an argument with the index of the next element (forgets about the past elements)
# we can use s_itr.__next__() or next(s_itr)
# print(s_itr.__next__())
# print("__reduce__", s_itr.__reduce__()) # <- (<built-in function iter>, ('String',), 1) 1 is the inedx of the next element

# print("__reduce__", s_itr.__reduce__()[0])
# print("__reduce__", s_itr.__reduce__()[1])
# print("__reduce__", s_itr.__reduce__()[2])



# _______Generator_______

n = 50_000_000

def gen(n: int):
    for i in range(n):
        yield i**2

# g = gen(n)
# print(sum(g))

g = gen(10)

# We can use __next__() and next() but CAN'T use __reduce__ for generator
# print(g.__next__())
# print(next(g))

# g.__next__() # -> skip 0
# for i in g: # -> 1, 4, 9, 16, 25, 36, 49, 64, 81
#     print(i)


# Simple example of iterator
class Iter:
    def __init__(self, n):
        self.n = n
        self.current = -1

    # def __iter__(self): # The iter function is used to check whether an object is iterable and if it is, than we can use __next__
    #     return self
    
    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current
    

itr = Iter(5)
print(itr)

# if class Iter doesn't have __iter__ method, than for loop will not work -> TypeError: 'Iter' object is not iterable
# But we still can use __next__ without __iter__ method and we won't get TypeError
for i in itr:
    print(i)