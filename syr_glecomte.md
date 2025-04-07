# 3N+1 || N/2

here i'm presenting my work on 3n+1



# 3^N
 = (2+1)^N


## k(x,y)u

Here is what i was working on before coming back to the syracuse problem.

Working with association of 2 and 3 then 2^n and 3^n. Where 2^n is my y axis and 3^n my x axis.

k*(x,y)(3,2) = N

- 2 * 2 * 2 = 8
- 2 * 2 * 3 = 12
- 2 * 3 * 3 = 18
- 3 * 3 * 3 = 27

## {3N+k}
(3n+k)[3] = k

### {3N} :
0. 0
1. 3
2. 6
3. 9
4. 12

### {3N+1} :
0. 1
1. 4
2. 7
3. 10
4. 13

### {3N+2} :
0. 2
1. 5
2. 8
3. 11
4. 14

### Table

| N | 3N | 3N+1 | 3N+2 |
| --- | --- | --- | --- |
|0|0|1|2|
|1|3|4|5|
|2|6|7|8|
|3|9|10|11|
|4|12|13|14|
|5|15|16|17|
|6|18|19|20|
|7|21|22|23|
|8|24|25|26|
|9|27|28|29|
|10|30|31|32|

from this view many propreties of cyracuse are visible

### definition of values :

#### even Number :

    {3n,even}   =     {3n} + {3n}      
    {3n+1,even} =   {3n+2} + {3n+2}
    {3n+2,even} =   {3n+1} + {3n+1}

#### odd Number :

    {3n,odd}     = {3n+2} + {3n+1}
    {3n+1,odd}   = {3n+1} + {3n}
    {3n+2,odd}   = {3n} + {3(n-1)+2}

Note : for even there are I,I and P,P and for odd there are P,I and I,P
cf split section

#### By Rank :
where n = rank
##### even Rank:

  {3n,even} have even rank
  {3n+1,even} have odd rank
  {3n+2,even} have even rank

##### odd Rank:
  reciprocally

  {3n,odd} have odd rank
  {3n+1,odd} have even rank
  {3n+2,odd} have odd rank



## Division alternative

### split(N,k)

"split Number by k"
Instead of dividing by cutting in n our number(k) to get 1 of the remaining part (k/n) ,we just split into an n dimension object
divide(8,2) = 4  split(8,2) = (4,4)
divide(27,3) = 9 split(27,3) = (9,9,9)
divide(12,4) =3 split(12,4) = (3,3,3,3)

so instead of having a one dimensionnal number like after dividing, after spliting we got an n dimensionnal number.
so if i want to split a number by seven, as split (49,7), i make a seven dimensionnal number (0,0,0,0,0,0,0) and add one to each until i reach the end.
then i add 1 to the first and so on...

1. remaining = 49 : (0,0,0,0,0,0,0)
2. remaining = 48 : (1,0,0,0,0,0,0)
7. remaining = 42 : (1,1,1,1,1,1,1)
8. remaining = 41 : (2,1,1,1,1,1,1)
...
49. remaining = 0 : (7,7,7,7,7,7,7)

the number is equal to the sum of all his dimension

## Representation of N:
    
img gen from py
    ...
    
                                                 aa,ab,ac,ba,bb,bc,ca,cb,cc = 3²*k9 + g9
                                                 

                                                            a,b,c            = 3¹*k3 + g3

                                                              N              = 3⁰*N*2⁰ + 0  
           
                                                             M,m             = 2¹*k2 + g2
       
                                                         k0,k1,k1,k2         = 2²*k4 + g4
       
    ...

    There are stable and instable state.
    The view 3=>2 and taking Mf,mf is equivalent to 2=>3 a,c
    a method similar to derivative may be used here.


    Na =(+b)> Nb =(+M)> Nc
    Nb - b = Na
    Nb + Mb = Nc

### split by 2 :

doing a split by two to a even Number:

- P = (I,I) || (P,P)

ex : 6 = (3,3)
or : 8 = (4,4)

by splitting an odd Number (by two), we obtain:

*note: we could make a split with a bigger difference between terms but i will focus only on splitting by minimizing the delta between number (for odd number : 1 and 0 for even number )*

- I = (P,I) || (I,P)

ex : 13 = 7 + 6
or : 15 = 8 + 7

*note* :

        P = (k,k)
        if split(N,2) == (P,I) :
            split(N,4) = (k,k,k,k-1)
        elif split(N,2) == (I,P) :
            split(N,4) = (k+1,k,k,k)


## form of 3n+1||n/2

for this example i am gonna use a special number that came from 27 and start a long additive journey
it's 31. and also 2⁵-1

