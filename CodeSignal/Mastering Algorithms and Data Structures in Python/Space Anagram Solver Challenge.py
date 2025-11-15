from collections import defaultdict
def find_anagram_words(list_1, list_2):
    # implement this
    #pass
    mp = defaultdict(list)
    ans = list()
    
    for word in list_1:
        if ''.join(sorted(word)) not in mp: mp.setdefault(''.join(sorted(word)), []).append(word)
        else: mp[''.join(sorted(word))].append(word)
        
    for word in list_2:
        if ''.join(sorted(word)) in mp: ans += mp[''.join(sorted(word))]
    
    return list(set(ans))

print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []
