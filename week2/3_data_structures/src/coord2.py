class Coord:

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return str(self.values)

    def __setitem__(self, index, value):
        self.values[index] = value

    def __eq__(self, other):
        return self.values == other.values

    def __hash__(self):
        return hash(tuple(self.values))

c1 = Coord([1, 1])
c2 = Coord([1, 1])
print(id(c1), id(c2))  # 139940334891904 139940334097168 (different)

# we defined value-based equality and hashing for Coord objects
print( c1 == c2 )            # True
print( hash(c1), hash(c2) )  # 838904819212 838904819212 (same)

coord_set = set([c1])
print(coord_set)          # {[1, 1]}
print( c1 in coord_set )  # True
print( c2 in coord_set )  # True  GOOD!
