
# # name = ['Blake', 'John']

# # randomStuff = [1,1.2,False,[],'S']









# # # indexing
# # print(name[1])


# # for item in randomStuff:
# #     print(item)



# # #Create a script that creates the sentence from the folowing two lists:
# # list1 = ['I','your','dude']
# # list2 = ['am','boss','.']
# # sentence = ""
# # length = round((len(list1)+len(list2))/2)
# # for item in range(length):
# #     if len(list1) < item:
# #         sentence += list2[item]
# #     elif len(list2) < item:
# #         sentence += list1[item]
# #     else:
# #         sentence += list1[item]
# #         sentence += " "
# #         sentence += list2[item]
# #         sentence += " "
# # print(sentence)




# # # create a function that allows the user to create 2 list of len 5. The user must type in only numbers (int). Once all 10 numbers have been added, create a third list with the sum of the same index values.
# count = 0
# list1 = []
# list2 = []
# list3 = []
# while count < 10:
#     user = input("Enter 10 numbers to add to 2 lists: ")
#     count += 1
#     check = user.isdigit()
#     if check == True and count <= 5:
#         list1.append(user)
#     elif check == True and count <= 10:
#         list2.append(user)
#     else:
#         print("Try a number this time")
# for x in range(5):
#     list3.append(int(list1[x])+int(list2[x]))
# print(list1,"\n",list2,"\n",list3)



# # problem 3
# # create a script that ask the user for 3 family members. then ask them what rank they give them from 1-3. keep track of the rank in a seperate list.


names = []
rank = []
for x in range(3):
    user = str(input(f"Enter {3-x} family members: "))
    names.append(user)
    ranking = input(f"What rank do you want to give to your {names[x]}: ")
    rank.append(ranking)    
print("========Ranking=========")
for x in range(len(names)):
    print(f"{names[x]} - {rank[x]}")
print("========================")