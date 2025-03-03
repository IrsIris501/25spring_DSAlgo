class MinStack(object):

    def __init__(self):
        self.item=[]
        self.helper=[]


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.item.append(val)
        if self.helper:
            if val<=self.helper[-1]:
                self.helper.append(val)
            else:
                self.helper.append(self.helper[-1])
        else:
            self.helper.append(val)


    def pop(self):
        """
        :rtype: None
        """
        self.item.pop()
        self.helper.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.item[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())# --> 返回 -3.
minStack.pop()
print(minStack.top())# --> 返回 0.
print(minStack.getMin())# --> 返回 -2.