def my_add(a,b):

    mysum = a ^ b
    carry_over = (a & b) << 1

    while(carry_over):

        a, b = mysum, carry_over
        mysum = a ^ b
        carry_over = (a & b) << 1

    return mysum


print(my_add(21,3400))
