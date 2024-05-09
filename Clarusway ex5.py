
#EX1
my_lst =[1,2,3,4,5,6,7,8,9]
my_lst1 =(my_lst[1:2]+my_lst[4:])
print(my_lst1)
################
#Ex2
my_tuple1 = (1,2,4,5,6)
my_tuple2 = (3,7,8,9)
new_tuple = my_tuple1 + my_tuple2
print(new_tuple)
####################
#Ex3;
my_lst=[1,2,3,4,5,6,7,8,9,10,'h','g','g']
my_lst1=len(my_lst)//2
first_lst = tuple(my_lst[:my_lst1])
second_lst = tuple (my_lst[my_lst1:])
print (first_lst)
print (second_lst)
#############################
#Ex3.2
my_lst=[1,2,3,4,5,6,7,8,9,10,'h','g','g']
first_lst = (my_lst[::2])
second_lst = (my_lst[1::2])
print (first_lst)
print (second_lst)
#########################3
#Ex4:
my_lst = [(2,3),(4,3),(4,1),(2,5),(6,7)]
my_lst1 = sorted(my_lst, key=lambda x: x[1])

print(my_lst1)

###################################
#Ex 5.1
my_lst = [1,5,7,8,6]
average_lst = sum(my_lst)/len(my_lst)
print("the average is :",average_lst)
#############################
#EX 5.2
my_lst = [1,5,7,8,6]
average_lst = sum(my_lst)/len(my_lst)
print("the average is :",average_lst)
my_lst.append(12)
print("add 12 to the list, The new list is :",my_lst)
average_lst = sum(my_lst)/len(my_lst)
print("the average is :",average_lst)
##############################################
