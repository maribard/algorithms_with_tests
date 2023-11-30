def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)

    for i in range(len(head)):
        permutations(head[:i] + head[i+1:], tail + head[i])


permutations("abc")


