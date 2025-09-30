import time
# Matthew Howard
def countdown():
    """Counts down from 10"""
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

def main():
    """Grabs User input and reacts accordingly"""
    while True:
        user_input = input('Enter "go" to start the timer (stop to end): ').strip().lower()

        if user_input == "go":
            countdown()
        elif user_input == "stop":
            print("stopping timer.")
            break
        else:
            # edge cases
            print("Invalid input, please enter 'go' or 'stop'.")
main()