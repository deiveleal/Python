import matplotlib.pyplot as plt


primeiros_5 = []
primeiros_5000 = []


for i in range(5000):
    primeiros_5000.append(i**3)
for i in range(5):
    primeiros_5.append(i**3)
    
print(primeiros_5)
print(primeiros_5000)

plt.scatter(range(5), primeiros_5, c=primeiros_5, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.scatter(range(5000), primeiros_5000, c=primeiros_5000, cmap=plt.cm.Blues,edgecolors='none',s=1)
