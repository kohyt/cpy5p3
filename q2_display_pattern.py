# q2_display_pattern.py
# display pattern with an additional number as it goes

def display_pattern(n):
    n += 2
    for i in range(1,n):
        for h in range(n,i,-1):
            print(end = " "*((h//10)+2))
        for j in range(i-1,0,-1):
            print(j, end = " ")
        print()
       
   

# get input
n = int(input("Enter number:"))
display_pattern(n)

##def asterix_triangle(i, t=0):
##    if i == 0:
##        return 0
##    else:
##        print(' ' * (i) + '*' * ( t ))
##        return asterix_triangle( i - 1, t + 1 )
##
##asterix_triangle(5)


         
