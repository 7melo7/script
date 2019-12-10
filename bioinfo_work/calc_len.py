import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
	This script is used for calculate the length of sequence of FASTA data.
	Author : S1mple""", formatter_class=RawTextHelpFormatter
)
parser.add_argument("-f", type=str, help="FASTA file",default=None)
parser.add_argument("-o", "-out", type=str, help="output filename",default="length.tsv")
args = parser.parse_args()

def read_fasta(filename):
	fasta = {}
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			if line.startswith(">"):
				sequence_name = line[1:]
				if sequence_name not in fasta:
					fasta[sequence_name] = ""
				continue
			sequence = line
			fasta[sequence_name] += sequence
	return fasta

def write_length(filename, fasta):
	with open(filename, 'w') as f:
		for key, value in fasta.items():
			f.write(key+'\t'+str(len(value))+'\n')


if __name__ == "__main__":
	fasta = read_fasta(args.fasta)
	write_length(args.out, fasta)

