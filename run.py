import sumy
import os
import sys
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lsa import LsaSummarizer

#import the file
if len(sys.argv) > 1:
	file = sys.argv[1]
	if file.endswith('.txt') or file.endswith('.doc') or file.endswith('.docx'):
		exists = os.path.isfile(file)
	else:
		print("Please enter a valid file")
		print("Only accepted txt/doc/docx as file extensions")
		exit()
	if not exists:
		file = "refer.txt"
else:
	file = "refer.txt"

#tokenize the file
parser = PlaintextParser.from_file(file, Tokenizer("english"))

# Check the number of characters in the string to understand the reduction
text  = open(file, "r")
count = len((text.read()).split())

if count == 0:
	print("No content present")
	exit()
# Calculate lines
if count > 10000:
	lines = 100
else:
	for i in range(10):
		if i == 0:
			continue
		if count > i * 1000 and count < (i+1) * 1000:
			lines = 20 + (i * 10)

#LexRank model
summarizer = LexRankSummarizer()

#Luhn model
# summarizer = LuhnSummarizer()

#LSA model
# summarizer = LsaSummarizer()

summary = summarizer(parser.document,lines)

for sentence in summary:
	print(sentence)