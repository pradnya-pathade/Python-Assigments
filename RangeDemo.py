"""
- Range is sequnce as well as Datatype 
- if we get o/p of type() it proves that its a data type cause type() used for datatype
- if we get o/p of len() it proves that its a sequnce cause len() used for seq
"""
Data = range(5)
print(Data)
print(type(Data))

Data1 = range(1,7)
print(Data1)

Data2 = range(3,9,2)
print(Data2)

print(len(Data))
print(len(Data1))
print(len(Data2))