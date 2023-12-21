
import numpy as np
import time
#input=[[3,3],
#       [5,10,5],
#       [5,5,5],
#       [10,5,10]]
import datetime
import random

t0=time.time()
print(t0)

input=[[20,20],
       [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
       [5,8,4],
       [1,6,9],
       [9,9,4]]

#random.seed(0)
#inpu = [[random.randint(0,900) for i in range(20)] for j in range(20)]
#input=[[20,20]]+inpu

np.random.seed(0)
M = np.random.randint(900,size=(100,100)).tolist()

print(M)

input=[[100,100]]+M


matriz = input[1:]

w=input[0][0]
h=input[0][1]
number=w*h

helpM=[[[j,i] for i in range(w)] for j in range(h)]
#print(helpM)

l = [j for i in matriz for j in i]
l = {x:l.count(x) for x in l}
l = dict(sorted(l.items(),reverse=True))
l["*"]=0
ajuda=False

def myfind(i,j,vis):
       if j == 0:
              vis = vis + [[i, j+1]]
       elif j == w-1:
              vis = vis + [[i, j-1]]
       else:
              vis = vis + [[i, j - 1]]
              vis = vis + [[i, j+1]]
       return vis

keys=list(l.keys())
n = keys[0]

while l["*"]!=number:
       lastOnes = False
       sol=[]

       if lastOnes == True:
              for i in reversed(range(len(matriz))):
                     for j in reversed(range(len(matriz[i]))):
                            if matriz[i][j]!="*":
                                   sol=[helpM[i][j],matriz[i][j]]
       if sol!=[]:
              print("lastOnes")
              break

       vis=[]
       a=0
       b=0
       x=0
       y=1
       while vis==[]:
              x=x+1
              if l[n]<x:
                     #print("_",n)
                     n=n-1
                     if n==0:
                            lastOnes = True
                            break
                     else:
                            while n not in keys:
                                   n = n - 1
                     x=1
                     #print("__", n)


              #print(n)
              #print(matriz)
              count=0
              for i in range(a,len(matriz)):
                     for j in range(b,len(matriz[i])):
                            if matriz[i][j]==n:
                                   count=count+1
                            if count==x:
                                   ajuda=True
                                   break
                     if ajuda==True:
                            break
              ajuda=False

              #print(i,j)

              vis = []
              if i == 0:
                     vis = vis + myfind(i,j,vis)
                     vis = vis + [[i +1, j]]
              elif i == h-1:
                     vis = vis + [[i-1,j]]
                     vis = vis + myfind(i, j, vis)
              else:
                     vis = vis + [[i - 1, j]]
                     vis = vis + myfind(i, j, vis)
                     vis = vis + [[i +1, j]]

              vis = [[matriz[k[0]][k[1]],k] for k in vis]
              vis = [k for k in vis if "*" not in k]

              if n == keys[len(keys)-1] and l[n]<x and vis==[]:
                     lastOnes=True
                     #print("lastOnes")
                     break

       if lastOnes == True:
              #print(matriz)
              for i in range(len(matriz)-1,-1,-1):
                     for j in range(len(matriz[i])-1,-1,-1):
                            if matriz[i][j]!="*":
                                   sol=[helpM[i][j],matriz[i][j]]
                                   ajuda=True
                                   break
                     if ajuda==True:
                            break
       ajuda=False

       if sol!=[]:
              #print("lastOnes")
              break

       #print(matriz)
       #print(i,j)
       #print(vis)

       minVis=min([k[0] for k in vis])
       minVisCor=[]
       for k in vis:
              if k[0]==minVis:
                     minVisCor=k[1]
                     break

       if minVis<n:
              matriz[minVisCor[0]][minVisCor[1]]=n-minVis
              matriz[i][j]="*"
              l[n]=l[n]-1
              l[minVis]=l[minVis]-1
              if n-minVis not in keys:
                     l[n-minVis]=1
                     najuda=l["*"]
                     l.pop("*")
                     l = dict(sorted(l.items(), reverse=True))
                     keys = list(l.keys())
                     l["*"]=najuda
              else:
                     l[n - minVis] = l[n - minVis]+1
              l["*"]=l["*"]+1
              helpM[minVisCor[0]][minVisCor[1]]=helpM[i][j]
              helpM[i][j]="*"
       else:
              matriz[i][j] = "*"
              matriz[minVisCor[0]][minVisCor[1]] = "*"
              l[n] = l[n] - 1
              l[minVis] = l[minVis] - 1
              l["*"] = l["*"] + 2
              helpM[i][j] = "*"
              helpM[minVisCor[0]][minVisCor[1]] = "*"

       #print(l)
       #print(matriz)
       #print("-----------------")


print(matriz)
#print(l)
if sol==[]:
       print("no winner")
else:
       print("sol",sol)

t1=time.time()
print(t1-t0)

#print(matriz.index(5))




