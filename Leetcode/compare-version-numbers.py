def compareVersion(version1, version2):
    version1 = version1.split('.')
    version2 = version2.split('.')
    for i in range(min(len(version1), len(version2))):
        if int(version1[i]) > int(version2[i]):
            return 1
        elif int(version1[i]) < int(version2[i]):
            return -1
    if len(version1) == len(version2):
        return 0
    elif len(version1) > len(version2) and sum([int(each) for each in version1]) > sum([int(each) for each in version2]):
        return 1
    elif len(version1) < len(version2) and sum([int(each) for each in version2]) > sum([int(each) for each in version1]):
        return -1
    else:
        return 0

version1 = "1"
version2 = "1.1"
print(compareVersion(version1, version2))