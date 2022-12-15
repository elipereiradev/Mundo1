#lists with python

""" list1 = [1,2,3,4]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
list4 = [1, 'a', True]
numbers = [1,2,3,4,5,6,7,8,9]
quadrados_impares = [numbers ** 2 for numbers in numbers if numbers % 2 == 1]
quadrados_pares = [numbers ** 2 for numbers in numbers if numbers % 2 == 0] """


#for multi_list in list1:
#  print(multi_list **2)

#print(list1[0], list2[0], list3[0], list4[0])

#print(quadrados_impares)
#print(quadrados_pares)

""" def anexa_correto(elem, lista=None):
    if not lista:
        lista = []
    lista.append(elem)
    return lista """

""" a, b = 40, 50
print(a, b) """

def foo(a,b, c, **args, **kwargs):
    print('a: {} {}'.format(a, type(a)))
    print('b: {} {}'.format(b, type(b)))
    print('c: {} {}'.format(c, type(c)))
    print('args: {} {}'.format(args, type(args)))
    print('kwargs: {} {}'.format(kwargs, type(kwargs)))

print foo(1,2,3)