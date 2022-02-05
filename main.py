answer = 8
guest_count = 3
user_guest = 1
while user_guest < 4:
    user_input = int(input("Your guest:"))
    if user_input == answer:
        print("You are right")
        break
    else: print(f'You are wrong. Please try again! Note: You only have {guest_count - user_guest} guest left')
    user_guest += 1
else: print("Sorry, you only have 3 chances")