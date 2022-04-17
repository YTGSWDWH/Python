import collections
def numUniqueEmails(emails):
    list1 = []
    list2 = []
    for each in emails:
        list1.append(each.split('@'))
    print(list1)
    for i in range(len(list1)):
        str1 = ''
        for each in list1[i][0]:
            if each.isalpha():
                str1 = str1 + each
            elif each == '+':
                # list2.append(str1+'@'+list1[i][1])
                break
        list2.append(str1+'@'+list1[i][1])
    print(list2)
    count = dict(collections.Counter(list2))
    print(count)
    ans = 0
    for _ in count.keys():
        ans += 1
    print(ans)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
numUniqueEmails(emails)