#!/usr/bin/env ${PYTHON}

import sys
import xhtml
import time
import string

def do_file(filename):

    fp = open(filename, "r")
    fj = open(filename + ".json", "w")
    print "<!-- This file automatically generated by mirrorfmt.py $Revision$ -->"
    print "<!-- DO NOT EDIT THIS FILE - edit the master file MIRRORS instead -->"
    print xhtml.dl.init({"class" : "download-mirror"})

    print >>fj, '"mirrors_http":[\n'

    for l in fp:
        l = l.rstrip()
        if len(l) > 1:
            if l[0] == "#":
                pass
            elif l[0] not in [' ', '\t', '\n']:
                print xhtml.dt(l)
            else:
                l = l.lstrip()
                idx = 0
                while idx < len(l) and l[idx] not in string.whitespace:
                    idx = idx + 1
                if idx < len(l):
                    # split the link (before whitespace) from the comment
                    print xhtml.dd(xhtml.hyperlink(l[0:idx], {"href" : l[0:idx]})
                                   + l[idx:len(l)])
                    if l.startswith("http"):
                        print >>fj, '"' + l[0:idx] + '",'
                else:
                    print xhtml.dd(xhtml.hyperlink(l, {"href" : l}))
                    if l.startswith("http"):
                        print >>fj, '"' + l[0:idx] + '",'
                pass
            pass
        pass

    print >>fj, "];"
    print xhtml.dl.fini()
    fp.close()
    fj.close()

    return

def main(argv):
    for a in argv:
        do_file(a)
        pass

    return

main(sys.argv[1:])