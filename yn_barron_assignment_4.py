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
#Player chooses a recovery time and it correspondes to recovery options
#Also shows membership operators
#when player chooses recovery time it will lead to their gpa outcome to see if they will graduate.
recovery_options = ["Sleeping", "Working out", "Socializing", "Gaming"]
print("Step 3: Recovery Strategy Decision")
print(f"Available Recovery Options: {recovery_options}")
recovery_choice = input("Enter your recovery choice (e.g., Sleeping, Socializing): ")

if recovery_choice in recovery_options:
    print(f"\nValid choice: Taking time for {recovery_choice}.")

    if (stress_level >= 100) and (social_points < 40):
        print("Strategy: High stress and low social life! This recovery needs to be highly effective.")
        if recovery_choice == "Sleeping":
            stress_level -= 20
        elif recovery_choice == "Socializing":
            social_points += 15
        else:
            if recovery_choice not in ["Sleeping", "Socializing"]:
                stress_level += 5
        print(f"Updated Stress: {stress_level}, Updated Social Points: {social_points}")

    elif (current_gpa >= 3.8) or (study_hours > 25):
        print("Strategy: You're performing well. This recovery choice will enhance your balance.")
        if recovery_choice == "Working out":
            current_gpa += 0.05
        elif recovery_choice == "Gaming":
            if not (current_gpa < 3.0):
                study_hours -= 2

    else:
        print("Strategy: Moderate stats. This recovery choice provides steady benefits.")
        if recovery_choice == "Sleeping":
            stress_level -= 10
        elif recovery_choice == "Socializing":
            social_points += 5

elif recovery_choice not in recovery_options:
    print(f"\nInvalid choice: {recovery_choice} is not a valid recovery option. Please choose from the list.")

print("Current Stats After Decision 3")
print(f"Final GPA: {current_gpa}")
print(f"Final Study hours: {study_hours}")
print(f"Final Social points: {social_points}")
print(f"Final Stress Level: {stress_level}")

Cleaning = ["Bedroom, Kitchen, Bathroom"]
Cleaning_choice = input()
if Cleaning_choice in Cleaning:
    print(f"\nValid choice: Taking time for {Cleaning_choice}.")

    if (stress_level >= 100) and (social_points < 40):
        print("Strategy: High stress and low social life! This recovery needs to be highly effective.")
        if Cleaning_choice == "Sleeping":
            stress_level -= 20
        elif Cleaning_choice == "Socializing":
            social_points += 15
        else:
            if Cleaning_choice not in ["Sleeping", "Socializing"]:
                stress_level += 5
        print(f"Updated Stress: {stress_level}, Updated Social Points: {social_points}")

    elif (current_gpa >= 3.8) or (study_hours > 25):
        print("Strategy: You're performing well. This recovery choice will enhance your balance.")
        if Cleaning_choice == "Working out":
            current_gpa += 0.05
        elif Cleaning_choice == "Gaming":
            if not (current_gpa < 3.0):
                study_hours -= 2

    else:
        print("Strategy: Moderate stats. This recovery choice provides steady benefits.")
        if Cleaning_choice == "Sleeping":
            stress_level -= 10
        elif Cleaning_choice == "Socializing":
            social_points += 5

elif Cleaning_choice not in recovery_options:
    print(f"\nInvalid choice: {Cleaning} is not a valid recovery option. Please choose from the list.")

print("Current Stats After Decision 3")
print(f"Final GPA: {current_gpa}")
print(f"Final Study hours: {study_hours}")
print(f"Final Social points: {social_points}")
print(f"Final Stress Level: {stress_level}")