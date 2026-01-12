file_name = input("Enter file name: ")
file = open(file_name,"xt")
file.write("This Is Simple Text File\n")
file.write("It Contains Multiple Lines")
file.close()
print(f"File '{file_name}.text' Created Successfully")

find_file = input("Enter Reading file name: ")
print("Reading File Contents..")
try:
    file = open(find_file,"r")
    print(file.read())
except FileNotFoundError:
    print(f"The File '{find_file}.text' Not Found")
finally:
    file.close()