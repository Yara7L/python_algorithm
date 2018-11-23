# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素x推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

# O(n)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :param x:int
        :return: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :return:void
        """
        self.stack.pop()

    def top(self):
        """
        :return: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :return:int
        """
        return min(self.stack[:])

# O(1)
class MinStack2(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        if len(self.stack) != 0:
            if len(self.minstack) != 0 and self.stack[-1] == self.minstack[-1]:
                self.minstack.pop()
            self.stack.pop()

    def top(self):
        # 最小栈中，栈顶元素，越来越小，返回stack栈顶，符合要求 
        # return self.minstack[-1]
        return  self.stack[-1]

    def getMin(self):
        return self.minstack[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

    minStack2 = MinStack2()
    minStack2.push(-2)
    minStack2.push(0)
    minStack2.push(-3)
    print(minStack2.getMin())
    minStack2.pop()
    print(minStack2.top())
    print(minStack2.getMin())
