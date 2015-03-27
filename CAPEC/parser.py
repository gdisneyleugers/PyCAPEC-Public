__author__ = 'gdl'
import xml.etree.ElementTree as ET
import json
import os

def get_pretty_print(json_object):
    return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))


def log(logfile, data):
    logger = file(logfile, 'a')
    logger.write(data)
    logger.close()


def capec_search(search):
    f = file('term', 'w')
    f.write(search)
    f.close()
    tree = ET.parse('capec.xml')
    purge = file("{0}.gv".format(search), "w")
    purge.close()
    root = tree.getroot()
    counter = 0
    for child in root:
        for node in child:
            if search in str(node.attrib):
                tick = counter + 1
                counter = tick
                format_cpec = get_pretty_print(node.attrib)
                print "|===========================================|"
                print "CAPEC: " + format_cpec.strip('{}')
                log(logfile="pycapec.log", data="CAPEC:" + format_cpec)
                graph = file("{0}.gv".format(search), "a")
                cp = format_cpec.replace('{}', '[]')
                cd = cp.replace(',','')
                cc = cd.replace(':',' -> ')
                if counter == 1:
                    graph.write("// {0}".format(search))
                    graph.write("\ndigraph{ ")
                else:
                    pass
                graph.write(cc.strip('{}').replace('ID', 'CAPEC'))
                #aa = open('tm-id', 'r').readlines()
                #for line in aa:
                    #graph.write(cc.strip('{}\n').replace('ID', 'CWE').replace('Name', line).strip('\n'))
                    #aa = open('tm-id', 'r').readline()
                graph.close()

def cwe_search(search):
    tree = ET.parse('cwec.xml')
    root = tree.getroot()
    counter = 0
    for child in root:
        for node in child:
            if search in str(node.attrib):
                tick = counter + 1
                counter = tick
                format_cwe = get_pretty_print(node.attrib)
                print "|===========================================|"
                print "CWE: " + format_cwe.strip('{}')
                log(logfile="pycapec.log", data="CWE: " + format_cwe)
                graph = file("{0}.gv".format(search), "a")
                cp = format_cwe.replace('{}', '[]')
                cd = cp.replace(',','')
                cc = cd.replace(':',' -> ')
                graph.write(cc.strip('{}').replace('ID', 'CWE'))
                #os.system('rm tm-id & touch tm-id')
                #os.system('/usr/local/bin/name2id.sh {0}.gv'.format(search))
                #aa = open('tm-id', 'r').readlines()
                #for line in aa:
                #graph.write(cc.strip('\n').replace('ID', 'CWE'))
                #aa = open('tm-id', 'r').readline()
            else:
                pass
    graph = file("{0}.gv".format(search), "a")
    graph.write('}'.strip("\n"))
    graph.close()
