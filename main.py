
def return_duplicates(a_list):
    dup_dict = dict()
    a_set = set()
    for item in a_list:
        ln1 = len(a_set)
        a_set.add(item)
        ln2 = len(a_set)
        if ln1 == ln2:
            try:
                dup_dict[item] += 1
            except:
                dup_dict[item] = 1
    return dup_dict

a_list = ["BMW", "Mercedes", "BMW", "Audi", "Volvo", "Volvo", "Volvo"]
dups = return_duplicates(a_list)
print(dups)