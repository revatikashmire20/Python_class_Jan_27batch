##class Netzwerk:
##    def __init__(abhi,name):
##
##        abhi.name = name
##
##    def fun(abhi):
##        print(abhi.name,"one")
##    def fun(abhi):
##        print(abhi.name,"two")
##
##    n_obj = Netzwerk("kohli")
##    n_obj.fun()
##
##var = "a"
##var = "b"
##print(var)

#python dont support functionoverloading
#python has access specifier  public private
###private access specifier can also be called as "Data Hiding"
##
##class Netzwerk:
##    def __init__(abhi,name):
##
##        abhi.name = name
##
##    def fun(abhi):
##        print(abhi.name,"one")
##        
##    def __new(abhi):  #private access specifier which can also be called "data hiding"
##        print(abhi.name,"two")
##
##    n_obj = Netzwerk("kohli")
##    n_obj.fun()
##    n_obj.new()


##class Netzwerk:
##    def __init__(abhi,name):
##
##        abhi.name = name
##
##    def fun(abhi):
##        print(abhi.name,"one")
##        
##class Two(Netzwerk):   #single inheritance
##    def new(abhi):
##        print(abhi.name,"two")
##
##    n_obj = Netzwerk("kohli")
##    n_obj.fun()
##    n_obj.new()
##    

##class Netzwerk:
##    def __init__(abhi,name):
##
##        abhi,name = name
##    def fun(abhi):
##        print(abhi.name,"one")
##
##class Two(Netzwerk):    #single inheritance
##    def new(revati):
##            print(revati.name,"two")
##
##        n_obj = Two("kohli")
##        n_obj.fun()
##        n_obj.new()

##class Netzwerk:
##    def __init__(abhi,name,age):
##        abhi.name = name
##        abhi.age = age
##
##        def fun(abhi):
##            print(abhi.name,"one",abhi.age)
##
##class Two(Netzwerk):
##    def new(revati):
##        print(revati.name,"two")
##        
##n_obj = Two("kohli",33)
##n_obj.fun()
##n_obj.new()

class Netzwerk:
    def __init__(abhi,name,age):
        abhi.name = name
        abhi.age = age

        def fun(abhi):
            print(abhi.name,"one",abhi.age)

class Two(Netzwerk):
    def __init__(revati,name):
        revati.name=name
        Netzwerk.__init__(revati,revati.name,23)
    
    def new(revati):
        print(revati.name,"two")
n_obj = Two("kohli",23)
n_obj.fun()
n_obj.new()































