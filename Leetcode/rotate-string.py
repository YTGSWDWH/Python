def rotateString(s, goal):
    for i in range(len(s)):
        s = s[1:] + s[0]
        print(s)
        if s == goal:
            return True
    return False

s = 'abcde'
goal = 'cdeab'
print(rotateString(s, goal))