def product(num):
    if num.strip() and num.strip().isdigit():
      b=int(num)
      while b>10:
        m=1
        for i,v in enumerate(num): 
          m*=int(v)
        b=m
        num=str(b)
        print(num)
    else:
       print("Enter the valid input")
def sum(num):
    if num.strip() and num.strip().isdigit():
      b=int(num)
      while b>10:
        m=0
        for i,v in enumerate(num): 
          m+=int(v)
        b=m
        num=str(b)
        print(num)
    else:
       print("Enter the valid input")
while True:
    print("1.product")
    print("2.sum")
    print("3.exit")
    ch=int(input("enter the choice:"))
    if ch ==1:
        num=input("enter the number:")
        product(num)
    elif ch==2:
        num=input("enter the number")
        sum(num)
    elif ch==3:
        break
    else:
        print("enter the valid number:")
