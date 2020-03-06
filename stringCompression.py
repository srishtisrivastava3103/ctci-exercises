#String Compression: Implement a method to perform basic string compression using the counts
#of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
#"compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
s=input()
r=""
c=1
for i in range(0,len(s)):
    if i+1<len(s) and s[i+1]==s[i]:
        c+=1
    if i+1<len(s) and (not(s[i+1]==s[i])):
        print(s[i])
        c=1
r=r+s[i]+str(c)
if(len(r)<len(s)):
    print(r)
else:
    print(s)
