__author__ = 'gdl'
import os
import CAPEC.parser as form
def setter(gv_file):
    os.popen("./name2id.sh {0}".format(gv_file))
    fh = file('tm-id', 'r')
    h = fh.readlines()
    for line in h:
        form.get_pretty_print()
