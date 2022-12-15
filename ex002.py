name = input('Enter your name: ')
print('Hi '+ name + '. How are you?')
age = int(input('Give me your age: '))
    
if(age<50):
    print('You are {} years old. You are young!'.format(age))    
    
elif (age>=50 & age<=100):
    print('You are {} years old. You are old.'.format(age))

else:
    print('You are {} years old : You are like Matusalem'.format(age))