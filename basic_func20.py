import math
def main(a, b):
    '''logarifm a asosga ko'r b ning qiymatini toping.
    
     Args:
     a (int): raqam
     b (int): raqam
    
     Qaytaradi:
     int: natija.
     '''
    x = math.log(b,a)
    return x 
print (main(10,100))