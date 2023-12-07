#!/usr/bin/python3

# SeqIO from Biopython was imported to aid in converting the FASTQ file to FASTA

from Bio import SeqIO

# the original FASTQ is opened while a new file with .fasta extension is created in write mode
# line is parsed with SeqIO.parse() using for loop
# SeqIO.write() used to convert each line to FASTA format

with open("SRS301869.denovo_duplicates_marked.trimmed.1.fastq", "r") as fastq_file:
    with open("SRS301869.denovo_duplicates_marked.trimmed.1.fasta", "w") as fasta_file:
        for line in SeqIO.parse(fastq_file, "fastq"):
            SeqIO.write(line, fasta_file, "fasta")
