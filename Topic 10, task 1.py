pets = {
    "Rex": {
        "Species": "Dog",
        "Age": 5,
        "Owner": "John"
    },
    "Whiskers": {
        "Species": "Cat",
        "Age": 3,
        "Owner": "Emily"
    }
}

for name, info in pets.items():
    age = info["Age"]
    if age % 10 == 1 and age != 11:
        age_str = f"{age} year"
    elif 2 <= age % 10 <= 4 and not 12 <= age <= 14:
        age_str = f"{age} years"
    else:
        age_str = f"{age} years"
    
    print(f'This is a {info["Species"]} named "{name}". Age: {age_str}. Owner: {info["Owner"]}')