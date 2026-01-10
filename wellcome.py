import json


def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    print("Hello", config.get("Name"))
    input("Press enter to continue...")


# small comment dont have time today
if __name__ == "__main__":
    main()
