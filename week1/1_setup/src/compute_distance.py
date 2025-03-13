import math

def main():
    coordinate = (3, 4, 2)
    print('coordinate: ', coordinate)
    print('has distance', compute_distance(coordinate) ,'to origin')

def compute_distance(coordinate):
    total = 0
    for c in coordinate:
        total += square(c)
    return math.sqrt(total)
        
def square(c):
    result = c * c
    return result

if __name__ == '__main__':
    main()
