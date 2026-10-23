def dfa(string):
    state = 0
    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                return False
        elif state == 1:
            if ch == 'b':
                state = 1
            else:
                return False
    return state == 1
tests = ["a", "ab", "abb", "abbb"]
for s in tests:
    if dfa(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")