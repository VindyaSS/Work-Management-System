

print("+--------------------------To Do List-------------------------------------------+")

print("|                      1. Add list                                              |")
print("|                      2. View List                                             |")
print("|                      3. Remove list                                           |")

print("+-------------------------------------------------------------------------------+")

task = []

while True:
    x = int(input("enter the number what do you want:"))
    if x==1:
        while True:
            task =input("adding tasks:")
            y = input("Do u want to add another task? yes/no:")
            if y=='no':
                break
    break      
    


