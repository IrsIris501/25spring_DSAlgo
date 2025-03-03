from collections import deque

class Queue:
    def __init__(self, teams):
        self.sequence=deque()
        self.teams=teams
        self.teams_inq=set()
        self.team_members_inq=[deque() for i in range(len(teams))]
    def enqueue(self, val):
        '''

        :param val: int
        '''
        for i in range(len(self.teams)):
            if val in self.teams[i]:
                if i in self.teams_inq:
                    self.team_members_inq[i].append(val)
                else:
                    self.sequence.append('Team '+str(i))
                    self.team_members_inq[i].append(val)
                    self.teams_inq.add(i)
                return

        self.sequence.append(val)

    def dequeue(self):
        temp=self.sequence.popleft()
        if type(temp)==type(' '):
            team_id=int(temp[5::])
            out=self.team_members_inq[team_id].popleft()
            if not self.team_members_inq[team_id]:
                self.teams_inq.remove(team_id)
            else:
                self.sequence.appendleft(temp)
            return out
        else:
            return temp




t=int(input())
teams=[]
for i in range(t):
    teams.append(list(map(int, input().split())))
q=Queue(teams)
while True:
    s=input()
    if s[0]=='S':
        break
    elif s[0]=='E':
        q.enqueue(int(s[8::]))
    else:
        print(q.dequeue())

