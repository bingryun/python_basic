class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    for i in S:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            answer += i
        elif i == '(':
            opStack.push(i)
        elif i == ')':
            temp = opStack.pop()
            while temp != '(':
                answer += temp
                temp = opStack.pop()
        else :
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[i]) :
                answer += opStack.pop()
            opStack.push(i)
            
    while not opStack.isEmpty():
        answer += opStack.pop()
    return answer