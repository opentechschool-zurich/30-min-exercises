# Given two strings, write a program that efficiently finds the longest common subsequence.
#
#       aaaaaaz
#       a
# bbzbbbb
#       b
#       aaaaaaz
#       a
#  bbzbbbb
#       b


#
#     lol
#   oao    0
#     lol
#    oao   0, 1
#     lol
#     oao  0, 0, 0
#     lol
#      oao 1, 0
#     lol
#       oao 0

def find_longest_common_subsequence(a, b):
    if len(a) < len(b):
       a, b = b, a 
    match_len = 0
    longest_match = 0
    n = 0
    longest_matching_string = ""
    for i in range(len(a) + len(b) - 1):
        if i < len(b):
            a_i = 0
            b_i = len(b) - 1 - i
            n += 1
        else:
            a_i = i - len(b) + 1
            b_i = 0  
            if i >= len(a):
                n -= 1
        match_len = 0
        for j in range(n):
            if a[a_i + j] == b[b_i + j]:
                match_len += 1
                if match_len > longest_match:
                    longest_match = match_len
                    longest_matching_string = a[a_i + j - (match_len - 1):a_i + j + 1]
            else:
                match_len = 0
    return longest_matching_string

# assert(find_longest_common_subsequence("ich bin", "blind") == 'ies')
assert(find_longest_common_subsequence("ich bin", "blind") == 'in') # lang <-> kurz
assert(find_longest_common_subsequence("blind", "bin ich") == 'in') # kurz <->
assert(find_longest_common_subsequence("french fries fresh and frizzleb", "spanish spoons spike spies wooo :3 uwu") == 'ies ')
assert(find_longest_common_subsequence("abc", "def") == '')
# assert(find_longest_common_subsequence(string_2, string_1) == 'ies')
