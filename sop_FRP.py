#!/usr/bin/python3

# this script will utilize the matplotlib library to generate FRPs
# several modules are imported: matplotlib, re, and sys

import matplotlib.pyplot as plt
import re
import sys

# argument from command line should be a .sop file through if/else statement
# if not, program issues a non-.sop statement and closes program
# file name is processed to remove file extension and replace "_" with white space

file_name_raw = sys.argv[1]
file_name_title = re.split(r"\.", file_name_raw)
file_name = file_name_title[0].replace("_", " ")

# if the file is in .sop format, if/else used to determine whether line is an alignment
# parsing method by stripping and splitting lines based on tab-delimited spacing
# regex is used to obtain information on position and percent identity provided in .sop file
# banded conditionals for position and percent identity used to prevent too much plotting in matplotlib
# these conditionals are based on the x-axis dimensions of the plot
# plt.plot() used to plot one point on graph for each alignment line

if re.search(r"\.sop", file_name_raw):
    for line in open(file_name_raw):
        line = line.strip()
        columns = re.split(r"\t", line)
        percent_identity_columns = re.split("%", columns[7])
        percent_identity_value = float(percent_identity_columns[0])
        alignment_position_begin = (int(columns[9]) / 1000)
        if (250 < alignment_position_begin < 500) and (40 < percent_identity_value < 100):
            plt.plot(alignment_position_begin, percent_identity_value, "bo", markersize=1)

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
