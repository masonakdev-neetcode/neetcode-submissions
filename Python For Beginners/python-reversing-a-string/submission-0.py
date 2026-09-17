def reverse_string(input_string: str) -> str:
    reversed_string = ""
    
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    
    return reversed_string

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
