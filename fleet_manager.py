# Feature 1: init_database()

def init_database(): 
    names = ["Jean-Luc Picard", "William Riker", "Data", "Geordi La Forge", "Beverly Crusher"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lt. Commander", "Commander"]
    divs = ["Command", "Command", "Operations", "Engineering", "Sciences"]
    ids = ["1701", "1702", "1703", "1704", "1705"]
    return names, ranks, divs, ids

# FEATURE 2: display_menu()

def display_menu(user_name):
    print(f"\n--- FLEET MANAGEMENT SYSTEM ---")
    print(f"Logged in as: {user_name}") 
    print("1. View Roster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count Officers")
    print("9. Exit")

    choice = input("Select an option: ")
    return choice

# FEATURE 3: add_member()

def add_member(names, ranks, divs, ids):
    new_id = input("Enter new Member ID: ").strip()

    if new_id in ids:
        print("Error: This ID is already assigned to another member.")
        return
    
    new_rank = input("Enter Rank (Captain/Commander/Lt. Commander/Lieutenant/Ensign): ").strip().title()

    valid_tng_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    if new_rank not in valid_tng_ranks:
        print("Error: Invalid TNG rank provided.")
        return

    new_name = input("Enter Full Name: ").strip().title()
    new_div = input("Enter Division (Command/Operations/Sciences): ").strip().title()

    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print(f"Successfully added {new_name} to the fleet.")

# FEATURE 4: remove_member()

def remove_member(names, ranks, divs, ids):
    target_id = input("Enter ID of the member to remove: ").strip()

    if target_id in ids:
        idx = ids.index(target_id)

        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print("Member records removed successfully.")
    else:
        print("Error: ID not found.")


# FEATURE 5: update_rank()

def update_rank(names, ranks, ids):
    target_id = input("Enter ID to update rank: ").strip()

    if target_id in ids:
        idx = ids.index(target_id) # Find indexs
        new_rank = input(f"Enter new rank for {names[idx]}: ").strip().title()
        ranks[idx] = new_rank # Update rank strings
        print("Rank updated.")
    else:
        print("Error: ID not found.")


# FEATURE 6: display_roster()
def display_roster(names, ranks, divs, ids):

    print(f"\n{'ID':<6} | {'Name':<20} | {'Rank':<15} | {'Division':<12}")
    print("-" * 60)

    for i in range(len(names)):
        print(f"{ids[i]:<6} | {names[i]:<20} | {ranks[i]:<15} | {divs[i]:<12}")