*apparently some (2^n)-1 come from 3^k :*

9 => 7 = 2³-1

27 => 31 = 2⁵-1 (27+14+21 = 62)=>(62/2)=31

81 => 61 = 2⁶-1 (81+41=122)=>(122/2)=61


### firsts values of 31 :


#### classic form :

    [31,94,47,142,71,214,107,322,161,484,242,121]

#### compressed form :

    [31,47,71,107,161,242,121]


####  Delta

By doing delta of the values in the compressed form we notice some pattern:
- 31 + 16 = 47
- 47 + 24 = 71
- 71 + 36 = 107
- 107 + 54 = 161
- 161 + 81 = 242

### Number

N = (Max+Min) = (P+I)||(I+P)
(N*3+1)/2 = N + N.max

    N  =>  PI       || IP
    M,m    k,k,k,k-1 || k+1,k,k,k
    N = 2¹* M - 1 || 2¹* m + 1

    PPPI = 3P + I = 3 * (k,k) + (k,k-1) =  7*k + k-1

#### Deduction

From delta and Number combined with the view detailled before we can se that compressed form is equivalent to N + N.max

{3n,odd} = {3n+2} + {3n+1} => + {3n+2}
{3n+1,odd} = {3n+1} + {3n} => + {3n+1}
{3n+2,odd} = {3(n-1)+3} + {3(n-1)+2} => + {3(n-1) + 3}


dividing by 2...


#### Deltas pattern

    [16,24,36,54,81]

another way of writing it would be

    [2⁴,2³*3,2²*3²,2*3³,3⁴]

following this pattern starting by
    
$$2^n-1 : Max = 2^n , NextMax = 2^{(n-1)}*3¹ ... FinalMax = 3^n$$

lead us to
    
$$3^n-1$$


#### Formula

m = n+1

so :

$$ 2^m-1 + \sum_{i=0}^{n-1} 2^{k-i} * 3^i = 2*3^n-1$$

and :

$$ 2*3^n-1 = 3^n + 3^n-1 =>(+3^n) = 3^m-1 $$

and as :
    k * sum(xi) = sum(k * xi)


$$ k* 2^n-1 + \sum_{i=0}^{n-1} k * 2^{k-i} * 3^i = k *2 * 3^n-1$$

*note: it is the same for :*
    
    # here it is pretty approximative need to review

    2^n + max^n = 3^n

    8 + 4 + 6 + 9 = 27
    16 + 8 + 12 + 18 + 27 = 81


    16 + 8 + 12 + 18 + (27) = 16 + 8 + 12 + 18 + (8 + 4 + 6 + 9) = 81

with a certain method that can be showed in the collab

27 that got around 111 step (around 80 in compressed form) reduce to around 20 step

depending of the choice that you make for the limit
(if the limit is 2*3^n-1 3^n-1,n is odd, or 3^n-1,n is odd)

### new form:

 2⁵-1 = 31 = 16,15 = 2⁴,2⁴-1 ...=> 3⁴,3⁴-1 : 161
 161 = 2*81-1 =(+81)> 242 = 3⁵-1

## check value here

111 base 3 = 13  =(*3+1)> 1111 base 3 = 40

11111 base 3 : 161 => 111111 base 3 = 364
                                      
    [31,242,121]

# 3^n

## in base 3

3^n is 100...0 with the number of 0 = n-1

and 3^n -1 belong to {3k+2} and is 22...2 with number of 2 = n-1

it's divisible by two

and it make 1...1 with number of 1 = n


# convergence

finally :

n is even and m is odd

we saw earlier that 2^n-1 move forward 3^n-1
and so 2^m-1 lead us to 3^m-1

as 3^m-1 is even and m is odd we know (see the periodic behaviour of the divisibility by 2 of 3^n) that we can only divide once 3^n-1 and it can be seen in base 3.

222...2 (m ,is odd, times 2)
and so dividing it by 2 give us 11..1 (m times 1) an odd number of 1 isn't a even number ...
so i'm multipling it by 3. it give us 11...10 (m times 1 plus one 0) and add one to it so it's giving us (m+1 times 1 or n times 1)
and clearly we now see that it tend to be the same value than 3^n-1/2
as we have 22...2 (n, is even, times 2) ,it's even we can divide it by 2 and got 11.....1 (n times 1) !


       if n is even:
           n/2 is still divisible by two
       if n is odd :
           n/2 is not divisible by two so going toward 3^(n+1)



This is still draft. And there are still a lot of work to achieve to be more rigorous and formal.

source code corresponding : <http://www.github.com/almatsy159/syracuse>

Author Gaëtan Lecomte





    










