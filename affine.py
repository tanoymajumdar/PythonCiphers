def afencode (text, a , b):
    l= len(text)
    c_text=""
    i=0
    while i<l:
        if ord (text[i])>= ord('a') and ord(text[i])<= ord('z'):
            x= ord(text[i])-97
            x = ((a*x)+b)%26
            x = x + 97
            c_text = c_text + chr(x)
            i = i + 1
       
        elif ord(text[i])>=ord('A') and ord(text[i])<= ord('Z'):
            x=ord(text[i])-65
            x = ((a*x)+b)%26
            x = x + 65
            c_text = c_text + chr(x)
            i = i + 1
        
        else:
            c_text = c_text+text[i]
            i = i+1
    return c_text
    
def mInverse( a, n ):
    r0, r1, t0, t1 = n, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
 
    if r1 == 1:
        return t1 % n
    return 0
    
def afdecode(cipher, a , b):
    l = len(cipher)
    c_text = ""
    i=0
    while i<l:
        if ord(cipher[i])>= ord('a') and ord(cipher[i])<= ord('z'):
            y = ord(cipher[i]) - 97
            x = (mInverse( a, 26 )*(y-b))%26
            x = x + 97
            c_text = c_text + chr(x)
            i = i + 1
        elif ord(cipher[i])>=ord('A') and ord(cipher[i])<= ord('Z'):
            y = ord(cipher[i])-65
            x = (mInverse( a, 26 )*(y-b))%26
            x = x + 65
            c_text = c_text + chr(x)
            i = i + 1
        else:
            c_text = c_text + cipher[i]
            i = i + 1
    return c_text
            
            
        
      
























            
