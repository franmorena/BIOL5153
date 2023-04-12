#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser Object 
parser = argparse.ArgumentParser(description="this script prints SBASH script with passed parameters/argument and options")

# add positional (required) arguments
parser.add_argument("gff_file", help="gff file name", type=str)
parser.add_argument ("fasta_file", help="corresponding FASTA file name", type=str)

# parse arguments
# access argument values via `args` variable
args = parser.parse_args()

# commands here 

# open files and read lines - line by line
gff_file = open(args.gff_file, "r")
gff_lines = gff_file.readlines()
gff_lines.remove(gff_lines[-1])
gff_file.close()
 
# loop over all the lines in the file with for loop - remove `#` if for loop is desired
# for line in gff_lines: 
		# print(line)
		# strip_line = line.strip()
		# split_line = strip_line.split('\t')
		# feature_len = int(split_line[4])  - int(split_line[3]) # 5th (end position) - 4th (start position) column to find length of each feature
		# print(feature_len)
		
# open the gff file
with open(args.gff_file) as gff:

	# loop over all the lines in the file with `with`
	for line in gff:
	
		# skip blank line
		if not line.strip():
			continue
			
		# else it's not blank
		else: 
			line = line.rstrip() # rstrip removes the blank space on the right (beginning of the line) 
								# and .lstrip removes the blank space on the left (end of the line)
			
		# split line on tab character
			columns = line.split('\t') 
	
		#give variables names to the columns 
			organism = columns[0]
			source = columns[1]
			feature_type = columns[2]
			start = int(columns[3])
			end = int(columns[4])
			length = columns[5]
			strand = columns[6]
			attributes = columns[8]
		
		# add the length to column 5
			columns[5] = str(end - start +1)
		
		# joint in a character 
			new_line = '\t'.join(columns)
		
			print(new_line)



