#Same problem as above using bit vector(Space efficient):
#Assumption- String contains only lowercase letters
s=input()
checker=0
val=0
i=0
while(i<len(s)):
    val=ord(s[i])-ord('a')
    if not((checker & 1<<val)==0):
        print ("Not Unique")
        break
    else:
        checker=checker|1<<val
    i+=1
if(i==len(s)):
    print("Unique")
