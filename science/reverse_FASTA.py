# This is a simple script that automates stripping whitespace from text (for example
# with pasted text) and reversing the sequence of characters. I wrote it to invert
# sequence data read from a reverse primer.

print 'Warning! The source FASTA file must be in the same directory as this script!'

in_file_name = raw_input('What is the file name? ')
inFile = open(in_file_name, 'r')

continuous = inFile.read().replace('\n', '')
inverse = ''.join(reversed(continuous))

out_file_name = raw_input('What should the output file be named? ')
outFile = open(out_file_name, 'w')
outFile.write(inverse)