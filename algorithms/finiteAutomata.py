NO_OF_CHARS = 256


def next_state(pattern, M, state, x):
    if state < M and x == ord(pattern[state]):
        return state+1

    i = 0
    for ns in range(state, 0, -1):
        if ord(pattern[ns-1]) == x:
            while i < ns - 1:
                if pattern[i] != pattern[state-ns+1+i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0


def compute_tf(pattern, M):
    global NO_OF_CHARS

    TF = [[0 for i in range(NO_OF_CHARS)] for _ in range(M+1)]

    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = next_state(pattern, M, state, x)
            TF[state][x] = z

    return TF


def search(pattern, text):
    global NO_OF_CHARS
    M = len(pattern)
    N = len(text)
    TF = compute_tf(pattern, M)
    state = 0
    for i in range(N):
        state = TF[state][ord(text[i])]
        if state == M:
            print("Pattern found at index: " + str(i-M+1))


if __name__ == "__main__":
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    search(pattern, text)
