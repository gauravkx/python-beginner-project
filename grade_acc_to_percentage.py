# GRADING ACC  TO PERCENTAGE

'''if percentage>= 81 then "very good"
                 >= 61 good
                 >= 41 average
                 >= fail'''


percentage = float(input("enter the percentage of student"))
if percentage>=81:
    print("VERY GOOD")
elif percentage>=61:
    print("GOOD")
elif percentage >=41:
    print("AVERAGE")
else:
    print('FAIL')

print("You can do better")