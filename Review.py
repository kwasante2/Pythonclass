# sum = 0
# print(sum)
num_1 = int(input("Enter a number"))
num_2 = int(input("Enter another number"))
num_3 = int(input("Enter the last number"))

sum_ = num_1 + num_2 + num_3 
avg= sum_/3 
print("The Sum is " + str(sum_) + ".  The average is " + str(avg) + ".")


norm_avg = avg > 5 and avg < 15
print (norm_avg)