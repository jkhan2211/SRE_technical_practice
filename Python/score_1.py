def product(score):
    if score < 50:
        print("Fail")
    else:
        print("Pass")


# Keep asking for input until a valid score is entered
while True:
    score = int(input("Please enter a score between 1 to 100: "))
    
    # Check if the input is within the valid range
    if 1 <= score <= 100:
        product(score)
        break  # Exit the loop once a valid score is entered
    else:
        print("Invalid score! Please enter a score between 1 and 100.")
