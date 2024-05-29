def add(**kwargs):
    summ = 0
    for k,v in kwargs.items():
        if isinstance(v,int):
            summ += v
    print(summ)
    
add(a=1,b=2,c=34) 