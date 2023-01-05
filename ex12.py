Hour = int(input())
Rate = 10
if Hour < 40 :
    result = Hour * Rate
    print(result)
elif Hour >= 40 :
    result = (Hour - 40) * (15) + 400
    print(result)
print ('Well done ')
