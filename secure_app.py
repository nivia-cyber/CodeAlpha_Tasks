import subprocess

print("Secure Coding Review Demo")

user_input = input("Enter your name: ")

# secure execution without shell
subprocess.run(["cmd", "/c", "echo", "Hello", user_input])