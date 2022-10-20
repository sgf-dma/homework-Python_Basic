nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [x for lst_2 in nice_list for lst in lst_2 for x in lst]
print(result)
