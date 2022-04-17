def maxConsecutiveAnswers(answerKey, k):
    def lianxucount(s):
        maxnum = 1
        num = 1
        result = []
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                num+=1
                if maxnum < num:
                    maxnum = num
            else:
                num = 1
        return maxnum

    len1 = len(answerKey)
    start = 0
    ans = 1
    for i in range(answerKey.count('F')):
        answerKey_copy = "".join(each for each in answerKey)
        answerKey_exam = "".join(each for each in answerKey)
        for index in range(k):
            start = answerKey_exam.index('F')
            for m in range(start,len1):
                if answerKey_exam[m] == 'F':
                    answerKey_exam = answerKey_exam[:m] + 'T' + answerKey_exam[m+1:]
                    break
            for j in range(start,len1):
                if answerKey_copy[j] == 'F':
                    answerKey_copy = answerKey_copy[:j] + 'T' + answerKey_copy[j+1:]
                    start += 1
                    break
        print(start,answerKey_copy, lianxucount(answerKey_copy))
        ans = max(ans,lianxucount(answerKey_copy))
        
        
    start = 0

    for i in range(answerKey.count('T')):
        answerKey_copy = "".join(each for each in answerKey)
        answerKey_exam = "".join(each for each in answerKey)
        for index in range(k):
            start = answerKey_exam.index('T')
            for m in range(start,len1):
                if answerKey_exam[m] == 'T':
                    answerKey_exam = answerKey_exam[:m] + 'F' + answerKey_exam[m+1:]
            for j in range(start,len1):
                if answerKey_copy[j] == 'T':
                    answerKey_copy = answerKey_copy[:j] + 'F' + answerKey_copy[j+1:]
                    start += 1
                    break

        print(start,answerKey_copy, lianxucount(answerKey_copy))
        ans = max(ans,lianxucount(answerKey_copy))
    return ans

answerKey = "FFFTTFTTFT"
k = 3
print(maxConsecutiveAnswers(answerKey, k))