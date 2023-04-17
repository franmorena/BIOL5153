#! /usr/bin/env python3

# import modules
import argparse
import csv 
from Bio import SeqIO

# create an ArgumentParser Object 
parser = argparse.ArgumentParser(description="this script prints SBASH script with passed parameters/argument and options")

# add positional (required) arguments
parser.add_argument("gff_file", help="gff file name", type=str)
parser.add_argument ("fasta_file", help="corresponding FASTA file name", type=str)

# parse arguments
# access argument values via `args` variable
args = parser.parse_args()

# read in the FASTA file

genome = SeqIO.read(args.fasta_file, "fasta")
print(genome.seq) 

# open files and read lines - line by line
# gff_file = open(args.gff_file, "r")
# gff_lines = gff_file.readlines()
# gff_lines.remove(gff_lines[-1])
# gff_file.close()
 
# loop over all the lines in the file with for loop - remove `#` if for loop is desired
# for line in gff_lines: 
		# print(line)
		# strip_line = line.strip()
		# split_line = strip_line.split('\t')
		# feature_len = int(split_line[4])  - int(split_line[3]) # 5th (end position) - 4th (start position) column to find length of each feature
		# print(feature_len)
		
# open the gff file
with open(args.gff_file) as gff:

	# create a csv reader object
	reader = csv.reader(gff, delimiter='\t')
	
	# loop over all the lines in the file with `with`
	for line in reader:
	
		# skip blank line
		if not line:
			continue
			
		# else it's not blank
		else: #you don't need the else if you use csv bc it strips it for you, you can leave it here for aesthetics/readability, it won't hurt the script
			# line = line.rstrip() # rstrip removes the blank space on the right (beginning of the line) 
								# and .lstrip removes the blank space on the left (end of the line)
			
		# split line on tab character
			# columns = line.split('\t') 
	
		# give variables names to the line variable | it was column before  
			organism = line[0]
			source = line[1]
			feature_type = line[2]
			start = int(line[3])
			end = int(line[4])
			
			# add the length to column 5
			line[5] = str(end - start +1)
			
			length = line[5]
			strand = line[6]
			attributes = line[8]
		
		
		# joint in a character 
			new_line = '\t'.join(line)
			#print(new_line)

		# extract each feature in the genome 
			feature_seq = genome.seq[start-1:end]
			
		# check if the length match with the previous calculated length 
			#print(len(feature_seq) - ((end-start)+1))
			
		# print FASTA output for this sequence
			print(">" + organism, feature_type, attributes)
			print(feature_seq)

