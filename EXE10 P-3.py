def countvowel(n):
    count=0
    vowels="aeiou"
    for i in n:
        if i in vowels:
              count+=1
    return count
a=input()
print(countvowel(a))

