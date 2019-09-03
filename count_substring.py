def count_substring(string, substring):
    st = string.find(substring)
    c = 0
    while st != -1:
        st = string.find(substring, st + 1)
        c += 1
    return c


h = 'ABCDCDCDC'
k = 'CDC'
print(count_substring(h, k))
