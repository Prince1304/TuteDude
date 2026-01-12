file_name = input("Enter file name: ")
try:
    file = open(file_name,"rt")
    file.close()
except FileNotFoundError:
    print(f"The File '{file_name}.text' Not Found")
else:
    file = open(file_name,"wt")
    User_input = str(input("Enter A Text To Write To File: "))
    file.write(User_input)
    print(f"Data Sucessfully Written To {file_name}.text.")
    file.close()

    print("Write More..")
    input_more = str(input("Enter A Text To Write To File: "))
    file = open(file_name,"at")
    file.write(f"\n{input_more}")
    print(f"Data Sucessfully Appended To {file_name}.text.")
    file.close()
finally:
    file = open(file_name,"rt")
    line1 = file.readline().strip()
    line2 = file.readline()
    print(f"Final Content Of {file_name}.text.")
    print(f"{line1}\n{line2}")
    file.close()