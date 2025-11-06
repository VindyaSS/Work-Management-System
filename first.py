

print("+--------------------------To Do List-------------------------------------------+")

print("|                      1. Add list                                              |")
print("|                      2. View List                                             |")
print("|                      3. Remove list                                           |")
print("|                      4. Exit                                                         |")

print("+-------------------------------------------------------------------------------+")

tasks = []

while True:
    x = int(input("enter the number what do you want:"))
    if x==1:
        while True:
            task =input("adding tasks:")
            tasks.append(task)
            y = input("Do u want to add another task? yes/no:")
            if y!='yes':
                break
         
    if x==2:
        for z in range(len(tasks)):
            print(z+1,tasks[z])

    if x==3:
        z = int(input("Enter the task number to remove: "))
        if 1<= z <=len(tasks):        
            tasks.pop(z-1)

    if x==4:
        print("Goodbye! 👋")
        break
        
        
            


