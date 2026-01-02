import json

def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    print("Hello", config.get("Name"))

if __name__ == "__main__":
   main()