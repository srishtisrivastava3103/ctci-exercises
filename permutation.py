#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
s1=input()
s2=list(input())
if not(len(s1)==len(s2)):
    print(False)
else:
    for i in range(0,len(s1)):
        if(s1[i] not in s2):
            print(False)
            break
        s2.remove(s1[i])
    if(s2==[]):
        print(True)
