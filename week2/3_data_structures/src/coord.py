class Coord:

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return str(self.values)

    def __setitem__(self, index, value):
        self.values[index] = value

c1 = Coord([1, 1])
c2 = Coord([1, 1])
print(id(c1), id(c2))  # 139940334891904 139940334097168 (different)

# identity-based equality and hashing is the default
print( c1 == c2 )            # False
print( hash(c1), hash(c2) )  # 7933673374520 7883269437765 (different)

coord_set = set([c1])
print(coord_set)          # {[1, 1]}
print( c1 in coord_set )  # True
print( c2 in coord_set )  # False  BAD!
