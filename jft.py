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
category_list = []
count_list = []
l = 0
i = 0
k = 0

for c1 in range(0, len(dictCategory)-1):
    j = list(dictCategory[c1].items())
    report_list_tuples.append(j)

for c2 in report_list_tuples:
    for i1 in c2:
        report_list.append(i1)

for c3 in report_list:
    for i2 in c3:
        report.append(i2)
 
while(i<(len(report)-1)):
    final_report.append(report[i+1])
    i = i + 2
 
while( k<(len(final_report)-1) ):
    category_list.append(final_report[k])
    k = k + 2

while( l<(len(final_report)-1) ):
        count_list.append(final_report[l+1])
        l = l + 2
        
print(count_list)