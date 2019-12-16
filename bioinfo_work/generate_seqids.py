#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
	This script is used to generate seqids for MCScan analysis.
	Author : Simple
	Example: ./generate_seqids.py -i ath.bed -o seqids --bed -n 50""", formatter_class=RawTextHelpFormatter
)
parser.add_argument("-i", type=str, help="input file", default=None, dest="input_file")
parser.add_argument("-o", type=str, help="output file, default: seqids", default="seqids", dest="output_file")
parser.add_argument("--bed", help="input bed file", action="store_true", default=True, dest="bed")
parser.add_argument("-n", type=int, help="longest scaffold/chromsome counts to output, defalut: 50", default=50, dest="n")
args = parser.parse_args()

def in_bed_out(filename):
	beds = []
	with open(filename, 'r') as f:
		for i in f.readlines():
			beds.append(i.strip('\n'))
	scaffold_dict = {}
	for i in beds:
		bed_oneline = i.split('\t')
		if bed_oneline[0] in scaffold_dict.keys():
			if scaffold_dict[bed_oneline[0]] < int(bed_oneline[1]): scaffold_dict[bed_oneline[0]] = int(bed_oneline[1])
		else:
			scaffold_dict[bed_oneline[0]] = int(bed_oneline[1])
	scaffold_list = sorted(scaffold_dict.items(), key=lambda d:d[1], reverse = True)
	return scaffold_list

def write_in(filename, scaffold_list, n):
	with open(filename, "a") as f:
		seqids_str = ""
		for i in range(n):
			seqids_str += scaffold_list[i][0] + ","
		f.write(seqids_str[:-2] + "\n")

if __name__ == "__main__":
	scaffold_list = in_bed_out(args.input_file)
	write_in(args.output_file, scaffold_list, args.n)