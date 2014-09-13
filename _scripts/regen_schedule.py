#!/usr/bin/python

# HOW TO USE THIS SCRIPT
# 1) run it, redirecting its output to schedule.html (i.e. `./regen_schedule.py > schedule.html`)
# 2) push changes
# 3) there is no step 3

import csv
from urllib2 import urlopen

rooms = []
keys = ["name", "type", "projector", "1000", "1100", "1330", "1430", "1600", "1700"]

f = urlopen("https://docs.google.com/a/pdx.edu/spreadsheets/d/1dWyyn8Qiq1fvnXCovfUUSeucMTM7CVfr7GwsWOJX29I/export?format=tsv&id=1dWyyn8Qiq1fvnXCovfUUSeucMTM7CVfr7GwsWOJX29I&gid=0")
tsv = csv.reader(f, delimiter='\t')
tsv.next() # skip the header row
for row in tsv:
    rooms.append(dict(zip(keys, row)))
f.close()

print("""---
layout: schedule
title: Schedule
section: schedule
---

<table class="table table-hover">
  <tr>
    <th>
      Room
    </th>
    <th>
      Session 1
    </th>
    <th>
      Session 2
    </th>
    <th class="bg-warning">
      Lunch
    </th>
    <th>
      Session 3
    </th>
    <th>
      Session 4
    </th>
    <th class="bg-warning">
      Break
    </th>
    <th>
      Session 5
    </th>
    <th>
      Session 6
    </th>
  </tr>""")

for room in rooms:
    print("""  <tr>
    <th>
      <strong>
        {name}
      </strong>
      </br>
      <small>
        {type}
      </small>
      <br>
      <span class="badge">{projector}</span>
    </th>""".format(name=room["name"], type=room["type"], projector=room["projector"]))
    for key in ["1000", "1100"]:
        if not room[key]:
            room[key] = "TBD"
        print("    <td><h4>{0}</h4></td>".format(room[key]))
    print("""    <td class="bg-warning">
      Lunch
    </td>""")
    for key in ["1330", "1430"]:
        if not room[key]:
            room[key] = "TBD"
        print("    <td><h4>{0}</h4></td>".format(room[key]))
    print("""    <td class="bg-warning">
      Break
    </td>""")
    for key in ["1600", "1700"]:
        if not room[key]:
            room[key] = "TBD"
        print("    <td><h4>{0}</h4></td>".format(room[key]))
    print("  </tr>")

print("</table>")
