##file_obj = open("reva.txt","w")
##file_obj.write("hello")
##file_obj.close()

##file_obj = open(r"C:\Users\WIN 10\Desktop\Python_Netzwerk\reva.txt","w")
##file_obj.write("hello")
##file_obj.close()

##import tkinter #gui, forms,frames buttons labels
##from tkinter import filedialog
##import os

##root = tkinter.Tk()
##root.withdraw
##
##folder = filedialog.askdirectory()
##print(folder)
##
##file = os.path.join(folder,"reva.txt")
##
##
##
##file_obj = open(file,"a")
##file_obj.write("\n")
##file_obj.write(lahhbhjsbhjbh)
##file_obj.close()


#context manager

##with open("netzwerk.txt","w") as file_obj:
##    file_obj.write("this is")

##with open("netzwerk.txt","r") as file_obj:
##    file_content = file_obj.read()
##    print(file_content)

##with open("netzwerk.txt","r") as file_obj:
##    file_content = file_obj.read(5)
##    print(file_content)
##    file_content1 = file_obj.read()
##    print(file_content1)

##with open("netzwerk.txt","r") as file_obj:
##    file_content = file_obj.readline(5)
##    print(file_content)
##    file_content1 = file_obj.readline()
##    print(file_content1)

with open("netzwerk.txt","r") as file_obj:
    file_content = file_obj.read(5)
    print(file_content)
    



