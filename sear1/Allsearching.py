# linear searching :
# code is ablable in discrepation . you can see there::::
def linear_search(lst,search):

    for i in range(len(lst)):

        if lst[i]==search:
            return "your value is :",i
    return None

# this for binar search::::::::
def binar_search(lst,search):

    low=0
    high=len(lst)
    while low<=high:

        mid=(low+high)//2
        if lst[mid]==search:
            return mid
        elif lst[mid]<search:
            low=mid+1
        else:
            high=mid-1
def main():
    print("\n1.for Linear search\n2.for binary_search")
    choice=int(input("enter the number which you find:"))
    if choice==1:
        lst=eval(input("enter the list :"))
        fin=int(input("enter the number :"))
        a=linear_search(lst,fin)
        print(a)
    elif choice==2:
        lst=eval(input("enter the list :"))
        fin=int(input("enter the number :"))
        a=binar_search(lst,fin)
        print(a)
    else:
        print("value is not found")

if __name__ == '__main__':
    main()

