__author__ = 'gdl'
from CAPEC import parser,Data
import os
s=raw_input("Search: ")

print "|===========================================|"
print "  CAPEC: "
capec = parser.capec_search(s)
print "|===========================================|"
print "  CWE: "
cwe = parser.cwe_search(s)
print "|===========================================|"
#os.system('./name2id.sh {0}.gv'.format(s))
# Decied to run this through shell script rather than python
