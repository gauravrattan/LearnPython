# Task=1

def add_number(*args):
    print(args)  # Inside the function, args is a tuple
    print(type(args))
    total = sum(args)  
    print(total)

add_number(1, 2, 3)


# Task=2

def student_result(**kwargs):
    print(kwargs) # Inside the function, kwargs is a dictionary
    failed_marks=37
    total=0
    max_marks=0
    max_user=''
    failed_user=[]
    for name in kwargs:
        total=total+kwargs[name]
        
        #for max user
        if kwargs[name]>max_marks:
            max_marks=kwargs[name]
            max_user=name
        
        #for failed user    
        if kwargs[name]<failed_marks:
            failed_user.append(name)
            
    #print(total)
    average_marks=total/len(kwargs)
    print('Average Marks is:-',average_marks)
    print(f'{max_user}:{max_marks}')
    print(failed_user)
    
    
student_result(gaurav=72,sundeep=56,raj=27,shivam=29)
