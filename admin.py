from person import Person

class Admin(Person):
    def __init__(self) -> None:
        super().__init__()
        
    def AddingEmployee(self,name,password,salary):
        super().RegisterUser(name,password,salary)
        

    def UpdatingEmployee(self,file_path, empUserId, new_content):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        found = False
        for line in lines:
            empInfo = line.strip().split('|')
            if line == "\n":
                continue
            else:
                if "\n" not in line:
                    line = line + "\n"
                
            if len(empInfo) > 0 and empInfo[0] == empUserId:
                found = True
            elif len(empInfo) > 0:
                modified_lines.append(line)
        if found == True:
            modified_lines.append(new_content)
            
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)
            
    def DeletingEmployee(self,file_path, empUserId):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        found = False
        for line in lines:
            empInfo = line.strip().split('|')
            if line == "\n":
                continue
            else:
                if "\n" not in line:
                    line = line + "\n"
                
            if len(empInfo) > 0 and empInfo[0] == empUserId:
                found = True
            elif len(empInfo) > 0:
                modified_lines.append(line)
                
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

        if found == True:
            return True
        return False            
        
        
        
            

        


        