a = int(input("enter a number :"))
if a > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(a) :
    print(i)
    if i > 2 : 
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')
