def licenseKeyFormatting(s, k):
    s = s.split('-')
    s = "".join(s)
    print(s)
    list1 = []
    remainder = len(s) % k
    groups = len(s) // k
    if remainder == 0:
        for i in range(len(s)):
            if i > 0 and i % k == 0:
                list1.append('-')
                list1.append(s[i].upper())
            else:
                list1.append(s[i].upper())
    else:
        for i in range(len(s)):
            if i == remainder:
                list1.append('-')
                list1.append(s[i].upper())
            elif i > remainder and (i - remainder) % k == 0:
                list1.append('-')
                list1.append(s[i].upper())
            else:
                list1.append(s[i].upper())

    return "".join(list1)

s = "2-5g-3-J"
print(licenseKeyFormatting(s, 2))