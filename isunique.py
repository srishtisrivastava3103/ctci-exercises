#Cracking the Coding Interview
#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures? 
#Using hash table( taking ASCII characterset)

s=input()
if(len(s)>128):
    print("Not Unique")
val=[0]*128
i=0
while(i<len(s)):
    if(val[ord(s[i])]==1):
        break
    else:
        val[ord(s[i])]=1
    i+=1
if i<len(s):
    print("Not Unique")
else:
    print("Unique")
        
    
