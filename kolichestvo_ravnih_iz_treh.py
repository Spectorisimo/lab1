numbers=[]
dictionary={}
[numbers.append(int(input())) for i in range(3)]
for i in numbers:
    dictionary[i]=numbers.count(i)
if max(dictionary.values())<=1:
    print(0)
else:
    print(max(dictionary.values()))



