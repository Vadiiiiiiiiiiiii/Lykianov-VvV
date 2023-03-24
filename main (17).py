m=int(input("Введите четырехзначное число"))
if m>10000:
    print("Ошибка")
    u=m//1000
    p=m%1000
    w=q//100
    e=q%100
    r=e//10
    t=e%10
    a=u+w
    v=r+t
    if a ==v:
        print("Сумма первых и последних чисел равна")
    n=k+w+r+t
    if n%3:
        print("Сумма кратна 3")
    s=k*w*r*t
    if s%4:
        print("Произведение кратно 4")
    if s%m:
        print("Произведение кратно числу")
number=int(input())
if 99>number<100:
    num1=number//10
    num2=number%10
    print("Число десятков",num1,"\nЧисло единиц",num2)
else:
    print("неверное число")
    quit()