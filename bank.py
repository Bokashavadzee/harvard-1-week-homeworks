def main():
    name = get_input()
    print(greeting(name))

def get_input():
    name = input("Greeting: ")
    return name

def greeting(name):
    if name == "hello" or name == "Hello":
        return "0$"
    elif "Hello" or "hello" in name:
        return "0$"
    elif "h" in name  and name != "hello":
        return "20$"
    else:
        return "100$"

main()