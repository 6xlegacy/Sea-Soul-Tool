import time
import sys
import random

def loading():
    print("Loading...\n")
    for i in range(0, 21):
        bar = "[" + "-" * i + " " * (20 - i) + "]"
        percent = i * 5
        sys.stdout.write(f"\r{bar} {percent}%")
        sys.stdout.flush()
        time.sleep(0.07)
    print("\n")

print("""
DISCLAIMER:

This tool is created for educational and demonstration purposes only.

The developer of this tool is NOT responsible for any misuse,
illegal activity, or damage caused by the use of this software.

By using this tool, you agree that you are fully responsible
for how you use it and for complying with all applicable laws.
""")

agree = input("Do you agree to these terms? (Y/N): ").lower()

if agree != "y":
    print("Exiting program.")
    sys.exit()

print("""
   _____                 _____             _
  / ____|               / ____|           | |
 | (___   ___  __ _ ___| (___   ___  _   _| |
  \\___ \\ / _ \\/ _` / __|\\___ \\ / _ \\| | | | |
  ____) |  __/ (_| \\__ \\____) | (_) | |_| | |
 |_____/ \\___|\\__,_|___/_____/ \\___/ \\__,_|_|
""")

print("Choose option:")
print("1 - spam followers(to rape people)")
print("2 - mass report")
print("3 - Exit")

choice = input("Option: ")

if choice == "1":
    loading()
    msg = input("Enter The amount : ")
    count = input("Enter the user : ")

    time.sleep(1)
    print("\nRoot Access Required!")
    input("Press Enter...")

elif choice == "2":
    loading()
    name = input("Enter username: ")
    num = int(input("Number of reports: "))

    print("\nInitializing report engine...\n")
    time.sleep(1)

    statuses = [
        "Connecting to server",
        "Authenticating session",
        "Preparing report payload",
        "Sending request"
    ]

    for i in range(1, num + 1):
        status = random.choice(statuses)
        print(f"[{i}] {status} -> target: {name}")
        time.sleep(10)
        print("    Report submitted\n")

    print("Process finished.")

elif choice == "3":
    print("Goodbye")

else:
    print("Invalid option")
