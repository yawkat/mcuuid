#!/usr/bin/env python

import yaml
import sys
import re

infile = sys.argv[1]
outfile = sys.argv[2]

doc = yaml.load(open(infile))

to_convert = []

for e in doc.keys():
    if re.match("\w{8}(-\w{4}){4}\w{8}", e):
        to_convert.append(e)

for c in to_convert:
    data = doc.pop(c)
    if not "options" in data:
        print "Skipping %s, no name found!" % c
        continue
    name = data["options"]["name"]
    data["options"].pop("name")
    if data["options"] == {}:
        data.pop("options")
    doc[name] = data

indent = "  "
with open(outfile, "w") as w:
    for l in yaml.dump(doc, default_flow_style=False).split("\n"):
        w.write("  " + l + "\n")