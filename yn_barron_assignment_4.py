student_name = "Yahzir Barron" 
current_gpa = 4.0 
study_hours = 20
social_points = 50
stress_level = 101 
#displaying game welcome stats
print("Welcome to my college life.")
print("")
print(f"Current GPA: {current_gpa}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f" stress Level.. {stress_level}")
#TEST 1 cases
#Adding in part 2 commits..
print("Choose your recovery time:")
print("A)  8 hours")
print("B) 10 hours")
print("C)  4 hours")
choice = input("Enter choice: ")

if choice == "A":
    if current_gpa >= 3.5:
        stress_level = stress_level - 5

elif choice == "B":
    if current_gpa >= 3.0:
        study_hours = study_hours + 3


elif choice == "C":
    if stress_level >= 100: 
        print("YOU FAILED CLASS...")
    elif current_gpa >= 2.7:
        stress_level = stress_level + 5
else:
    print("invalid")

#Step 3: Study strategy Decisiom 
#Player chooses a recovery time and it correspondes to gpa output
#Also shows membership operators
#when player chooses recovery time it will lead to their gpa outcome to see if they will graduate.
Recvoery_options = []
