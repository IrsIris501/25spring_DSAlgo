class Allocator:
    def __init__(self, n: int):
        self.memory=[0 for i in range(n)]

    def allocate(self, size: int, mID: int) -> int:
        temp_start=-1
        for i in range(len(self.memory)):
            if self.memory[i]!=0:
                temp_start=i
            if self.memory[i]==0:
                if i-temp_start==size:
                    for j in range(temp_start+1, i+1):
                        self.memory[j]=mID
                    print(*self.memory)
                    return temp_start+1
        print(*self.memory)
        return -1

    def freeMemory(self, mID: int) -> int:
        ans=0
        for i in range(len(self.memory)):
            if self.memory[i]==mID:
                ans+=1
                self.memory[i]=0
        print(self.memory)
        return ans

n=int(input())
obj = Allocator(n)
while True:
    s=input()
    if s=='end':
        break
    if s[0]=='a':
        size, mID=map(int, input().split())
        print(obj.allocate(size,mID))
    else:
        mID=int(input())
        print(obj.freeMemory(mID))