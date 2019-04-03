# Dictionary - locations
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India':['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt':['Cairo']}

# printing the USA cities in alphabetical order
sorted_locations = sorted(locations['North America']['USA'])
for city in sorted_locations:
    print(city)

print('# --- O --- #')
# printing the cities and their respective countries in Asia

from future.utils import iteritems
asia_cities = []
for countries, cities in iteritems(locations['Asia']):
    city_country = cities[0] + '-' + countries
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)
