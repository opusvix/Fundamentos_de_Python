name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Welcome to our website {name.strip().title()}!")
else:
    print(f'You cannot access our website {name.strip().title()}.')
