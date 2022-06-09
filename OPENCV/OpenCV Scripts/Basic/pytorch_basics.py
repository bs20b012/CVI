import torch
import numpy as np


#x=torch.empty(2)
#print(x)

#creating tensors from list or any other dtype :
#x = torch.tensor([2.3,4])
#print(x)


#simple operations :
#can use multiple functions add mul div sub and symbols too + - * /
#x = torch.rand(2,2)
#y = torch.rand(2,2)
#print(x)
#print(y)
#z = x + y 
#print(z)


#printing individual elements (like in matrices & slicing) :

#x=torch.rand(5,3)
#print(x)
#print(x[0,1])
#print(x[0,1].item()) #for true value of the tensor element 

#converting tensor to array using numpy:

#***********both point to the same address***********
#a=torch.ones(5)
#print(a)
#b=a.numpy()
#print(b)
#print(type(b))



#moving to cuda not working in cpu to increase speed :

