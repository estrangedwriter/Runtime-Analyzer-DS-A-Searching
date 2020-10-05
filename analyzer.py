import random
from algorithms import bisection_iter, bisection_recur
import time

def create_random_email():
    pass


def create_random_email_list():
    pass


def analyze_func(func_name, n, arr):
    tic = time.time()
    func_name(n, arr)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()} --> Elapsed time: {seconds:.5f}")

def main_script():
    size = int(input("How many emails would you like to create?: "))
    search_query = input("Which email address would you like to search for?:")

random_email_list = ['a','b','c','d','e','f','h']

analyze_func(bisection_iter,'a', random_email_list)