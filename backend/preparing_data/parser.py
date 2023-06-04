#!/usr/bin/env python3
from PyPDF2 import PdfReader
import csv, sys, os, re
import shutil

TYPE=os.getenv("TYPE")

class BookParser:
	def __init__(self, path_to_file):
		self.file = path_to_file

	def parse_page(self, text):
		i = 0
		for line in text.split('\n\n'):
			print('line: {}'.format(i))
			print(line)
			i += 1

	def save_to_csv(self, paragraphs):
		with open(TYPE+'.csv', 'a') as f:
		#with open('test.csv', 'a') as f:
			w = csv.writer(f)
			for pp in paragraphs:
				w.writerow([TYPE, pp])

	def parse_paragraph(self, pp):
		pattern = r'[^a-zA-Z.,\s]'
		if len(pp) < 150:
			return None, False
		pp = pp.strip()
		pp = re.sub(pattern, '', pp)
		pp = re.sub(r'\s+', ' ', pp)
		if len(pp) > 512:
			pp = pp[:513]
		idx = pp.rfind('.')
		pp = pp[:idx+1]
		if len(pp) == 0: return None, False
		else: return pp, True

	def parse_txt(self):
		paragraphs = []
		with open(self.file, 'r', encoding='utf-8-sig') as f:
			for line in f.read().split('\n\n'):
				pp, keep = self.parse_paragraph(line)
				if not keep:
					continue
				paragraphs.append(pp)
		#paragraphs = paragraphs[5:-5]
		self.save_to_csv(paragraphs)

	def parse_pdf(self, replace=False):
		pass

	def parse(self):
		if self.file[:-4] == '.pdf':
			self.parse_pdf()
		else:
			self.parse_txt()

	

if __name__ == '__main__':
	assert (TYPE is not None) and (len(sys.argv) == 2)
	#shutil.copy2('test.csv', '/tmp/test.csv')
	bp = BookParser(sys.argv[1])
	bp.parse_txt()

