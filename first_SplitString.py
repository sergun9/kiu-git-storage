def solution(s):
    step = 2
    if len(s) % 2 == 1:
        s = s + '_'
    return [s[letter]+s[letter+1] for letter in range(0, len(s)-1, step)]
