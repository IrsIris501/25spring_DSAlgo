from collections import deque
def palindrome(s):
    '''
    :param s: string
    :return: bool
    '''
    queue=deque(s)
    while len(queue)>1:
        a=queue.popleft()
        b=queue.pop()
        if a!=b:
            return False
    return True

while True:
    try:
        s=input()
    except:
        break
    print('YES' if palindrome(s) else 'NO')

