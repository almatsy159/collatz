
# script used to compare expected result and real value , test the equivalence of values and numbers of steps. 

def get_odd_and_pow_of_2(even):
    if even == 0:
        return 0,0
    tmp = even 
    cpt = 0
    while tmp%2 == 0:
        tmp = tmp//2
        cpt += 1
    return tmp,cpt


def get_k_and_pow_of_4(even):
    if even == 0:
        return 0,0
    tmp = even 
    cpt = 0
    while tmp%4 == 0:
        tmp = tmp//4
        cpt += 1
    return tmp,cpt


def get_form(odd):
    # 3 mod 4 
    if odd%2 == 0:
        print("number is even !")
        return TypeError
    tmp = odd+1
    k,power_of_2 = get_odd_and_pow_of_2(tmp)
    print(f"{odd} = 2**{power_of_2}*{k}-1 = {2**power_of_2*k-1}")
    return power_of_2,k

def syr(x):
    if x %2 == 1:
        return (x*3+1)//2
    else :
        return x//2


def growth_phase(x):
    nb_step = 0
    while syr(x)>x:
        x = syr(x)
        nb_step +=1

    return x,nb_step

def compare(x):
    if x % 2 ==0:
        x = get_odd_and_pow_of_2(x)[0]
    
    # 2**n*k-1
    n,k = get_form(x)

    final_growth,nb_step = growth_phase(x)
    final_value_estimated = 3**n*k-1
    print(k,n,final_value_estimated,final_growth,nb_step)
    if final_value_estimated != final_growth or n != nb_step:
        raise ValueError

# uncomment to test odd in range 1 to 10⁶
"""
for n in range(1,1000000,2):
    compare(n)
"""

def get_form_decay(odd):
    if odd%2 == 0:
        print("x is even !")
        return TypeError
    if odd%4 == 3:
        print("x is 3 mod 4 !")
        return TypeError
    
    tmp = odd -1 
    k,power_of_4 = get_k_and_pow_of_4(tmp)
    print(f"{odd} = {k}*4**{power_of_4}+1 = {k*4**power_of_4+1}")
    return k,power_of_4


def syr2(x):
    if x % 4 == 1:
        res = (3*x+1)//4
        #print(res)
        return res
    if x % 2 == 0:
        res = x//2
        return res
    else :
        res = (x*3+1)//2
        print(res)
        return res
        
def decay_phase(x):
    nb_step=0
    while syr2(x)<x and x%2==1:
        print(x,syr2(x))
        x = syr2(x)
        nb_step += 1
    return x,nb_step

def compare2(x):
    if x%4 != 1 :
        print(" x is not 1 mod 4")
        return TypeError
    k,n = get_form_decay(x)
    almost_final_decay,nb_step = decay_phase(x)
    #if k % 2 == 1:
        #final_value_estimated = (3**n*k+1)//2
    #else :
    final_value_estimated = 3**n*k+1
    print(k,n,final_value_estimated,almost_final_decay,nb_step)
    if final_value_estimated != almost_final_decay or n != nb_step:
        raise ValueError
    

# uncomment to test 1mod4 in range [5:10⁶]
"""
for n in range(5,1000000,4):
    compare2(n)
"""
