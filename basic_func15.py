def main(a, b):
    '''A soni b ga bo'linganda qoldiqni toping va uning 3 darajasini hisoblab qaytaring.
    
     Args:
     a (int): raqam
     b (int): raqam
    
     Qaytaradi:
     int: natija.
     '''
    y = a % b
    x = pow (y,3)
    return x
print (main(15,4))
