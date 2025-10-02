# Matthew Howard
running_times = []   

# 1. Exit
def exit_program():
    print("Good-Bye!")

# 2. Add a time
def add_time():
    running_time = int(input("Enter the running time in seconds: "))
    running_times.append(running_time)
    print("Time added.")

# 3. Show all the times
def list_times():
    if len(running_times) == 0:
        print("No times recorded yet.")
    else:
        print("Running times are:")
        for t in running_times:
            print(t)

# 4. Show the best 3 times
def best_times():
    if len(running_times) == 0:
        print("No times recorded yet.")
    else:
        sorted_list = sorted(running_times)
        print("Your best times are:")
        count = 0
        for t in sorted_list:
            if count < 3:   
                print(t)
                count = count + 1

# 5. Show the worst 3 times
def worst_times():
    if len(running_times) == 0:
        print("No times recorded yet.")
    else:
        sorted_list = sorted(running_times, reverse=True)
        print("Your longest times are:")
        count = 0
        for t in sorted_list:
            if count < 3:   
                print(t)
                count = count + 1

# 6. Delete a time
def delete_time():
    value = int(input("Enter the time to delete: "))
    if value in running_times:
        running_times.remove(value)
        print("Time deleted.")
    else:
        print("That time was not found.")

# 7. Sort and show all the times
def sort_times():
    if len(running_times) == 0:
        print("No times recorded yet.")
    else:
        sorted_list = sorted(running_times)
        print("Running times sorted from shortest to longest:")
        for t in sorted_list:
            print(t)

# 8. Unknown choice
def unknown_choice(choice):
    print("Sorry, but", choice, "isn't a valid choice.")

# Main program loop
def main():
    choice = ""
    while choice != "0":
        print("\nMenu:")
        print("0 - Exit")
        print("1 - Add a Time")
        print("2 - Show Times")
        print("3 - Show the Best 3 Times")
        print("4 - Show the Worst 3 Times")
        print("5 - Delete a Time")
        print("6 - Sort Times")
        
        choice = input("Enter your choice: ")
#  Main ---
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_time()
        elif choice == "2":
            list_times()
        elif choice == "3":
            best_times()
        elif choice == "4":
            worst_times()
        elif choice == "5":
            delete_time()
        elif choice == "6":
            sort_times()
        else:
            unknown_choice(choice)

main()