420-SN1-RE - PROGRAMMING IN SCIENCE
Prepared by: Hanif Azhar
Lab 8 - Functions and Conditional Logic (FASTA)
Concept Summary
Define reusable functions for parsing FASTA files and computing sequence statistics; use conditional logic and comprehensions.
Step-by-step Instructions (for students)
1.	Download Gene Sequences (FASTA) from NCBI GenBank into your working folder (see Appendix A below)
2.	Create lab8.py.
3.	Implement a read_fasta() function that returns a dictionary of header->sequence.
4.	Implement base_percentages(seq) that returns the percentage of A,T,G,C.
5.	Test functions on a any FASTA sample files and print results.
Tasks
•	Write a function to parse a FASTA file and return sequences keyed by header.
•	Write a function to calculate nucleotide percentages for a given sequence.
Exercises (with immediate solutions)
6.	Write read_fasta(filename) to return a dict of header->sequence for a FASTA file.
def read_fasta(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    header = lines[0].strip()
    sequence = ''.join(line.strip() for line in lines[1:])
    return header, sequence
header, dna_seq = read_fasta(r"C:\Users\azharh\Downloads\sequence.fasta")
print(header)
print(dna_seq[:100])  # print first 100 bases

7.	Write base_percentages(seq) that returns the percentage of each base (A,T,G,C).
def base_percentages(seq):
    seq = seq.upper()
    return {b: seq.count(b)/len(seq)*100 for b in 'ATGC'}

print(base_percentages('ATGCATGC'))


Appendix :A
How to Access and Download Gene Sequences (FASTA) from NCBI GenBank
Step 1 — Go to GenBank Search
1.	Open your browser and go to:
🔗 https://www.ncbi.nlm.nih.gov/genbank/
2.	In the search bar at the top, make sure it’s set to “Nucleotide”.
3.	Type the gene name or organism you want.
Examples:
o	BRCA1 human
o	ATP synthase E. coli
o	hemoglobin beta chain
Step 2 — Choose a Record
1.	Click on a search result that matches your gene.
You’ll be taken to a GenBank record page.
2.	You’ll see sections like:
o	LOCUS
o	DEFINITION
o	ACCESSION
o	ORIGIN (the actual DNA bases)
Step 3 — Get the FASTA Format
1.	At the top right of the gene record page, look for the “Send to” button.
2.	Choose:
o	Destination: File
o	Format: FASTA
3.	Click Create File or Download — this saves a .fasta file to your computer.
Step 4 — Sample FASTA Format
Here’s how a FASTA file looks:
>NM_000518.5 Homo sapiens hemoglobin subunit beta (HBB), mRNA
ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTG
GATGAAGTTGGTGGTGAGGCCCTGGGCAG...
•	The first line (starts with >) is the header, containing gene ID and description.
•	All other lines are the DNA sequence.
Appendix :B
How to fix file read error:
In Python, backslashes (\) are used for escape sequences — like:
•	\n → newline
•	\t → tab
•	\U → start of a Unicode escape (which expects 8 hex digits after it)
When Python sees:
C:\Users\azharh\Downloads\sequence.fasta
it interprets \U as the start of a Unicode escape — which causes the “unicodeescape” error.

Option 1 — Use a Raw String (Recommended)
Prefix the string with an r, which tells Python not to interpret backslashes:
header, dna_seq = read_fasta(r"C:\Users\azharh\Downloads\sequence.fasta")
Option 2 — Use Forward Slashes
Python accepts forward slashes (/) in file paths, even on Windows:
header, dna_seq = read_fasta("C:/Users/azharh/Downloads/sequence.fasta")
Option 3 — Escape Every Backslash
If you prefer backslashes, you must double each one:
header, dna_seq = read_fasta("C:\\Users\\azharh\\Downloads\\sequence.fasta")

