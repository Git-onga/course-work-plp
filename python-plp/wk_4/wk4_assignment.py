# 1. File Read & Write Challenge 🖋️

# file = open('exmple.txt', 'w')
# file.write('Hello, World!')
# file.close()
with open('example.txt', 'w') as file:
    file.write('Hello, World!')


# 2. Error Handling Lab 🧪

name = input("Enter the filename: ")

try:
    with open(name, 'r') as file:
        content = file.read()
        print("\n📄 File content:\n")
        print(content)
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don't have permission to read this file.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
