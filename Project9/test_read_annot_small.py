
from proj09 import read_annot_file
import json

instructor = { '504900': {'bbox_list': [[0.0, 75.05, 393.36, 427.0],
   [0.0, 88.15, 461.89, 287.42],
   [54.78, 3.52, 640.0, 427.0]],
  'bbox_category_label': [18, 63, 1],
  'cap_list': ['a man sitting on a couch with a dog on his lap',
   'a man wearing glasses holds his dog in his lap',
   'a man with a dog on his lap.',
   'a man on a couch with a brown and white dog laying on top of it.',
   'a man and a brown and white dog sitting together.']},
 '161141': {'bbox_list': [[35.06, 263.95, 88.84, 291.13],
   [125.81, 162.37, 279.57, 463.48],
   [176.4, 0.0, 334.0, 379.78],
   [10.89, 191.89, 79.52, 252.94]],
  'bbox_category_label': [18, 2, 7, 2],
  'cap_list': ['a red bicycle with a basket on front next to a train.',
   'a red bike is leaning against a blue wall',
   'the bike is parked next to the broken down bus.',
   'a bicycle leans against a standing train car.',
   'a bike that is parked next to a building']},
 '210012': {'bbox_list': [[314.29, 209.0, 403.67, 280.19],
   [209.21, 106.34, 215.47, 119.10000000000001],
   [198.08, 97.72, 206.46, 121.0],
   [183.42, 38.62, 288.37, 281.59999999999997],
   [364.3, 204.82, 407.14, 218.35999999999999],
   [354.88, 107.87, 421.75, 141.3],
   [267.51, 98.91, 359.19, 253.15],
   [125.6, 131.24, 139.4, 145.37],
   [45.8, 137.87, 100.11, 151.92000000000002],
   [0.07, 130.0, 5.0200000000000005, 160.18],
   [0.12, 116.93, 20.630000000000003, 158.77],
   [105.91, 100.9, 126.11, 147.2],
   [210.78, 100.11, 213.27, 112.27],
   [185.95, 104.45, 197.23999999999998, 137.12],
   [203.54, 98.91, 209.44, 120.16],
   [57.98, 113.87, 92.58, 133.2]],
  'bbox_category_label': [18,
   44,
   44,
   1,
   51,
   78,
   79,
   47,
   51,
   86,
   86,
   44,
   44,
   44,
   44,
   51],
  'cap_list': ['a woman standing in a kitchen with hard wood floors.',
   'a woman fixes food in the kitchen while a cat sits behind her.',
   'a woman and a little dog in a very large kitchen.',
   'a person in a kitchen with a stove and cupboards',
   'a woman and a dog in her kitchen waiting as she prepares a meal']}}

fp = open("small.json")
student = read_annot_file(fp)
fp.close()

print("Instructor:")
print(instructor)
print("\nStudent:")
print(student)
assert student == instructor
