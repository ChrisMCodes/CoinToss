#!/usr/bin/env
#
#
# Purpose: performs a simulation of coin tosses
# to use empirical data
# to demonstrate the law of large numbers.
#
# Last update: 2020-06-18

# Uses random package to choose heads or tails
import random

def coin_flip(trials, my_data):
    '''randomizes 0 and 1 'trials' times'''
    my_data += [random.randint(0, 1) for i in range(0, trials)]
    return my_data

def get_vals(my_data, my_dict):
    '''compiles my_data into a dictionary, 0 and 1 are keys, count of each are values'''
    for data in my_data:
        if data in my_dict:
            my_dict[data] += 1
        else:
            my_dict[data] = 1
    return my_dict

def show_results(my_data, my_dict):
    '''prints out percentages. Here, we'll call 0 heads and 1 tails'''
    # some local variables to handle counts
    heads = my_dict[0] / (my_dict[0] + my_dict[1]) * 100
    tails = my_dict[1] / (my_dict[0] + my_dict[1]) * 100
    trials = len(my_data)
    variance = 0
    
    if heads > 50:
        variance = heads - 50
    else:
        variance = tails - 50

    # print("Heads: {:.3f}%, tails: {:.3f}%  for a total variance from 50% of {:.3f}% in a trial of {}.".format(heads, tails, variance, trials)) # This can be commented out if you don't want it
    
    return variance


# A sample test

def test_it(num):
    '''This function was added for my test purposes only'''
    max_variance = 0
    current_variance = 0

    # iterates through num flips x times
    for i in range(0, 10):
        my_data          = [] 
        my_dict          = {}
        my_data          = coin_flip(num, my_data)
        my_dict          = get_vals(my_data, my_dict)
        current_variance = show_results(my_data, my_dict)
        if current_variance > max_variance:
            max_variance = current_variance

    # prints how far the results of this round varied from an even 50/50 split.
    # for example, if you flipped 9 heads and 1 tail, that's a 90% max variance.
    print("In 10 trials of {} flips each, the max variance from a 50/50 split was: {:.3f}%.".format(num, max_variance))
    pass

# calling my test_it function with multiples of 10 flips
test_it(10)
test_it(100)
test_it(1000)
test_it(10000)
test_it(100000)
    
