class Coord:

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return str(self.values)

    def __setitem__(self, index, value):
        self.values[index] = value

    def immu(self):
        return tuple(self.values)

c1 = Coord([1, 1])
c2 = Coord([1, 1])
print(id(c1), id(c2))  # 139940334891904 139940334097168  (different)

# immutable types have value-based equality and hashing
print( c1.immu() == c2.immu() )            # True
print( hash(c1.immu()), hash(c2.immu()) )  # 838904819212 838904819212 (same)

coord_set = set([c1.immu()])
print(coord_set)                 # {(1, 1)}
print( c1.immu() in coord_set )  # True
print( c2.immu() in coord_set )  # True  GOOD!
