#from math import*
#j=0
#print('Kirjutage 15 numbrid')
#for i in range(1,16,1): #range(15)
#    A=float(input(f'{i} Sisesta A : '))
#    if int(A)==A:  j+=1
#    print(j)
#j=0
#i=0
#while True:
#    i+=1
#    A=float(input(f'{i} Sisesta A : '))
#    if int(A)==A: j+=1
#    if i==15: break
#print(j)

#j=0
#i=0
#while i>=0 and i<9:
#    i+=1
#    A=float(input(f'{i} Sisesta A : '))
#    if int(A)==A: j+=1
#    if i==8:break
#print(j)

#2
#print('Sisesta number')
#j=0
#A=int(input('Sisesta A=> '))
#for i in range(1,A+1):
#    if int(A)==A: j+=i
#print(j)

#3
#j=1
#for i in range(1,9):
#    A=int(input('Sisesta A=> '))
#    if A>0: j*=A
#print(j)

#4
#for i in range(10,21):
#    print(i**2)

#5
#j=0
#N=int(input('Sisesta N=> '))
#for i in range(0,N):
#    a=int(input('sisesta number=> '))
#    if a<0: j+=a
#print(j)

#6
#j_1=0
#j_2=0
#j_3=0
#N=int(input('Sisesta N=> '))
#for i in range(0,N):
#    a=int(input('Sisesta number=> '))
#    if a<0: j_1+=1
#    elif a>0: j_2+=1
#    elif a==0: j_3+=1
#print(f'нечёт {j_1}',f'чётные {j_2}',f'Null {j_3}')

#7
#A=int(input('от=> '))
#B=int(input('до=> '))
#K=int(input('Кратное => '))
#for i in range(A,B+1):
#    if(i%K==0):
#        print(i)

#8
#for i in range(1,21):
#    print(f'{i} дюйм=',f'{i*2.5} см')

#9
#Summa=int(input('Summa=>'))
#Aastat=int(input('Aastat=> '))
#pr=3
#Profit=(Summa*pr/Aastat)/100
#Kokku=Summa+Profit
#print(Kokku)

#10
i=0
j=0
for i in range(1,11):
    A=int(input('Sisesta number 1 => '))
    B=int(input('Sisesta number 2=> '))
    if A==int(A) and B==int(B):
        if A>B:
            j={A} 
        elif A<B:
            j={B}
print(j)

    



