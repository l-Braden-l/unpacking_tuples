#Braden Leach
#January 14 2024
#Unpacking Tuples Practice



#----1----#
def calculate_product(num1,num2):
    my_product = num1 * num2
    my_sum = num1 + num2
    return my_sum,my_product
    
my_sum,my_product =calculate_product(2,5)
print(f'the sum of your two numbers are {my_sum} and the product is {my_product}.')


#----2----#
def max_min_numbers(num1,num2):
    min_num = min(num1,num2)
    max_num = max(num1,num2)
    return max_num,min_num

max_num,min_num = max_min_numbers(5000,100)
print(f'The largest of the too numbers is {max_num} and the smallest is {min_num}.')
