def valid_brackets(text):
    brackets_depth = 0
    for c in text:
        if c == "(":
            brackets_depth += 1
        elif c == ")": 
            brackets_depth -= 1
        if brackets_depth < 0:
            return False
        
    if brackets_depth == 0:
        return True
    return False


# Tests
passing_tests = [
  "",
  "()",
  "()()",
  "(())",
  "((())())",
]

failing_tests = [
    "(",
    "())",
    ")(",
    "))((",
]

# for test in passing_tests:
#     print(valid_brackets(test) is True)

print(valid_brackets(passing_tests[0]) is True)
print(valid_brackets(passing_tests[1]) is True)
print(valid_brackets(failing_tests[0]) is False)
