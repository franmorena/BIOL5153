#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser Object 
parser = argparse.ArgumentParser(description="this script prints SBASH script with passed parameters/argument and options")

# add positional (required) arguments
parser.add_argument("gff_file", help="gff file name", type=str)
parser.add_argument ("fasta_file", help="corresponding FASTA file name", type=str)

# parse arguments
args = parser.parse_args()

# commands here 

# open files and read lines - line by line
gff_file = open(args.gff_file, "r")
gff_lines = gff_file.readlines()
gff_lines.remove(gff_lines[-1])
gff_file.close()
 
for line in gff_lines: # loop over all the lines in the file 
		# print(line)
		strip_line = line.strip()
		split_line = strip_line.split('\t')
		feature_len = int(split_line[4])  - int(split_line[3]) # 5th - 4th column to find length of each feature
		print(feature_len)
	

