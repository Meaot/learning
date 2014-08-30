# This is a simple script I wrote to perform a few simple manipulations on a DNA
# sequence file, assuming the sequence is in the correct format. More improvements
# are needed. Mostly a learning exercise.

from sys import exit

print 'Warning! The source FASTA file must be in the same directory as this script!'

in_file_name = raw_input('What is the file name?\n')
inFile = open(in_file_name, 'r')

prompt = raw_input('What would you line to do? \nTo convert the provided file to \
the antiparallel strand, enter \'antiparallel\'. \nTo reverse the provided file, enter \
\'reverse\'.To cancel, enter \'cancel\'\n')

if type(prompt) != str or prompt not in ('antiparallel', 'reverse', 'cancel'):
	print 'Error! Improper input. Enter one of the specified inputs.'
	exit()

if prompt == 'cancel':
	exit()

def make_continuous():
	result = inFile.read().replace('\n', '')
	return result
	
def reverse_file():
	result = ''.join(reversed(make_continuous()))
	return result

def make_antiparallel():
	uppered = reverse_file().upper()
	a_to_x = uppered.replace('A', 'x')
	c_to_y = a_to_x.replace('C', 'y')
	t_to_a = c_to_y.replace('T', 'A')
	g_to_c = t_to_a.replace('G', 'C')
 	x_to_t = g_to_c.replace('x', 'T')
	result = x_to_t.replace('y', 'G')
	return result

if prompt == 'reverse':
	result = reverse_file()

if prompt == 'antiparallel':
	result = make_antiparallel()

out_file_name = raw_input('What should the output file be named?\n')
outFile = open(out_file_name, 'w')
outFile.write(result)