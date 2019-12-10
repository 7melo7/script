import argparse
import pymysql
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
	A script used for storing FASTA sequence data into mysql table.
	Author : S1MPLE
	""", formatter_class=RawTextHelpFormatter)
parser.add_argument("-f", "--fasta", type=str, help="FASTA format sequence file", default=None)
parser.add_argument("-ht", "--host", type=str, help="MySQL host",default="localhost")
parser.add_argument("-u","--user", type=str, help="MySQL username" ,default="root")
parser.add_argument("-p", "--pwd", type=str, help="MySQL password", default="12345678")
parser.add_argument("-db", "--db", type=str, help="MySQL database name",default=None)
parser.add_argument("-t", "--table", type=str, help="table that stores sequence data",default=None)
args = parser.parse_args()

def read_fasta(filename):
	fasta = {}
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			if line.startswith('>'):
				seq_id = line[1:]
				if seq_id not in fasta.keys():
					fasta[seq_id] = ""
					continue
			fasta[seq_id] += line
	return fasta

def seq_2_mysql(host, user, pwd, db, seqs, table):
	db = pymysql.connect(host, user, pwd, db)
	cursor = db.cursor()
	i, f = 0, 0
	try:
		for k,v in seqs.items():
			sql = "INSERT INTO %s(gene_id, sequence) VALUES ('%s', '%s')" % (table, k, v)
			cursor.execute(sql)
			i += 1
		db.commit()
		f = 1
	except Exception as e:
		print(str(e))
		db.rollback()
	db.close()
	if f == 1:
		print("%d squences has been stored into mysql" % i)


if __name__ == "__main__":
	seqs = read_fasta(args.fasta)
	print("%d sequences loaded from fasta file." % len(seqs))
	seq_2_mysql(args.host, args.user, args.pwd, args.db, seqs, args.table)
	print("script done!")
