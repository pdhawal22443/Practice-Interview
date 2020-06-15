#lets say we have existing function to devide two integers
# and now we want to Add functionality to check if any one integer is zero

def smart_devide(func):
    def test1(a,b):
        print("We are going to Divide {} and {}".format(a,b))

        if b == 0:
            print("We can't devide {} and {}".format(a,b))
            return
        return func(a,b)
    return test1

@smart_devide
def devide(a,b):
    return a/b

print(devide(2,5))

