def encrypt_word(word):
    newword=''
    for char in word:
        if ord(char) >= ord('a') and ord(char) < ord('n'):
            ch=chr(ord('z')-(ord(char)-ord('a')))
        elif ord(char) > ord('m') and ord(char) <= ord('z'):
            ch = chr(ord('a')+(ord(char)-ord('m')))
        newword+=ch
    return newword

c = input()
print(encrypt_word(c))