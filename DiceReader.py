import d20
import re
from d20 import utils
import numpy as np
import matplotlib as plt


test_input = "2d6+5d10"
expressiondatabase = []
if (d20.roll(test_input)!= None): #This does ensure valid syntax... by crashing
    dice_terms = re.findall(r'\d+[dD]\d+', test_input)
    operators = re.findall(r'(?<=\d)([+\-])', test_input)
    print(dice_terms)
    dice_terms = [dice.split('d') for dice in dice_terms]
    print(dice_terms)
    print(operators)
# I started wanting to make an encoder and then found a library that does that but it does not let me interact with the encoding easily or at least its not well explained and so im back to square one I guess
# Use PMF
           
                



#  print("die trigger on ", i, test_input[i])
#             while (test_input[i-1].isdigit()==True):
#                 print(test_input[i-1])
#                 i-=1

# print(rollequation)
# print(vars(rollequation))
# print(rollequation.expr.left)




# print(binop)
# left = binop.expr
# print(left)
# dieroll = left.roll
# print(dieroll)
# dievalues = dieroll.num
# print(dievalues)
# diesize = dieroll.size
# print(diesize)
# time to do this in a cringe fashion using arrays
# I need 1 array with each possibility - works as a simple sum


# probabilities = [None] * dievalues
# for i in range(dievalues):
#     count = 1
#     arr = [None] * diesize
#     for j in range (diesize):
#         arr[j] = j+1
#         count += 1
#     probabilities[i] = arr
# print(type(probabilities[0]))
# print((probabilities))

# plt.bar()