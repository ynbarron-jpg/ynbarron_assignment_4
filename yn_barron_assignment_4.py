student_name = "Yahzir Barron"
current_gpa = 4.0
study_hours = 20
social_points = 50
stress_level = 100
# displaying game welcome stats
print("Welcome to my college life.")
print("")
print(f"Current GPA: {current_gpa}")
print(f"Study hours: {study_hours}")
print(f"Social points: {social_points}")
print(f" stress Level.. {stress_level}")

print("Choose your recovery time:")
print("A)  8hours")
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
    if current_gpa >= 2.7:
        stress_level = stress_level - social_points
else:
    print("YOU FAILED CLASS...")