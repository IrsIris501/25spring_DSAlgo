import heapq


class TreeNode:
    def __init__(self, weight, alphabet, left=None, right=None):
        self.weight=weight
        self.alphabet=alphabet
        self.left=left
        self.right=right
    def __lt__(self, other):
        if self.weight!=other.weight:
            return self.weight<other.weight
        else:
            temp1=sorted(self.alphabet)
            temp2=sorted(self.alphabet)
            return ord(temp1[0])<ord(temp2[0])

n=int(input())
heap=[]
for i in range(n):
    char, freq=input().split()
    freq=int(freq)
    heap.append(TreeNode(freq, {char}))
heapq.heapify(heap)
while len(heap)>1:
    t1=heapq.heappop(heap)
    t2=heapq.heappop(heap)
    heapq.heappush(heap, TreeNode(t1.weight+t2.weight, t1.alphabet | t2.alphabet, t1, t2))
huffman_tree=heapq.heappop(heap)

while True:
    try:
        s=input()
    except EOFError:
        break
    if ord(s[0])>=ord('A'):
        ans=''
        for i in range(len(s)):
            temp=''
            pos=huffman_tree
            while True:
                if s[i] in pos.left.alphabet:
                    temp+='0'
                    if not pos.left.left:
                        break
                    else:
                        pos=pos.left
                elif s[i] in pos.right.alphabet:
                    temp+='1'
                    if not pos.right.left:
                        break
                    else:
                        pos=pos.right
                else:
                    break
            ans+=temp
        print(ans)
    else:
        ans=''
        i=0
        s+='2'
        pos=huffman_tree
        while i<len(s):
            if s=='2':
                temp = list(pos.alphabet)
                ans += temp[0]
                break
            elif s[i]=='0':
                if pos.left:
                    pos=pos.left
                    i+=1
                else:
                    temp=list(pos.alphabet)
                    ans+=temp[0]
                    pos=huffman_tree

            else:
                if pos.right:
                    pos=pos.right
                    i+=1
                else:
                    temp = list(pos.alphabet)
                    ans += temp[0]
                    pos = huffman_tree
        print(ans)

