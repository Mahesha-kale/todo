from sys import argv
import datetime
l1 = []
l1 = argv
if len(l1) == 1  or l1[1] == "help":
    print('''Usage :-
     ./todo add "todo item"  # Add a new todo
     ./todo ls               # Show remaining todos
     ./todo del NUMBER       # Delete a todo
     ./todo done NUMBER      # Complete a todo
     ./todo help             # Show usage
     ./todo report           # Statistics''')
elif l1[1] == "ls":
    todo_file = open("todo.txt",'r+')
    lines = todo_file.readlines()
    count = len(lines)
    for line in lines :
        print(f"[{count}] {line.strip()}")
        count -= 1
    todo_file.close()
elif l1[1] == "add":
    print(f"Added todo: \"{l1[2]}\"")
    line = l1[2]
    with open("todo.txt", 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
elif l1[1] == "done":
    try:
        todo_file = open("todo.txt",'r')
        done_file = open("done.txt",'a')
        x = datetime.datetime.now()
        date = str(x)
        xv = date.split(" ")
        v = xv[0]
        lines = todo_file.readlines()
        todo_file.close()
        if len(lines)-int(l1[2]) >= 0:
            line1 = "x "+v+" "+lines[len(lines)-int(l1[2])]
            with open("done.txt", 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                f.write(line1.rstrip('\r\n') + '\n' + content)
            lines.pop(len(lines)-int(l1[2]))
            todo_file = open("todo.txt",'w')
            for line in lines:
                todo_file.write(line)
            todo_file.close()
            print(f"Marked todo #{int(l1[2])} as done.")
        else:
            print(f"Error: todo #{int(l1[2])} does not exist.")
    except:
        print(f"Error: todo #{int(l1[2])} does not exist.")
elif l1[1] == "del":
    try:
        todo_file = open("todo.txt",'r')
        lines = todo_file.readlines()
        if len(lines)-int(l1[2]) >= 0:
            print(f"Deleted todo #{int(l1[2])}")
            lines.pop(len(lines)-int(l1[2]))
            todo_file.close()
            todo_file = open("todo.txt",'w')
            for line in lines:
                todo_file.write(line)
            todo_file.close()
        else:
            print(f"Error: todo #{int(l1[2])} does not exist. Nothing deleted.")
    except:
        print(f"Error: todo #{int(l1[2])} does not exist. Nothing deleted.")
elif l1[1] == "report":
    todo_file = open("todo.txt",'r')
    done_file = open("done.txt",'r')
    lines_todo = todo_file.readlines()
    lines_done = done_file.readlines()
    x = datetime.datetime.now()
    date = str(x)
    xv = date.split(" ")
    v = xv[0]
    print(f"{v} pending : {len(lines_todo)} completed : {len(lines_done)}")
    todo_file.close()
    done_file.close()
