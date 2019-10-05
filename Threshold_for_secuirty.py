from __future__ import division
from __future__ import print_function
import random
import functools
 
#=================================================================================================================
#=============================Code to key Generation using threahold's algorithmn==================================
_PRIME = int(input("Enter the Prime Number: "))
# 2**521 - 1
_RINT = functools.partial(random.SystemRandom().randint, 0)
def keygen():
    
 
    def _eval_at(poly, x, prime):
        accum = 0
        for coeff in reversed(poly):
            accum *= x
            accum += coeff
            accum %= prime
        return accum
 
    def make_random_shares(minimum, shares, prime=_PRIME):
    #Generates a random shares.
        if minimum > shares:
            raise ValueError("pool secret would be irrecoverable")
        poly = [_RINT(prime) for i in range(minimum)]
        points = [(i, _eval_at(poly, i, prime))
                  for i in range(1, shares + 1)]
        return poly[0], points
 
    def _extended_gcd(a, b):
        x = 0
        last_x = 1
        y = 1
        last_y = 0
        while b != 0:
            quot = a // b
            a, b = b, a%b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y
        return last_x, last_y
 
    def _divmod(num, den, p):
    #mod division
        inv, _ = _extended_gcd(den, p)
        return num * inv
 
    def _lagrange_interpolate(x, x_s, y_s, p):
    #Finding the Y value
        k = len(x_s)
        assert k == len(set(x_s)), "points must be distinct"
        def PI(vals):  
            accum = 1
            for v in vals:
                accum *= v
            return accum
        nums = []  
        dens = []
        for i in range(k):
            others = list(x_s)
            cur = others.pop(i)
            nums.append(PI(x - o for o in others))
            dens.append(PI(cur - o for o in others))
        den = PI(dens)
        num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
                   for i in range(k)])
        return (_divmod(num, den, p) + p) % p
 
    def recover_secret(shares, prime=_PRIME):
     #Recovering the Keys with y,x
        if len(shares) < 2:
            raise ValueError("need at least two shares")
        x_s, y_s = zip(*shares)
        return _lagrange_interpolate(0, x_s, y_s, prime)
 
    def maingen():
        #main function
        n=int(input("Enter the minimum keys required: "))
        s=int(input("Enter the no.of shares required: "))
        secret, shares = make_random_shares(minimum=n, shares=s)
 
        print('Generated secret Code is: ',secret)
        print('shares:')
        # if shares:
        #     for share in shares:
        #         print('  ', share)
        print(shares)
    maingen()
 
 
 
def secgen():
    def _extended_gcd(a, b):
        x = 0
        last_x = 1
        y = 1
        last_y = 0
        while b != 0:
            quot = a // b
            a, b = b, a%b
            x, last_x = last_x - quot * x, x
            y, last_y = last_y - quot * y, y
        return last_x, last_y
    def _divmod(num, den, p):
    #mod division
        inv, _ = _extended_gcd(den, p)
        return num * inv
 
    def _lagrange_interpolate(x, x_s, y_s, p):
    #Finding the Y value
        k = len(x_s)
        assert k == len(set(x_s)), "points must be distinct"
        def PI(vals):  
            accum = 1
            for v in vals:
                accum *= v
            return accum
        nums = []  
        dens = []
        for i in range(k):
            others = list(x_s)
            cur = others.pop(i)
            nums.append(PI(x - o for o in others))
            dens.append(PI(cur - o for o in others))
        den = PI(dens)
        num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
                   for i in range(k)])
        return (_divmod(num, den, p) + p) % p
 
    def recover_secret(shares, prime=_PRIME):
     #Recovering the Keys with y,x
        if len(shares) < 2:
            raise ValueError("need at least two shares")
        x_s, y_s = zip(*shares)
        return _lagrange_interpolate(0, x_s, y_s, prime)
 
    def mainsec():
           ns=int(input("Enter the no.of subset share keys u got: "))
           rs=[]
           for i in range(ns):
               m=int(input("Enter the i value of the person: "))
               s=int(input("Enter his secret key: "))
               p=(m,s)
               rs.append(p)
           print('secret recovered from  subset of share key: ', recover_secret(rs[:ns]))
 
 
    mainsec()
 
 
