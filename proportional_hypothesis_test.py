#!/usr/bin/env python3.6

import pandas as pd
import numpy as np
import scipy
from scipy import stats


def calculate_proportions_hypothesis_test(n_one, p_one_total, n_two, p_two_total,
                                          sideness, print_intermediate_steps):

    """

    Calculates the Hypothesis Test using Proportions. Overall layout of equations
    and analysis based on the PSU Education Info for Stat500 found at the following link:

    https://online.stat.psu.edu/stat500/book/export/html/573

    Param n_one: count of cases in group one
    Param p_one_total: total count in group one
    Param n_two: count of cases in group two
    Param p_two_total: total count in group two
    Param sideness: One or Two Sided P-Value Results
    Param print_intermediate_steps: Tells function to print intermediate steps for error checking

    Return p_value: Two sided p-value based on the z-score distribution

    """

    # Calculate group one proportions
    proportion_group_one = n_one / p_one_total
    # Print Intermediate Step
    if print_intermediate_steps in ["on", "ON", "On"]:
        print ("Group One Proportion is: " + str(proportion_group_one))

    # Calculate group two proportions
    proportion_group_two = n_two / p_two_total
    # Print Intermediate Step
    if print_intermediate_steps in ["on", "ON", "On"]:
        print ("Group Two Proportion is: " + str(proportion_group_two))

    # Calculate the p
    p_star = (n_one + n_two) / (p_one_total + p_two_total)
    # Print Intermediate Step
    if print_intermediate_steps in ["on", "ON", "On"]:
        print ("P-Star value is: " + str(p_star))


    ### Calculate the Z score of the Hypothesis Test ###
    # Calculate the numerator
    numerator_prop_diff = proportion_group_one - proportion_group_two

    # Calculate the denominator
    initial_denom_value = p_star * (1 - p_star) * (1/p_one_total + 1/p_two_total)
    denominator_value = np.sqrt(initial_denom_value)

    # Calculate the Z-Score from the Hypothesis Test
    z_score_value = numerator_prop_diff / denominator_value
    # Print Intermediate Step
    if print_intermediate_steps in ["on", "ON", "On"]:
        print ("The z-score is: " + str(z_score_value))


    ### Converts the Z-Score Value to a p-value using SciPy ###
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
    # Specifically utilizes a "Survival Function" when calculating p-value from
    # the Z-score distribution
    
    # Calculate p-value if one sided
    if sideness == "one-sided":
        p_value = scipy.stats.norm.sf(abs(z_score_value))

    # Two Sided P-Value from Z-score
    else:
        p_value = scipy.stats.norm.sf(abs(z_score_value))*2

    return (p_value)
                                          

def main():

    # Data/Equations for Example Based on PSU Stat Course at following link:
    # https://online.stat.psu.edu/stat500/book/export/html/573

    # Proportional Example Values from Example
    # Get Group One Results
    group_one_result = 52
    group_one_total = 69
    
    # Get Group Two Results
    group_two_result = 120
    group_two_total = 131

    # P-value result is two-sided
    sidness = "two-sided"

    # Tell Program to Print Intermediate Steps ('on'/'off')
    print_intermediate_steps = 'off'
    
    # Calculate the P-value for the Hypothesis Test of Two Proportions
    p_value = calculate_proportions_hypothesis_test(group_one_result, group_one_total, group_two_result,
                                                    group_two_total, sidness, print_intermediate_steps)

    print ("The two-sided p-value is: " + str(p_value))



main()  
