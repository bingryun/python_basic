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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for i in tokenList:
        if type(i) is int:
            postfixList.append(i)
        elif i == ')':
            while opStack.peek() != '(':
                postfixList.append(opStack.pop())
            opStack.pop()
        else :
            if opStack.isEmpty() == False:
                if prec[opStack.peek()] >= prec[i] and i != '(':
                    postfixList.append(opStack.pop())
                    opStack.push(i)
                elif prec[opStack.peek()] >= prec[i] and i == '(':
                    opStack.push(i)
                else:
                    opStack.push(i)
            elif opStack.isEmpty() == True:
                opStack.push(i)
                
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    opStack = ArrayStack()
    for i in tokenList:
        if type(i) is int :
            opStack.push(i)
        elif i == '*':
            num1 = opStack.pop()
            num2 = opStack.pop()
            opStack.push(num2*num1)
        elif i == '/':
            num1 = opStack.pop()
            num2 = opStack.pop()
            opStack.push(num2/num1)
        elif i == '+':
            num1 = opStack.pop()
            num2 = opStack.pop()
            opStack.push(num2+num1)
        elif i == '-':
            num1 = opStack.pop()
            num2 = opStack.pop()
            opStack.push(num2-num1)
    return opStack.pop()
            


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val