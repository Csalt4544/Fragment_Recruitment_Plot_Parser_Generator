#!/usr/bin/python3

# this script will utilize the matplotlib library to generate one composite FRP for a metagenomic sample
# several modules are imported: matplotlib, sys, and the second .py script

import matplotlib.pyplot as plt
import sys
import sop_processing_v2

# command line arguments are stored within the array seen below
# if needed a larger/dynamic array could be utilized for more reference genomes

files = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
graph_title = sys.argv[5]

# to differentiate between reference genome plot points, the RGB version of color was used in Matplotlib
# initial values of 0.0 for each color correspond to black
# after each reference genome, values are updated gradually at different rates

red = (0.0)
green = (0.60)
blue = (0.10)

# similar set up to the first and second .py scripts but split up
# a processing .script defining the class Line() was created to avoid repeating functions/methods/etc.
# objects are created based on the file name
# conditional bounds were changed since many plot points will be present

for file in files:
    for line in open(file):
        values = sop_processing_v2.Line(line)
        genome_position = values.position()
        recruit_percent_identity = values.percent_identity()
        if (300 < genome_position < 400) and (40 < recruit_percent_identity < 100):
            plt.plot(genome_position, recruit_percent_identity, marker="o",
                     color=(red, green, blue), markersize=1, label=file)
        # print(genome_position)
        # print(recruit_percent_identity)
    # red += (0.2)
    green -= (0.15)
    blue *= (2)

plt.axis((300, 400, 40, 100))
plt.xlabel("Position in the Genome (kb)")
plt.ylabel("Percent Identity (%)")
plt.title(graph_title)
# plt.legend()
plt.show()
