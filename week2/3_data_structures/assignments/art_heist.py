import csv
from geopy.distance import distance as geopy_distance

inwoners_filename = 'inwoners.csv'
buitenland_filename = 'buitenland.csv'
lengte_filename = 'lengte.csv'
geboortedatum_filename = 'geboortedatum.csv'
beroepscrimineel_filename = 'beroepscrimineel.csv'
postcode_filename = 'postcode.csv'
postcode_coordinaat_filename = 'postcode_coordinaat.csv'
output_filename = 'daders.csv'

def main():
    # implement this function and save your results to 'output_filename'
    with open(output_filename, 'w') as file:
        file.write('id, naam\n')
    print('saved results to:', output_filename)

if __name__ == '__main__':
    main()
