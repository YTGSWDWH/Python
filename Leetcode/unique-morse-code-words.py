def uniqueMorseRepresentations(words):
    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    list2 = []
    for word in words:
        str1 = ''
        for each in word:
            str1 = str1 + table(ord(each)-96)
        list2.append(str1)
    print(list2)
