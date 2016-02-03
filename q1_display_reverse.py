# q1_display_reverse.py
# display integer in reverse order

# get input
integer = input("Enter integers:")

while integer.isalpha():
    print("Invalid input!")
    integer = input("Enter integers:")

# display results
print(integer[::-1])


    
