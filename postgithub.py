# how to go to HG
CONST = 3.14
my_list_str = ['hr', 'min', 'sec']
another1 = [[123, 44], [6, 7, 88]]
print another1
print my_list_str
another2 = []
another2.append(123)
another2.append(6)
print another2
another1.insert(2, 444)
print another1

sometuple = (1, 2)
somelist = [1, 2]
print sometuple
print somelist

a = tuple(range(10))
b = list(range(10))
print "a  ", a
print "b  ", b
print a.__sizeof__()  # 52 ie smaller
print b.__sizeof__()  # 88
b[5] = 3  # [3, 2]
# a[0] = 3     #error
print "a  ", a
print "b  ", b
b.append(566)
print "a  ", a
print "b  ", b

'''
If you went for a walk, you could note your coordinates at any instant in an (x,y) tuple.
If you wanted to record your journey, you could append your location every few seconds to a list.
But you couldn't do it the other way around.
	
This is an example of Python lists:
my_list = [0,1,2,3,4]
top_rock_list = ["Bohemian Rhapsody","Kashmir","Sweet Emotion", "Fortunate Son"]

This is an example of Python tuple:
my_tuple = (a,b,c,d,e)
celebrity_tuple = ("John", "Wayne", 90210, "Actor", "Male", "Dead")

The values of list can be changed any time but the values of tuples can't be change.
'''


c = [1,2,3]
print c
c[2] = 77
print c
print 'done'