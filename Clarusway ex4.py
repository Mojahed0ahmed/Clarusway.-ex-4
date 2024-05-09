Ex 1
The_list = input ("Enter a list: ")
if len(The_list) == 0 :
    print ("This list is empty")

else :
    print("The list is not empty")
#####################
Ex 2
the_lst = input("Enter your list: ")
new_lst =list(the_lst)
if len (the_lst) >= 3 :
         new_lst.remove(max(the_lst))
         new_lst.remove(min(the_lst))
         new_lst.sort()
         print ('The new lest is:', (new_lst))
else :
         print ('error')
##############################
Ex 3
user_input = input("Enter a list separated by commas: ")
item_list = user_input.split(",")
j_list = "".join(item_list)

if len(item_list) == 5:
    print("your list is:",(j_list))
else:
    print("This list doesn't have the right size")


###############################################
Ex 4
quarters = [
        int(input("days Frank was sick in first quarter: ")),
        int(input("days Frank was sick in second quarter: ")),
        int(input("days Frank was sick in third quarter: ")),
        int(input("days Frank was sick in forth quarter: "))
]
total_sick_days = sum(quarters)

dancing_days = 365 - total_sick_days

print ("total of sick days",quarters)
print ("sick days is:",total_sick_days)
print ("Total dancing_days",dancing_days)

###############################
EX 4.2
qu1_first_year = 3
qu2_first_year = 10
qu3_first_year = 4
qu4_first_year =12
qu1_second_year = 14
qu2_second_year = 4
qu3_second_year = 20
qu4_second_year =5
first_year = [qu1_first_year , qu2_first_year , qu3_first_year , qu4_first_year]
second_year = [qu1_second_year , qu2_second_year , qu3_second_year , qu4_second_year]
all_sick_days = (first_year + second_year)

print("The full list of frank's sick day for two years are:",all_sick_days)

max_sick_days = max(all_sick_days)

if max_sick_days == qu1_first_year:
    print("Frank was sick the most in quarter 1 of the first year")
elif max_sick_days == qu2_first_year:
     print("Frank was sick the most in quarter 2 of the first year")
elif max_sick_days == qu3_first_year:
     print("Frank was sick the most in quarter 3 of the first year")
elif max_sick_days == qu4_first_year:
     print("Frank was sick the most in quarter 4 of the first year")
elif max_sick_days == qu1_second_year:
     print("Frank was sick the most in quarter 1 of the second year")
elif max_sick_days == qu2_second_year:
     print("Frank was sick the most in quarter 2 of the second year")
elif max_sick_days == qu3_second_year:
     print("Frank was sick the most in quarter 3 of the second year")
else:
     print("Frank was sick the most in quarter 4 of the second year")
