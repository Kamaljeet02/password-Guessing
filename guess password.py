from itertools import count


passcode=input("pass")
count=int(input('how many chances:'))
for i in range(count):
    guess =input("guess the password")
    print("correct")if guess==passcode else print("incorrect") 
