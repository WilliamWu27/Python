
def my_reverse(in_list):
    list_len = len(in_list)
    rev_list = []
    for i in range(list_len - 1, -1, -1):
        rev_list.append(in_list[i])
    
    return rev_list

orig_list = [2, 3, 6, 7, 8, 1, -98, 2, 3]
print(my_reverse(orig_list))


res = set()
for i in orig_list:
    if i not in res:
        res.add(i)
print ("The list after removing duplicates : " + str(res))