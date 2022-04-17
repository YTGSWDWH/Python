def uniqueMorseRepresentations(words):
    list1 = []
    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for word in words:
        str1 = ''
        for each in word:
            str1 = str1 + table[ord(each)-97]
        list1.append(str1)
    return len(set(list1))

words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))