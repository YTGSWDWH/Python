def wordPattern(pattern, s):
    word2ch = {}
    ch2word = {}
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    for ch, word in zip(pattern, words):
        if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
            return False
        word2ch[word] = ch
        ch2word[ch] = word
        print(word2ch)
    return True

pattern = "abba"
s = "dog dog cat dog"
print(wordPattern(pattern, s))