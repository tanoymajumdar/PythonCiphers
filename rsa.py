def rsaencrypt(value, n, e):
    cipher = pow (value, e, n)
    return cipher
    
def rsadecrypt(value, n, d):
    decipher = pow (value, d, n)
    return decipher

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
    
def rsahack(n, e):
    i=2
    p=0
    q=0
    while i<n:
        if n%i==0:
            p=i
            break
        else:
            i=i+1
    q = int(n/p)
    phi_n = (p-1)*(q-1)
    d = mInverse( e, phi_n )
    return d
        

    