#write a python program to display a user entered name following by Good afternoon using input()function.


'''name=input("Enter  YOur name = ")
print(f"Good afternoon  {name}")'''


#Write a program to fill in a letter template gives below with name and date.

#
name=str(input("Enter the your Name = "))
Gender=str(input("Enter the your Answers = "))
letter='''  Hello , </name/>
            You are a male or Female ?
            
           No i m  </Gender/> 
   Ok Than You are going to market'''

print(letter.replace ("</name/>",name).replace("</Gender/>",Gender))


