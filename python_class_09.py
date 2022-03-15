##var = ["a","b","c"]
##for x in var:
##    var.append(x.upper())
##    print (var)

##var="abc"
##for x in var:
##    var=var+x.upper()
##    print(var)

var=["a","b","c","d","e","f"]
for x in var:
    if (x%2 == 0):
        var.remove(x)
        print(var)

##var=[4,3,5,3,"dhoni","ashwin","rahul"]
##var.sort()
##print(var)

##var=["cat","goat","umbrella","pig","tension"]
##var.sort()
##print(var)

var=["cat","goat","umbrella","pig","tension"]
output=sorted(var,key=len)   #length 
print(output)

