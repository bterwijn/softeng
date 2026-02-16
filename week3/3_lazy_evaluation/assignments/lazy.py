import random
import itertools
random.seed(0)

MINIMAL_VOLUME = 0.1        # in cubic meters
TRUCK_VOLUME_CAPACITY = 20  # in cubic meters
NR_TRUCKS = 5

def random_length():
    """ Returns a random length in centimeters """
    return random.randint(1, 200)  # do not change this function

def get_package():
    """ Returns a package with dimension (x, y, z) """
    return (random_length(), random_length(), random_length())  # do not change this function

def get_packages():
    """ Returns an infinite generator of packages """
    # implement this function

def compute_volume(packages):
    """ Reads packages from generator 'packages' and
    Returns a generator of volumes of the packages in cubic meters """
    # implement this function

def larger_than(volumes, minimum):
    """ Reads volumes from generator 'volumes' and
    Returns a generator of volumes that are larger then 'minimum' """
    # implement this function

def fill_trucks(volumes):
    """ Reads volumes from generator 'volumes' and
    Returns a generator of trucks packed with packages until capacity is reached """
    # implement this function, you probably want to use 'yield' here

def get_first_n(trucks, n):
    """ Reads trucks from generator 'trucks' and
    Returns the first n trucks from the generator """
    # implement this function, have a look at 'itertools.islice'
        

if __name__ == "__main__":
    pipeline = get_packages()
    pipeline = compute_volume(pipeline)
    pipeline = larger_than(pipeline, MINIMAL_VOLUME)
    pipeline = fill_trucks(pipeline)
    pipeline = get_first_n(pipeline, NR_TRUCKS)

    for i, truck in enumerate(pipeline, 1):
        print(f'truck{i}: {truck} sum: {sum(truck):.3f} m3')
