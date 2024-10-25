def main(a, b):
    '''a va b  bo'linmasinining yaxlitlangan qiymatini toping va uni qaytaring.
    
     Args:
     a (int): raqam
     b (int): raqam
    
     Qaytaradi:
     int: natija.
     '''
    y = (a / b)
    x = round (y,2)
    return x
print (main(9.2255,3.1164))