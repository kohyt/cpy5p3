# q6_display_matrix.py
# displays n by n matrix, n is positive integer

def print_matrix(n):
    import random
    for i in range(n):
        for h in range(n):
            print(random.randint(0,1), end = "")
        print("")

try:
    # get input
    n = int(input("Enter a positive integer:"))
    # check and display
    print_matrix(n)

except ValueError:
    print("Invalid input")
    
##if type(n) == int:
##    print_matrix(n)
##else:
##    print("Invalid input")



    