def rsa():
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"," r","s","t","u","v","w","x","y","z",",","0","1","2","3","4","5","6","7","8","9"] 
    pt=str(input("Enter the data to be encypted:")) 
    pl=len(pt) 
    p1=int(input("Enter the first prime number: ")) 
    p2=int(input("Enter the second prime number: ")) 
    n=p1*p2 
    relprime=[] 
    enc=[] 
    dt=[] 
    dec=[] 
    relprime.append(1) 
    pin=(p1-1)*(p2-1) 
    for i in range(2,pin): 
        if(pin%i!=0): 
            if(i!=pin): 
                e=i 
                break 
 
    for a in range(2,pin+1): 
        k=0 
        for i in range(2,a//2+1): 
            if(a%i==0): 
                k=k+1 
        if(k<=0): 
            relprime.append(a) 
    l=len(relprime) 
    for i in range(l): 
        if((relprime[i]*e)%pin==1): 
            d=relprime[i] 
            break 
    for i in range(pl): 
        for j in range(37): 
            if(pt[i]==alpha[j]): 
                c=(pow(j,e))%n 
                enc.append(c) 
    e=''.join(map(str, enc)) 
    print("Encrypted data is: ",e) 
    encl=len(enc) 
    for i in range(encl): 
        p=(pow(enc[i],d))%n 
        dec.append(p) 
    for i in range(len(dec)): 
        dt.append(alpha[dec[i]])
    f=''.join(map(str, dt)) 
 
    print("Decypted data is:",f)
 
def main():
    p=int(input('''Enter 
    1: Key Geneation 
    2:Generating Secret key from Distribution
    3: Key Sharing Using RSA
    ''' ))
 
    if p==1:
        keygen()
    elif p==2:
        secgen()
    elif p==3:
        rsa()
 
main()
 
 
 #====================Enc and Dec=========================
import time
 
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"," r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9",",","/","!","@","#","$","%","&","(",")","[","]"] 
print(len(alpha))
def enc(key,string):
    s=[]
    en=[]
    eni=[]
    de=[]
    deci=[]
    dec=[]
    enc=[]
    n=int(input("Enter the minimum keys required to generate the Key: "))
    for i in range(len(string)):
        for j in range(len(alpha)):
            if string[i]==alpha[j]:
                j=(j+n)%len(alpha)
                s.append(j)
    print(s)
    for i in range(len(s)):
        for j in range(key+2):
            if int(s[i])*j>key:
                k=((int(s[i])*j)-key)%len(alpha)
                en.append(alpha[k])
                eni.append(alpha[j])
                break
    f = open("enc.txt", "w")
    f.write(str(n))
    for i in range(len(en)):
        f.write(en[i])
        f.write(eni[i])
    f.close()
    print(en)
    print(eni)
    t=int(input('''
        1: Decrypt
        0: exit'''))
    if t==1:
        g = open("dec.txt", "w")
        f = open("enc.txt", "r")
        r=f.read()
        #print(r[1])
        n1=r[0]
        m=[]
        d=[]
        for i in range(1,len(r)):
            if i%2 ==0:
                m.append(r[i])
            elif i%2!=0:
                d.append(r[i])
 
        for i in range(len(m)):
            for j in range(len(alpha)):
                if m[i]==alpha[j]:
                    deci.append(j)
                    print("The m value is: ",m[i])
                if d[i]==alpha[j]:
                    de.append(j)
                    print("The d value is: ",d[i])
        for i in range(len(m)):
            y=((key+int(de[i]))/int(deci[i]))-int(n1)
            #print("The y value is: ",y)
            #print("The alpha value: ",alpha[y])
            dec.append(alpha[y])
        for i in range(len(dec)):
            g.write(dec[i])
 
        g.close()
    elif t==0:
        print("Bye")
        time.sleep(3)
        exit()
 
k=int(input("Enter the key: "))
st=str(input("Enter the string: "))
enc(k,st)

