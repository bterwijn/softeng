import random
import itertools
random.seed(0)

MINIMAL_VOLUME = 0.1        # in cubic meters
TRUCK_VOLUME_CAPACITY = 20  # in cubic meters
NR_TRUCKS = 5

def random_length():
    """ Returns a random length in centimeters """
    return random.randint(1, 200)

def get_package():
    """ Returns a package with dimension (x, y, z) """
    return (random_length(), random_length(), random_length())

def compute_volume(package):
    """ Computes the volume of the package in cubic meters """
    x, y, z = package
    return round(x * y * z / 1e6, 3)

def larger_than(volume, minimum):
    """ Filter the packages that are larger than minimum """
    return volume > minimum

def fill_trucks():
    """ Returns a list of trucks with packed packages """
    trucks = []
    truck = []
    volume_sum = 0
    while True:
        package = get_package()
        volume = compute_volume(package)
        if larger_than(volume, MINIMAL_VOLUME):
            if volume_sum + volume > TRUCK_VOLUME_CAPACITY:
                trucks.append(truck)
                if len(trucks) >= NR_TRUCKS:
                    break
                truck = [volume]
                volume_sum = volume
            else:
                truck.append(volume)
                volume_sum += volume
    return trucks

if __name__ == "__main__":
    for i, truck in enumerate(fill_trucks(), 1):
        print(f'truck{i}: {truck} sum: {sum(truck):.3f} m3')
