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


# FEATURE 7: search_crew()
def search_crew(names, ranks, divs, ids):
    search_term = input("Enter name or partial name to search: ").strip().lower()
    print(f"Results for '{search_term}':")

    found = False 

    for i in range(len(names)):
        if search_term in names[i].lower():
            print(f"[{ids[i]}] {names[i]} - {ranks[i]} ({divs[i]})")
            found = True
    
    if not found:
        print("No crew member found with that name.")


# FEATURE 8: filter_by_division()
def filter_by_division(names, divs):
    target_div = input("Filter by (Command/Operations/Sciences): ").strip().title()
    print(f"Crew in {target_div} Division:")

    for i in range(len(names)):

        match divs[i]:
            case _ if divs[i] == target_div:
                print(f"- {names[i]}")


# FEATURE 9: calculate_payroll()
def calculate_payroll(ranks):
    total_cost = 0
    for rank in ranks:
        if rank == "Captain":
            total_cost += 1000
        elif rank == "Commander":
            total_cost += 800
        elif rank == "Lt. Commander":
            total_cost += 600
        elif rank == "Lieutenant":
            total_cost += 400
        else:
            total_cost += 200
            
    return total_cost 

# FEATURE 10: count_officers()
def count_officers(ranks):
    officer_count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            officer_count += 1
    return officer_count

# MAIN SYSTEM ORCHESTRATOR

def main():
    n_list, r_list, d_list, i_list = init_database()
    current_user = input("Please enter your full name to log in: ").strip().title()

    while True:
        user_choice = display_menu(current_user)

        if user_choice == "1":
            display_roster(n_list, r_list, d_list, i_list)
        elif user_choice == "2":
            add_member(n_list, r_list, d_list, i_list)
        elif user_choice == "3":
            remove_member(n_list, r_list, d_list, i_list)
        elif user_choice == "4":
            update_rank(n_list, r_list, i_list)
        elif user_choice == "5":
            search_crew(n_list, r_list, d_list, i_list)
        elif user_choice == "6":
            filter_by_division(n_list, d_list)
        elif user_choice == "7":
            total = calculate_payroll(r_list)
            print(f"Total Fleet Payroll: {total} Credits")
        elif user_choice == "8":
            officers = count_officers(r_list)
            print(f"Total High Ranking Officers: {officers}")
        elif user_choice == "9":
            print("System Shutting Down. Live Long and Prosper.")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
