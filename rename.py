
import os
import random

path = r'F:\test1'
rename_dict = {}
list_ = []
for parent, dirname, files in os.walk(path):
    list_.append(parent)


seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_one():
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = ''.join(random.sample(seed,k=4))
    return name

start = False


def modify_list(list_,tail):
    list_sub = []
    for ele in list_:
        if tail in ele:
            ele = ele.replace(tail,rename_dict[tail])
        list_sub.append(ele)
    return list_sub

# for item in list_:
    # head, tail = os.path.split(item)
    # print(head, tail)
    # if not start:
    #     start = True
    #     continue
    # if start:
    #     if tail not in rename_dict:
    #         rename_dict[tail] = get_one() + tail
    #     os.rename(item, os.path.join(head, get_one() + rename_dict[tail]))
    #     list_ = modify_list(list_, tail)

print(len(list_))
for i in range(len(list_)-1,-1,-1):

    head,tail = os.path.split(list_[i])
    name, ext = os.path.splitext(tail)
    print(name, ext)
    if name not in rename_dict:
        rename_dict[name] = get_one() + '_' + name
    os.rename(list_[i], os.path.join(head,  rename_dict[name] + ext))

    # list_ = modify_list(list_, tail)



