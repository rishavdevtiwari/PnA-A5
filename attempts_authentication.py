attempt=0
for i in range(1,4):
    uname=input("Enter the username : ")
    password=input("Enter the password : ")
    attempt+=1
    if uname == "admin" and password == "admin123":
        print("Welcome Admin")
    else:
        if attempt<3:
            print(f"Invalid username or password. Attempt left: {3 - attempt}")
        else:
            print("You have exceeded the maximum attempts. Account locked")
            
        
    
    