P1=input().split(' ')
P2=input().split(' ')

x1,y1=P1
x2,y2=P2

distancia=(((float(x2)-float(x1))**2)+((float(y2)-float(y1))**2))**(1/2)

print('{:.4f}'.format(distancia))
