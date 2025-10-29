from sortedcontainers import SortedDict

# Initialize a SortedDict with a few countries and their populations
country_populations = SortedDict({'Nigeria': 206, 'Brazil': 213, 'Pakistan': 225, 'Indonesia': 276})

# TODO: Find the insertion point for 'Pakistan' and calculate the country that comes right before it in alphabetical order
print(country_populations.bisect_left('Pakistan'))

# Hint: Use the method that finds the insertion point in a SortedDict (bisect_left) and then access the country directly preceding that position (peekitem)

# TODO: Print the country that comes before 'Pakistan' in alphabetical order
print(country_populations.peekitem(country_populations.bisect_left('Pakistan') - 1))
