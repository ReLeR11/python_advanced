mapper = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y
}


def calculate(num1, num2, sign):
    func = mapper[sign]
    return func(num1, num2)