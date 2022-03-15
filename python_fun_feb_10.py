##def fun(var,country):
##    if isinstance(var,str):
##        if isinstance(country,str):
##            print("hello",var,"from",country)
##            print("welcome to hdfc")
##fun("dhoni","india")
##fun("kohli","austrillia")
##fun("ashwin",2)

##def fun(var,country):
##    if isinstance(var,str) and isinstance(country,str):
##            print("hello",var,"from",country)
##            print("welcome to hdfc")
##fun("dhoni","india")
##fun("kohli","austrillia")
##fun("ashwin",2)

##def fun(var,country):
##    if isinstance(var,str) and isinstance(country,str):
##            print("hello",var,"from",country)
##            print("welcome to hdfc")
##fun(country = "india",var="dhoni")
##fun("kohli","austrilia")

##def fun(var,country = "india"):
##    if isinstance(var,str) and isinstance(country,str):
##            print("hello",var,"from",country)
##            print("welcome to hdfc")
##fun("dhoni",)
##fun("kohli","austrillia")

##def fun(var = "dhoni",country="india"):
##    if isinstance(var,str) and isinstance(country,str):
##            print("hello",var,"from",country)
##            print("welcome to hdfc")
##fun()
##fun("ashwin")
##fun("kohli","austrillia")

##def fun(var = "dhoni",country):
##    if isinstance(var,str) and isinstance(country,str):
##            print("hello",var,"from",country)
##            print("welcome to hdfc")
##fun()
##fun("ashwin")
##fun("kohli","austrillia")

##def Passed_Students(*name):  #*arguments
##    print(name)
##    print(type(name))

##    passed_Students("dhoni","kohli")

##def Passed_Students_Details(**var):       # **keyarguents
##    print(var)
##    print(type(var))
##
##    passesd_students_details(name="dhoni",age=44)
##    passesd_students_details(name="kohli",team="rcb")
##

def student_marks(name,eng,maths):
    total=eng+maths
    return total,name

print(student_marks("dhoni"))
























