
with open(f'8.txt', 'r') as f:
    input = f.read().strip().split('\n')  # f.readlines()


def ws_intersect(word, s):  # len of word-set-intersection
    return len(set(word) & s)


def get_digit_encoding(encoded):
    enc = [set([]) for i in range(10)]  # holds the encoding for the 10 digits
    for n in encoded:
        if len(n) == 2:
            enc[1] = set(n)
        if len(n) == 3:
            enc[7] = set(n)
        if len(n) == 7:
            enc[8] = set(n)
        if len(n) == 4:
            enc[4] = set(n)

    for n in encoded:
        if len(n) == 5:
            if ws_intersect(n, enc[1]) == 2:
                enc[3] = set(n)
            elif ws_intersect(n, enc[4]) == 2:
                enc[2] = set(n)
            elif ws_intersect(n, enc[4]) == 3:
                enc[5] = set(n)

        if len(n) == 6:
            if ws_intersect(n, enc[1]) == 1:
                enc[6] = set(n)
            elif ws_intersect(n, enc[4]) == 4:
                enc[9] = set(n)
            elif ws_intersect(n, enc[4]) == 3:
                enc[0] = set(n)

    return enc


# solve
ans = 0
for l in input:
    encodings = l.split(" | ")[0].split(" ")
    output = l.split(" | ")[1].split(" ")
    # part 1:
    # for x in output:
    #     if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
    #         ans += 1
    # part 2:
    enc = get_digit_encoding(encodings)
    res = 0
    for x in output:
        res *= 10
        for i, s in enumerate(enc):
            if s == set(x):
                res += i
    ans += res


print(ans)
