from sortedcontainers import SortedDict

# Create a SortedDict containing event names and their dates
event_dates = SortedDict({'Concert': '2023-06-21', 'Conference': '2023-07-12', 'Seminar': '2023-06-11', 'Workshop': '2023-08-05'})

# Invert the dictionary to have dates as keys for chronological ordering
date_events = SortedDict({date: event for event, date in event_dates.items()})

# TODO: Write logic to find and display the name of the event that is scheduled immediately after 'Seminar'
print(date_events.peekitem(date_events.bisect_right('2023-06-11'))[1])
