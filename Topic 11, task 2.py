import collections

# Initialize database
pets_db = {
    1: {
        "name": "Rex",
        "species": "Dog",
        "age": 5,
        "owner": "John"
    },
    2: {
        "name": "Whiskers",
        "species": "Cat",
        "age": 3,
        "owner": "Emily"
    }
}

def get_age_suffix(age):
    """Returns proper grammatical suffix for age"""
    if age % 10 == 1 and age % 100 != 11:
        return "year"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "years"
    else:
        return "years"

def display_pet(pet_id):
    """Shows information about a specific pet"""
    pet = pets_db.get(pet_id)
    if pet:
        print(f'This is a {pet["species"]} named "{pet["name"]}". '
              f'Age: {pet["age"]} {get_age_suffix(pet["age"])}. '
              f'Owner: {pet["owner"]}')
    else:
        print("Pet not found!")

def create_pet():
    """Adds a new pet to the database"""
    last_id = collections.deque(pets_db.keys(), maxlen=1)[0] if pets_db else 0
    new_id = last_id + 1
    
    pets_db[new_id] = {
        "name": input("Enter pet name: "),
        "species": input("Enter species: "),
        "age": int(input("Enter age: ")),
        "owner": input("Enter owner's name: ")
    }
    print(f"Successfully added pet with ID {new_id}")

def update_pet(pet_id):
    """Modifies an existing pet's record"""
    if pet_id in pets_db:
        pet = pets_db[pet_id]
        print(f"\nCurrent information for pet ID {pet_id}:")
        display_pet(pet_id)
        
        print("\nEnter new information (leave blank to keep current):")
        pet["name"] = input(f"Name [{pet['name']}]: ") or pet["name"]
        pet["species"] = input(f"Species [{pet['species']}]: ") or pet["species"]
        pet["age"] = int(input(f"Age [{pet['age']}]: ") or pet["age"])
        pet["owner"] = input(f"Owner [{pet['owner']}]: ") or pet["owner"]
        
        print("Record updated successfully!")
    else:
        print("Pet not found!")

def delete_pet(pet_id):
    """Removes a pet from the database"""
    if pet_id in pets_db:
        deleted_name = pets_db[pet_id]["name"]
        del pets_db[pet_id]
        print(f"Successfully deleted {deleted_name} (ID: {pet_id})")
    else:
        print("Pet not found!")

def list_all_pets():
    """Displays all pets in the database"""
    if not pets_db:
        print("No pets in database!")
        return
    
    print("\nAll Pets in Database:")
    for pet_id, pet in pets_db.items():
        print(f"ID: {pet_id} - {pet['name']} ({pet['species']}), "
              f"{pet['age']} {get_age_suffix(pet['age'])}, "
              f"owned by {pet['owner']}")

# Main application interface
def main():
    print("Veterinary Clinic Database System")
    print("--------------------------------")
    
    while True:
        print("\nOptions:")
        print("1. Add new pet")
        print("2. View pet details")
        print("3. Update pet information")
        print("4. Remove pet")
        print("5. List all pets")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            create_pet()
        elif choice == "2":
            pet_id = int(input("Enter pet ID: "))
            display_pet(pet_id)
        elif choice == "3":
            pet_id = int(input("Enter pet ID: "))
            update_pet(pet_id)
        elif choice == "4":
            pet_id = int(input("Enter pet ID: "))
            delete_pet(pet_id)
        elif choice == "5":
            list_all_pets()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()