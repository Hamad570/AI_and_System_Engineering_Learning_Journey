
choice=input('IF you have an account type: login\nBut if you dont have account type: Signup\nEnter your choice here: ')
if choice=="login":
    username=input("Enter a user name: ")
    pin=input("Enter 8 digits password including a small,upper,special and numbers: ")
    login=False
    try:
       file=open("Example.txt","r")
       r=file.readlines()
       for line in r:
            h1 = line.strip().split(",")
            h=username+pin
            for i in h1:
                if i == h:  
                    print("ok_200") 
                    login=True
            if login==False:
                print("UserName or Password is Invalid")
            else:
                print("Login Successful!")
    except:
        print("UserName or Password is Invalid")
    finally:
        if login==False:
                print("Try Again!")
        else:
                print("System is loading.")
    

elif choice== "Signup":
    file=open("Example.txt","a")
    try:
       username=input("Enter a valid UserName: ")
       pin=input("Enter 8 digits password including a small,upper,special and numbers: ")
       if len(pin)>=8:
           a=username+pin
           try:
               file2=open("Example.txt","r")
               file2=file2.readlines()
               for i in file2:
                  if a==i:
                      print("User already exist!")
                      break
                  pass
           except:
              file.write("\n")
              file.write(a)
           
    except:
        print("NotValid UserName or Password")
    finally:
        print("Login Again! please")
        file.close()
else:
    print("Invalid Choice!")
