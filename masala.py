 # 1-masala
son=int(input("sonni kiriting"))
if son %2==0:
    print("juft son")
else:
    print("toq son")

# 2-masala
son=int(input("sonni kiriting:"))
if son==0:
    print("nol")
elif son>0:
    print("musbat son")
else:
    print("manfiy son")

# 3-masala
a=int(input("a sonni kiriting"))
b=int(input(" b sonni kiriting"))
if a>b:
    print("b sondan a son katta")
elif a<b:
    print("a sondan b son katta")
else:
    print("ikkala son ham teng")

# 4-masala
son=int(input("sonlarni kiriting"))
summa=0
for raqam in str(son):
    summa += int(raqam)

print(summa)


# 5- masala
son=int(input("sonni kiriting"))
teskari=int(str(son)[::-1])
print(teskari)
matn=input("matn yozing")
teskari=str(matn)[::-1]
print(teskari)

# 6-masala
son=int(input("sonni kiriting:"))
kopaytma = 1
for raqam in str(son):
    kopaytma *= int(raqam)

print(kopaytma)

# 7-masala
son = 1221

if str(son) == str(son)[::-1]:
    print(True)
else:
    print(False)

# 8-masala
son=29
if son <= 1:
    print("Tub emas")
else:
    for i in range(2, son):
        if son % i == 0:
            print("Tub emas")
            break
    else:
        print("Tub son")


# 9-masala tuple

t=(1,2,3,4)
print(len(t))

# 10-masala
t=(5,8,2,9)
eng_katta=max(t)
print("eng katta",eng_katta)

# 11-masala
t=(7,7,3,7,1)
noyon_son=len(set(t))
print(noyon_son)

# 12-masala
t=(1,2,3,4,5)
teskari=t[::-1]
print(teskari)

# 13-masala
t=(10,20,30)
yigindi=sum(t)
print(yigindi)

# 14-masala
t=("a","b","a","c")
noyob = set(t)
print(noyob)

# 15-masala
s={1,2,3}
if 2 in s:
    print("2 bor")
else:
    print("2 yoq")

# 16-masala
t={4,5,6}
print(len(t))

# 17-masala
t=(1,2,3)
new_set=set(t)
print(new_set)

# 18-masala
s={1,2,3}
new_tuple=tuple(s)
print(new_tuple)

# 19-masala ortacha
t=(1,2,2,3,4,4)
olib_tashlash=tuple(set(t))
print(olib_tashlash)

# 20-masala
t1=(1,2,3)
t2=(3,4,5)
umumiy = set(t1) & set(t2)
print(umumiy)

# 21-masala
t=(5,3,8,1)
sorted_tuple = tuple(sorted(t))
print(sorted_tuple)


# 22-masala
s1={1,2,3}
s2={3,4,5}
print(s1.union(s2))

# 23-masala
t=(1,2,3,4,5)