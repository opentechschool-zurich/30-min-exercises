def matching_brackets(input_text):
    matching_brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in input_text:
        if c in matching_brackets:
            stack.append(matching_brackets[c])
        elif c in matching_brackets.values():
            if stack[-1] == c:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def main():
    assert matching_brackets('()') == True
    assert matching_brackets('([)]') == False

if __name__ == '__main__':
    main()
