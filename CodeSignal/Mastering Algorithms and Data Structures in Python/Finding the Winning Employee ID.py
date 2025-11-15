from collections import Counter

def elect_board_member(votes):
    # implement this
    # pass
    mp = Counter(votes)
    ans = list()
    
    mp_sorted = sorted(mp.items(), key=lambda x:x[1], reverse=True)
    
    #print(mp_sorted)
    
    for k, v in mp_sorted:
        if len(votes) % 3: 
            if v >= len(votes) // 3 + 1: ans.append(k)
        else:
            if v >= len(votes) // 3: ans.append(k)
        
    ans.sort()
    
    return ans[0] if ans else -1
    

print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1
