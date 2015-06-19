#getting input from the terminal and performing comparison operators
import sys, getopt #methods used to get command line arguments

def main(argv):
	_Op1=0
	_Op2=0

#---------------------------------
#------try catch part-------------

try:
	opts,args = getopt.getopt(argv,"hi:o",["_Op1=","_Op2="])

#exception goes here

except getopt.GetoptError:
	print "Error in Input"
	sys.exit(2)


#loop through command line arguments
	for opt,arg in opts:
		if opt == '-h':
			print "Helper"
			sys.exit(2);
		elif opt in ("-i", "--_Op1"):			
			_Op1=arg
		elif opt in ("-o", "--_Op2"):
			_Op2=arg
			print "Operator 1", _Op1
			print "Operator 2", _Op2



	



