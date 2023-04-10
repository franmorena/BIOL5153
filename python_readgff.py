#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser Object 
parser = argparse.ArgumentParser(description="this script prints SBASH script with passed parameters/argument and options")

# add positional (required) arguments
parser.add_argument("gff_file", help="file name", type=str)
parser.ass_argument ("fasta_file", help="corresponding FASTA file", type=str)

# parse arguments
args = parser.parse_args()

# commands here 
gff_file = open(args.gff_file, "r") #r means read

gff_lines = gff_file.readlines()

