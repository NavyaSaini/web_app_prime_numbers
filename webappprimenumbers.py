import streamlit as st 
import pandas as pd 
import math 
import numpy as np 

st.title('Explore Prime Numbers') 
st.header('Find if a number is prime, prime numbers under a particular integer, odd/even prime numbers')

#to tell if a number is prime 
def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
isprime = st.number_input("Enter n an integer",3)
isprime = int(isprime)
Answer =is_prime(isprime)
if Answer:
    s = " is a prime number"
else:
    s = "is not a prime number"
st.write('{}'.format(isprime),s  )
def even_numbers(lst):
    l = lst[:]
    for x in l:
        if not x%2 == 0:
            l.remove(x)
    return l

def primes(n):
    #https://radiusofcircle.blogspot.com/2016/06/problem-50-project-euler-solution-with-python.html
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    # even numbers except 2 have been eliminated
    for i in np.arange(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in np.arange(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime  

L = 0
K = [[50,50]]
for i in range(1, 100):
    for j in range(100,i,-1):
        if i+j == 100:
            K.append([i,j])
    
          
            L+= 1


n = isprime

primesundern =primes(n)


            
if(st.button('Find prime numbers under n')):
      
    # print the BMI INDEX
    st.text("The prime numbers under n are {}".format(primesundern ))
    st.text("There are {} prime numbers under n".format(len(primesundern)))

if(st.button('Find odd prime numbers under n')):
      
    # print the BMI INDEX
    st.text("The prime numbers under n are {}".format(primesundern ))
    st.text("There are {} prime numbers under n".format(len(primesundern)))



if(st.button('Find even prime numbers under n')):
      
    # print the BMI INDEX
    st.text("The prime numbers under n are {}".format(even_numbers(primesundern )))
    st.text("There are {} prime numbers under n".format(len(primesundern)))

if(st.button('Find prime numbers divisble by n under n')):
      
    # print the BMI INDEX
    st.text("The prime numbers under n are {}".format(primesundern ))
    st.text("There are {} prime numbers under n".format(len(primesundern)))

