import sys

# Check if exactly 2 arguments are passed (script name + 1 value)
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    name = sys.argv[1]
else:
    name = "Gadag"

# Check palindrome
if name == name[::-1]:
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")
