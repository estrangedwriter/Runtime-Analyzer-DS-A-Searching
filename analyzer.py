import random
from algorithms import bisection_iter, bisection_recur
import time

def create_random_email():
    random_email = ""
    domain_names = ["@yahoo.com", "@hotmail.com", "@gmail.com"]
    
    for i in range(0, random.randint(6, 15)):
        char = chr(random.randint(97,122))
        random_email = random_email + char
    
    randomint = random.randint(0,2)
    random_email = random_email + domain_names[randomint]

    return random_email


def create_random_email_list(number):
    email_list = []
    print("\nGenerating random list of emails...")
    
    tic = time.time()
    
    for i in range(number):    
        email_list.append(create_random_email())
    
    toc = time.time()
    seconds = toc - tic

    print(f"Time elapsed:----------------------->    {seconds:.5f}")

    tic1 = time.time()
    sorted(email_list)
    toc1 = time.time()
    seconds = toc1 - tic1
    print(f"Time to sort the email list:-------->    {seconds:.5f}\n")


    return email_list    
    


def analyze_func(func_name, n, arr):
    print("*" * 40)
    
    tic = time.time()
    print(func_name(n, arr))
    toc = time.time()
    
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()} Elapsed time: ------->    {seconds:.5f}")
    print("\n")
    print("*" * 40)

def main_script():
    size = int(input("How many emails would you like to create?: "))
    search_query = input("Which email address would you like to search for?: ")

    email_list = create_random_email_list(size)
    email_list.append(search_query)
    email_list = sorted(email_list)

    analyze_func(bisection_iter, search_query, email_list)
    
    tic = time.time()
    print(bisection_recur(search_query, email_list, 0, size))
    toc = time.time()

    seconds = toc - tic
    print(f"Bisection_recur Elapsed time: ------->   {seconds:.5f}")
    print("\n")
    print("*" * 40)

main_script()

