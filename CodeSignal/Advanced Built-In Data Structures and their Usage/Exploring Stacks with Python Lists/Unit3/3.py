from sortedcontainers import SortedDict

# Create a SortedDict from the given dictionary
sd = SortedDict({'pomegranate': 10, 'grape': 15, 'orange': 20, 'apple': 5})

# TODO: Determine and print the fruit that comes right after 'grape' in our catalog
print(sd.peekitem(sd.bisect_right('grape')))
