#Adding to git
#1/Enter dir)             cd "/f/Pycharm/pycharm projects/OOP TRANING/git"
#2/int the folder )       git init
#3/add the pythone file ) git add 1.py
#4/do the first commit to local ) git commit -m "First commit"
#5/git branch -M master
#6/add it to git hub repesitory )
#7/$ git remote set-url origin https://github.com/AleksandarDochev/OOP-TRANING.git
#8/$ git pull
#9/Push the changes in your local repository to GitHub.) git push origin master

 #TUTORIAL that I used https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
###########################################################################
class Employee:
#here def __init__(self): we star building the Mehod so we can properly use the
#advantages of the class  ANd this how it lookks It creats it automaticly when we add the object Employee
     def __init__(self, first, last , pay): #This is a METHOD /CONSTRUCTOR for universal ,
              self.first  = first                            # Whe have self so it has it sticks to its name
              self.last = last                               # and we set the arguments we want in the small brackets like
              self.pay = pay
              self.email = first + '.' + last + '@company.com'


emp_1 = Employee('Corey', 'Schafer', 50000)  #we create the object and we pass in the same information but IN the correct order
emp_2 = Employee('Test', 'User', 60000)



#this is just a manual example of entering data that is unreliable and slow
emp_1 = Employee()
emp_1.first = 'Corey'  #This is instance variable
emp_1.last = 'Shafer'   #This is instance variable
emp_1.email = 'Corey.Shafer@company.com'       #This is instance variable
emp_1.pay  = 50000

emp_2 = Employee()
emp_2.first = 'Test'  #This is instance variable
emp_2.last = 'User'   #This is instance variable but set manualy
emp_2.email = 'test.user@company.com'       #This is instance variable
emp_2.pay  = 60000

print(emp_1.email)
print(emp_2.email)

