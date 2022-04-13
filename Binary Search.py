c=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        m=(l+u)//2
        if list[m]==n:
            globals() ['c']=m
            return True
        else:
            if list[m] <n:
                l=m
            else:
                u=m
    return False
list=[4,7,8,12,56,45,99]
n=56
if search(list,n):
    print("Found",c)
else:
    print("Not Found")