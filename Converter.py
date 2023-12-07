#!/usr/bin/python3

# SeqIO from Biopython was imported to aid in converting the FASTQ file to FASTA
import sys
from Bio import SeqIO

original_file = sys.argv[1]
converted_file = sys.argv[2]

# the original FASTQ is opened while a new file with .fasta extension is created in write mode
# line is parsed with SeqIO.parse() using for loop
# SeqIO.write() used to convert each line to FASTA format

with open(original_file, "r") as fastq_file:
    with open(converted_file, "w") as fasta_file:
        for line in SeqIO.parse(fastq_file, "fastq"):
            SeqIO.write(line, fasta_file, "fasta")
