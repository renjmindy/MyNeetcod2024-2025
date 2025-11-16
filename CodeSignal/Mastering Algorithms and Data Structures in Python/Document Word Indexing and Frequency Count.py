from collections import defaultdict
from collections import Counter

def keyword_index(docs):
    # implement this
    # pass
    ans = dict()
    
    for idx, doc in enumerate(docs):
        cnt = defaultdict(int)
        for word in doc.split(" "):
            cnt[word] += 1
            if word in ans: ans[word].update({idx: cnt[word]})
            else: ans[word] = {idx: cnt[word]}
        del cnt
            
    return ans

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  # Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}
