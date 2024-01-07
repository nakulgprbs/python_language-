# grading system 

marks = int(input("enter marks out of 100: ")) # taking only for one subject it can be for all subjects 
if marks > 100:
    print("you enter wrong marks please check it once.")
elif marks >= 80:
    print("you got A grade.")
elif marks >=60:
    print("you got B grade.")
elif marks >= 40:
    print("you got C grade.")
elif marks >= 30:
    print("you got D grade.")
else:
    print("sorry, you are fail.")
