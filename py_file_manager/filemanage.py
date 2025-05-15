import os

# now = os.getcwd()


# def reading():
#     val = input("Enter the file name to read : ")
#     file = open(f"{val}",'r')
#     values = file.read()
#     print(values)


# def create():
#     name = input("Enter a file name : ")
#     file_type = input("Enter file type extention : ")
#     with open(f'{name}.{file_type}','w') as newfile:
#         newfile.write('')
#     return f"file created as {name}.{file_type} at location {now} "


# def writeingonfile():
#     file = input("Enter the file name to write : ")
#     content = input(f"enter the content to write in {file} : ")
#     with open(f"{file}",'a') as writeonfile:
#         writeonfile.write(content + '\n')

import os
while True:
    x = input("enter the command : ")
    print(x)

    val = x.split()

    if not val:
        print("No command entered.")
    else:
        command = val[0]

        if command == 'touch':
            if len(val) >= 2:
                filename = val[1]
                content_str = ' '.join(val[2:]) if len(val) > 2 else ''
                def creatingfile(name, content):
                    with open(name, 'w') as f:
                        f.write(content)
                creatingfile(filename, content_str)
                print("done")
            else:
                print("Filename not provided for touch command.")

        elif command == 'ls':
            print("Current directory:", os.getcwd())
            print("Contents:")
            new_item = []
            for item in os.listdir():
                if os.path.isfile(item):
                    new_item.append(item)
                else:
                    new_item.append(item + "/")
            for i in new_item:
                print(i)  # Print each item on a new line
            print()  # Extra newline for spacing

        elif command == 'cd':
            directory = input("Enter the directory : ")
            base_path = r"C:\Users\Minfy.DESKTOP-3E50D5N"
            new_dir = os.path.join(base_path, directory)
            os.chdir(new_dir) 
            print("changed the directory : ", os.getcwd())
              # Extra newline for spacing

        else:
            print("not done")
