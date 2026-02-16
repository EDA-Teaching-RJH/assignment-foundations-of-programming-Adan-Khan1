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