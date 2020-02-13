#take a list of numbers
my_list = [10, 15, 20, 25, 27, 30, 32,45]
#use anonymous function to filter
result = list(filter(lambda x: (x % 2 == 0), my_list))
#display the result
print("numbers divisible by 2 are",result)

# Take a list of numbers
my_list = [10, 15, 20, 25, 27, 30, 32,45]
#use anonymous function to filter
result = list(filter(lambda x: (x % 5 == 0), my_list))
#display the result
print("numbers divisible by 5 are",result)