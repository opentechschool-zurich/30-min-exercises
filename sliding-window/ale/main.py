pattern = "T--X---T" # 8 chars
records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]

"""
<li>If any of the ‘T' positions in the pattern are bigger or equal to 'X’ the malware replaces 'X' with 0.</li>
<li>If the 'X' position in the pattern is near the left or right border and is missing a 'T' position neighbor, only the other side is considered.</li>
<li>The malware finds all the positions first and only then sets them to 0.</li>
"""

def conditions_1_and_3_only(records, pattern):
    # print(records)
    replacements = [] # index to replace
    for x in range(0, len(records) - len(pattern) + 1):
        window = records[0+x:8+x]
        # print(window)  
        if window[0] >= window[3] or window[7] >= window[3]:
            replacements.append(x + 3)
    # print(replacements)
    for i in replacements:
        records[i] = 0

    print(records)

# conditions_1_and_3_only(records, pattern)

def should_reset(records, i):
    if i >= 3 and records[i - 3] >= records[i]:
        return True
    if i < len(records) - 4 and records[i + 4] >= records[i]:
        return True
    return False

def erase_by_pattern(records):
    result = []
    for i, v in enumerate(records):
        if should_reset(records, i):
            result.append(0)
        else:
            result.append(v)
    print(result)

erase_by_pattern(records)
