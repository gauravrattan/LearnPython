# Task-3


def  fried_func(fried):
    for i in fried:
        for k,v in i.items():           
            print(f'\t{k}:-{v}')

for i in a_dict:
    #print(i)
    #print (i.items())
    for key,value in i.items():
        if isinstance(value,list):
            print(f'{key}:- ')
            fried_func(value)
        else:
            print(f'{key} :- {value}')
