

print("+--------------------------To Do List-------------------------------------------+")

print("|                      1. Add list                                              |")
print("|                      2. View List                                             |")
print("|                      3. Remove list                                           |")

print("+-------------------------------------------------------------------------------+")

tasks = []

while True:
    x = int(input("enter the number what do you want:"))
    if x==1:
        while True:
            task =input("adding tasks:")
            tasks.append(task)
            y = input("Do u want to add another task? yes/no:")
            if y=='no':
                break
         
    if x==2:
        for i in range(len(tasks)):
            print(i+1,tasks[i])

    if x==3:
        z = input("what task do u want to remove?:")        



