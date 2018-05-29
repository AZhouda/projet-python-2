
# coding: utf-8

# In[1]:


from math import log


# In[2]:




def minProd(K):
    s = 3  
    for n in range(4, K+1) :
        smalest = float('inf') 
        for k in range(1, int( log(n, 2) )+1 ):
            if smalest > sliding_window(n=n, k=k) :
                smalest = sliding_window(n=n, k=k)
        s = s + smalest

    return s


# In[4]:



def sliding_window(n, k):
    
    odd_pow = {1:2, 2:4}

    m = bin(n)
    m = m[2:]
    m = m[::-1]

   
    X, i, ch_len = 1, len(m)-1, 0

    while i > -1 :
        
        if m[i] == '1' :
            
            for a in range(k) :

                if i-a > 0 :
                    b = i-a
                else :
                    b = 0

                if m[b] == '1' :
                    window = m[ b:i+1 ]
                    c = b
                    
            window = window[::-1]

            for _ in range(i-c+1):
                X = X**2
            
      
            if X > 1 :
                ch_len += i-c+1
            
           
            while int(window, 2) not in odd_pow :
                i = len(odd_pow)-1
                odd_pow[2*i+1] = odd_pow[2*i-1]*2

            if odd_pow[ int(window, 2) ] > 1 :

                if X > 1 :
                    ch_len += 1

                X = X*odd_pow[ int(window, 2) ]
            
            i = c-1
    
        else : 
            X, ch_len, i = X*X, ch_len+1, i-1

    ch_len += len(odd_pow)-1  
    return ch_len


# In[5]:



a = 200
print( "Sommes des chaines d'exponentiations a l'aide de l'algorithme sliding window, pour borne sup =", a ,":", minProd(K=a) )

