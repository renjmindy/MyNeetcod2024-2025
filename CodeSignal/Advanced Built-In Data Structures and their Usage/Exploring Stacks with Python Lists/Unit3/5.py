# TODO: Initialize a dictionary named participant_scores (name -> score mapping) to track the scores of different participants (Feel free to choose any participant names and scores)
#from sortedcontainers import SortedDict
#sd = SortedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2})
#sd_rev = SortedDict({score: name for name, score in sd.items()})

mp = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
mp_sorted = sorted(mp.items(), key = lambda x:x[1], reverse=True)
vlist = list(mp.values())
vlist.sort(reverse=True)
# TODO: Determine who has the highest score and print their name as the top performer
#print(sd_rev.peekitem(sd_rev.bisect_left(4))[1])
print(mp_sorted[0][0])
print(vlist)
