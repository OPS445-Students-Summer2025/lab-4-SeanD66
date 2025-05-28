#!/usr/bin/env python3

list1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
join = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
match = [5, 6, 7, 8, 9]
diff = [1, 2, 3, 4, 10, 11, 12, 13, 14]



def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    jslist = list(set(l1)|set(l2))
    return jslist

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    mlist = list(set(l1).intersection(l2))
    return mlist

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    dlist = list(set(l1)^set(l2))
    return dlist

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))

