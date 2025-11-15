def find_unique_string(words):
    # implement this
    # pass
    seen, duplicate = set(), set()
    
    for word in words:
        if word in seen: duplicate.add(word)
        else: seen.add(word)
        
    ans = ''
    
    for word in reversed(words):
        if word not in duplicate: ans = word; break
        
    return ans

print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'
print(find_unique_string(['hello', 'world', 'hello']))  # It should print: 'world'
print(find_unique_string(['hello', 'world', 'hello', 'world']))  # It should print: ''
print(find_unique_string([]))  # It should print: ''
