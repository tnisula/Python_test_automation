and_output1 = (10==10) and (10 > 9)
and_output2 = (10==11) and (10 > 9)
and_output3 = (10!=10) and (10 <= 9)

or_output1 = (10==10) or (10 < 9)
or_output2 = (10==10) or (10 < 9)
or_output3 = (10!=10) or (10 < 9)

not_true = not(10 == 10)
not_false = not (10 > 10)

print(and_output1)
print(and_output2)
print(and_output3)
print(or_output1)
print(or_output2)
print(or_output3)
print(not_false)
print(not_true)

"""
order of evaluation
1. not
2. and
3. or
"""

bool_output = True or not False and False
# True
print(bool_output)
bool_output1 = 10 == 10 or not 10 > 10 and 10 > 10
print(bool_output1)
# False
bool_output2 = (10 == 10 or not 10 > 10) and 10 > 10
print(bool_output2)