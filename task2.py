enter_score = input("Enter Score: ")
try:
    score = int(enter_score)
    if 0 <= score <= 100:
        if score >= 90:
            print("Grade is A")
        elif score >= 80:
            print("Grade is B")
        elif score >= 70:
            print("Grade is C")
        elif score >= 60:
            print("Grade is D")
        else:
            print("Grade is F")
    else:
        print("Error, please enter numeric input between 0 and 100")
except ValueError:
    print("Error, please enter numeric input between 0 and 100")
