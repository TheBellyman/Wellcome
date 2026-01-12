import json
import time

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    print("Hello", config.get("Name"))
    time.sleep(3)
    goals = config.get("My goals for this year")
    print("Your Goals for this year are:")
    time.sleep(2)
    for goal in goals:
        print(goal)
        time.sleep(2)
    time.sleep(3)
    input("Press Enter to continue...")


# small comment dont have time today
if __name__ == "__main__":
    main()
