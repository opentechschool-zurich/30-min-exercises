def longest(sequence):
    longest = 0
    longest_pairs = {}
    last_seen_pair = {}
    if len(sequence) < 4:
        return longest_pairs
    pair = sequence[0:2]
    last_seen_pair[pair] = 0
    for i, c in enumerate(sequence[2:]):
        pair = pair[1:] + c
        if pair in last_seen_pair:
            if 2 + i <= last_seen_pair[pair] + 1:
                continue
            length = 2 + i - last_seen_pair[pair] - 3
            if length == longest:
                longest_pairs[pair] = length
            elif length > longest:
                longest_pairs = {pair: length}
                longest = length
        last_seen_pair[pair] = i
    return longest_pairs

def main():
    assert(longest('aabcdaa') == {'aa': 3})
    assert(longest('abbcdab') == {'ab': 3})
    assert(longest('bbb') == {})
    assert(longest('bbbb') == {'bb': 0})
    assert(longest('cbbbbd') == {'bb': 0})
    assert(longest('cbbbd') == {'bb': 0})
    assert(longest('cbbbasgbbd') == {'bb': 4}) # or 3?

if __name__ == '__main__':
    main()
