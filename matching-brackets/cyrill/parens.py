pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
}
closing = pairs.values()

def validate(input):
    stack = []
    for c in input:
        if c in pairs:
            stack.append(pairs[c])
        elif c in closing:
            if stack.pop() != c:
                return False
    return len(stack) == 0


assert validate('') == True
assert validate('()') == True
assert validate('([]{})[]') == True
assert validate('([)(])[]') == False
assert validate('hello, world') == True
assert validate('(hello)[world]') == True
assert validate('(') == False
assert validate('(])') == False
