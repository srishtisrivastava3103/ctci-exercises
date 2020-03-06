#String Rotation; Assume you have a method isSubs t rin g which checks if one word is a substring
#of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
#call to isSubs t rin g [e.g., "wate r bottle " is a rotation oP'erbottlewat"), 
def checkRotation(a,b):
    l=list(b)
    if not(len(a)==len(b)):
        return False
    for i in range(0,len(l)):
        if(a[0]==l[i]) and (l[(i+1)%len(l)]==a[1]):
            l=l[i:]+l[0:i]
    print(l)
        
checkRotation("waterbottle","erbottlewat")  
