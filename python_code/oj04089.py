class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children={}

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert_check(self, char):
        ptr=self.root
        for i in range(len(char)):
            if char[i] in ptr.children:
                ptr=ptr.children[char[i]]
                if ptr.is_end:
                    return False
            else:
                ptr.children[char[i]]=TrieNode()
                ptr=ptr.children[char[i]]
        if ptr.children:
            return False
        ptr.is_end=True

        return True

t=int(input())
for _ in range(t):
    n=int(input())
    root=Trie()
    nums=[]
    for i in range(n):
        nums.append(input())
    avail=True
    for i in nums:
        avail=root.insert_check(i)
        if not avail:
            print('NO')
            break
    if avail:
        print('YES')


