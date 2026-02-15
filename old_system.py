n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0. # Bug 1: Infinite Loop. "Loading" was never incremented
    while loading < 5:
        print("Loading module " + str(loading))
        loading += 1 #Added increment to break loop
        
    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        if opt == "1":  # Bug 2: Syntax Error. "=" is for assignment, "==" is for comparison
            print("Current Crew List:")
            
            for i in range(len(n)): # Bug 3: Runtime Error. Range was harcoded to 10, but n only has 4 items
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name) # Bug 4: Logic Error. Parallel list desync. Only name was appended, causing errors in other lists
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
        
        if rem in n: # Bug 5: Runtime Error. Index() crashes if the name is not found
            idx = n.index(rem)
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                if rank == "Captain" or  rank == "Commander": # Bug 6: Logical Error. Rank == "Captain" or "Commander" evaluates to True
                    count = count + 1
            print("High ranking officers: " + str(count)) # Bug 7: Type Error. The + cannot be used to join a string and an integer directly
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

run_system_monolith
