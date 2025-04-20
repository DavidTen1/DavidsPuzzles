def move_zeroes_to_end(n):
    num_str = str(n)
    non_zeroes = ''.join(c for c in num_str if c != '0')
    zeroes = ''.join(c for c in num_str if c == '0')
    return non_zeroes + zeroes

print(move_zeroes_to_end(20020000))
