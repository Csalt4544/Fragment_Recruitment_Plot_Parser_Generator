#!/usr/bin/python3

# this script will utilize the matplotlib library to generate FRPs
# several modules are imported: matplotlib, re, and sys

import matplotlib.pyplot as plt
import re
import sys

# argument from command line should be a .sam file through if/else statement
# if not, program issues a non-.sam statement and closes program

file_name = sys.argv[1]

# if the file is in .sam format, if/else used to determine whether line is an alignment
# parsing method by stripping and splitting lines based on tab-delimited spacing
# CIGAR value for total matches and position obtained from initial splitting of alignment
# MD line is split further to obtain only number values that can be used as integers for sum
# commented-out print statement to stdout to test values obtained
# banded conditionals for position and percent identity used to prevent too much plotting in matplotlib
# these conditionals are based on the x-axis dimensions of the plot
# plt.plot() used to plot one point on graph for each alignment line

if re.search(r"\.sam", file_name):
    for line in open(file_name):
        if line.startswith("@"):
            pass
        else:
            line = line.strip()
            columns = re.split(r"\t", line)
            position = ((int(columns[3])) / 1000)
            cigar = re.search("[0-9][0-9]M", columns[5])
            cigar_value = re.match("[0-9][0-9]", cigar.group())
            int_cigar_value = int(cigar_value[0])
            field_MD = (columns[12])
            match_plus_mismatch = re.split(":", field_MD)
            only_matches = re.split("[A-Z]", match_plus_mismatch[2])
            sum_matches = 0
            int_value = 0
            for item in only_matches:
                int_value = int(item)
                sum_matches += int_value
            percent_identity = ((sum_matches / int_cigar_value)*100)
            # print("X-axis = {0}, Y-axis = {1}%".format(columns[3], percent_identity))
            if (250 < position < 500) and (40 < percent_identity < 100):
                plt.plot(position, percent_identity, "bo", markersize=1)

    # plot diagram parameters are declared including scale and labels
    # if desired, values within the plt.axis() line can be changed to scale the plot differently

    plt.axis((250, 500, 40, 100))
    plt.xlabel("Position in the Genome (kb)")
    plt.ylabel("Percent Identity (%)")
    plt.title("{0}".format(file_name))
    plt.show()

else:
    print("Your file is not in .sam format.")
    print("Please convert your alignment data into a .sam file to use this program.")

print("Program now quitting.")
