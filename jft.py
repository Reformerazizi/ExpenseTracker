dictCategory = [
    {'category': 'Business Analytics', 'count': 336},
    {'category': 'Data ethics', 'count': 389},
    {'category': 'visualization', 'count': 314},
    {'category': 'statistics', 'count': 428},
    {'category': 'NLP', 'count': 368},
    {'category': 'Language', 'count': 1},
    {'category': 'python', 'count': 373},
    {'category': 'maths', 'count': 379},
    {'category': 'deep learning', 'count': 364},
    {'category': 'SQL', 'count': 403},
    {'category': 'Python', 'count': 80},
    {'category': 'R Studio', 'count': 246},
    {'category': 'data science', 'count': 395},
    {'category': None, 'count': 0},
]

report_list_tuples = []
report_list = []
report = []
final_report = []

for i in range(0, len(dictCategory)-1):
    j = list(dictCategory[i].items())
    report_list_tuples.append(j)

for i in report_list_tuples:
    for item in i:
        report_list.append(item)

for i in report_list:
    for item in i:
        report.append(item)

i = 0
 
while(i<(len(report)-1)):
    final_report.append(report[i+1])
    i = i + 2
 
print(final_report)