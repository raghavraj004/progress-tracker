
print("""what do you want to do?

1) show progress of all tasks
2) create task
3) update progress to a task \n""")
answer = int(input("answer : "))

if answer == 1:
    file = open("data.txt","r")
    lines = file.readlines()
    for i in range(len(lines)):
        if (len(lines)/2)<(2*i):
            break
        task=int(lines[2*i])
        progress = int(lines[2*i+1])
        count = int((progress/task)*100)
        anticount = 100-count
        print(f"task {i}")
        print(f"["+"#"*count+" "*anticount+"]")
    if len(lines) == 0:
        print("no task in progress")
    file.close()
elif answer == 2:
    file = open("data.txt","a")
    task = input("how many task do you have :")
    progress = input("enter how many you have completed : ")
    file.write(f"\n{task}\n{progress}")
    count = int((int(progress)/int(task))*100)
    anticount = 100-count
    print(f"["+"#"*count+" "*anticount+"]")
    file.close()
elif answer == 3:
    num = int(input("""
enter task number to update on its progress (0,1,2...) :"""))
    print(f"selected task = {num}\n\n")
    file = open("data.txt","r")
    lines = file.readlines()
    list = lines
    print("""1) wanna add 1 to the progress
2) add custom\n""")
    ans = int(input("answer : "))
    if ans == 1:
        list[2*num +1] = int(list[2*num +1]) + 1
    elif ans == 2 :
        custom_num = int(input("enter the custom progress here : "))
        list[2*num+1] = int(list[2*num +1]) + custom_num
    list = lines
    file.close()
    file = open("data.txt","w")
    file.writelines(str(x) for x in lines)
    file.close()
else:
    print("error")

