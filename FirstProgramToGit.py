gr='Hello World'
print(gr)
n=str(input("What's your name? \nMy name is:"))
import random
r=random.randint(0,4)
if n=='Chedda':
  n='Mister '+n
  c='Gouda'
elif r==3:
  c='Cheesed'
else:
  c='nice'
print('Hello',n+',',c,'to meet you.')
