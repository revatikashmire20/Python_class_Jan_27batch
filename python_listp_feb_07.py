##var = []
##print(type(var))

##var = ["dhoni",55,44.5,"ab",["a","b"]]   #class list
##print(type(var))      
##
##print(var[3])   #it will print index of 3 i.e. "ab"

##var=["a","b","c"]
##var[1]="d"
##print(var)

##var=["a","b","c"]     #python dictionary
##print(dir(var))

##var=["a","b"]
##var1=["c","d"]
##print(var + var1)

##a=["dhoni","kohli","ashwin"]
##b=a            #shallow copy
##print(a)    
##print(b)
##
##b[0]="rohit"
##print(a)
##print(b)

##a=["dhoni","kohli","ashwin"]
##b=a[:]            #deeep copy
##print(a)    
##print(b)
##
##b[0]="rohit"
##print(a)
##print(b)

##var=["a","b","c"]
##var[0]="dhoni"
##print(var)

##var=["a","b","c"]
##var.insert(0,"dhoni")
##print(var)

##var=["a","b","c"]
##var.append("dhoni")  #append means to add the data in the last
##print(var)

##var=["a","b","c"]
##var.append("dhomi","kohli")   #it gives error
##print(var)

##var=["a","b","c"]
##var.extend(["dhoni","kohli"])
##print(var)

##var=["a","b","c"]
##var.extend(("dhoni","kohli"))
##print(var)

##var=["dhoni","and","cat","apple",2,4,6,5,"gaoat"]
##var.sort()
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##var.sort()
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##var.sort(reverse = True)
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##output=sorted(var,reverse=True)
##print(output)

##var=["dhoni","and","cat","apple","goat"]
##output=sorted(var,key=len)
##print(output)

##var=["dhoni","and","cat","apple","goat"]
##var.pop()
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##var.pop(2)
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##var.remove("apple")
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##var.clear()
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##del var
##print(var)

##var=["dhoni","and","cat","apple","goat"]
##del var[4]
##print(var)
##
##var=["dhoni","and","cat","apple","goat"]
##del var[14]
##print(var)
##

var=("dhoni",)
print(type(var))

















































