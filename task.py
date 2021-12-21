
def parse(command):
  #Takes the command as input and returns the command name and args

  cmd_list = command.split()
  cmd_name = cmd_list[0]

  if(cmd_name=="add"):
    return cmd_list[0], cmd_list[1:]
  elif(cmd_name=="help"):
    return cmd_list[0],[]
  elif(cmd_name=="ls"):
    return cmd_list[0],[]
  elif(cmd_name=="delete"):
    return cmd_list[0], cmd_list[1:]
  elif(cmd_name=="done"):
    return cmd_list[0], cmd_list[1:]
  elif(cmd_name=="report"):
    return cmd_list[0],[]
  elif(cmd_name=="quit"):
    return cmd_list[0],[]
  else:
    return "invalid",[]
  
       
def main():
  print('Started the Task application...')
  
  while(1):
    # take the command as input from the user
    command = input('$ ')
    if(len(command.split())==0):
      print("invalid command")

    command_name, command_args = parse(command)
    # print(command_name, command_args)
    if (command_name == 'quit'):
      break
    elif (command_name == 'help'):
      with open('help.txt', 'r') as help_file:
        print(help_file.read())

    elif (command_name == 'add'):
      command_priority = command_args[0] 
      command_task = command_args[1:]   
      f=open('task.txt','a')
      f.close()
      with open('task.txt') as file:
        lines = file.readlines()
        task_dict={}
        for line in lines:
            each_line=line.split()
            task_dict[each_line[0]]=[each_line[1]]
        task_dict[command_priority]=[((str(command_task)).replace(","," "))]
        task_list=list()
        for i in task_dict:
            task_list.append(i)
        task_list.sort()
        sorted_task_dict={}
        for i in task_list:
            sorted_task_dict[i]=[task_dict.get(i)]
        with open('task.txt','w') as write_file:
            for i in sorted_task_dict:
                formated = ((str(sorted_task_dict.get(i)).replace("[","")).replace("]","")).replace("\'","")
                write_file.write(str(i)+" "+formated+"\n")
            

    
    elif (command_name == 'ls'):
        print("pending task")
        with open('task.txt','r') as read_file:
            lines=read_file.readlines()
            i=1
            for line in lines:
                one_line=line.split()
                print(str(i)+" "+one_line[1]+" "+one_line[0])
                i=i+1


    elif (command_name == 'delete'):
        with open('task.txt','r+') as read_file:
            lines=read_file.readlines()
            if(int(command_args[0])>=len(lines)):
                print("Error : Attempting to delete a non-existent item.")
        f=open('task.txt','w')
        f.close
        i=1
        for line in lines:
              
              with open('task.txt','a') as read_file:
                if(int(command_args[0])!=i):
                    one_line=line.split()
                    read_file.write(one_line[0]+" "+one_line[1]+"\n")
              i=i+1
        print("deleted item with index"+str(command_args))



    elif (command_name == 'done'):
         with open('task.txt','r+') as read_file:
            lines=read_file.readlines()
            if(int(command_args[0])>len(lines)):
                print("Errpr : Attempting to done a non-existent item.")
         i=1
         f=open('task.txt','w')
         f.close
         with open('completed.txt','a') as com_file:
          with open('task.txt','a') as read_file:
           for line in lines:
                one_line=line.split()
                if(int(command_args[0])!=i):
                    read_file.write(one_line[0]+" "+one_line[1]+"\n")
                
                elif(int(command_args[0])==i):
                        com_file.write(one_line[1]+"\n")
                i=i+1



    elif (command_name == 'report'):
        print("pending task:\n")
        with open('task.txt','r') as read_file:
            lines=read_file.readlines()
            i=1
            for line in lines:
                one_line=line.split()
                print(str(i)+" "+one_line[1]+" "+one_line[0]+"\n")
                i=i+1
        print("Completed task:\n")
        with open('completed.txt','r') as read_file:
            lines=read_file.readlines()  
            for line in lines:
                print(str(line)+"\n")
                
    elif (command_name == 'invalid'):
        print("invalid command")
        with open('help.txt','r') as read_file:
            lines=read_file.readlines()
            for line in lines:
                print(line)


if __name__ == '__main__':
  main()
