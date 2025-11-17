def rabin_karp_search(pat, txt):
    R = 256
    Q = 2147483647  

    M = len(pat)
    N = len(txt)
    if M == 0:
        return 0
    if M > N:
        return N  

    h = pow(R, M - 1, Q)

    p = 0
    t = 0
    for i in range(M):
        p = (R * p + ord(pat[i])) % Q
        t = (R * t + ord(txt[i])) % Q

    for i in range(N - M + 1):
        if p == t:
            if txt[i:i+M] == pat:
                return i
        if i < N - M:
            t = (R * (t - ord(txt[i]) * h) + ord(txt[i + M])) % Q
            if t < 0:
                t += Q

    return N

s1 = 'ABCDCBDCBDAADFCBDABDCBADF'
s2 = 'ADF'

resposta = rabin_karp_search(s2, s1)

print(f"Primeira ocorrência: {resposta}")