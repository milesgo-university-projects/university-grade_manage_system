from werkzeug.security import generate_password_hash

"""
str=[
'2016211257',
'2016211239',
'2016211252',
'2016211246',
'2016211235',
'2016211258',
'2016211237',
'2016211261',
'2016211265',
'2016211263',
'2016210262',
'2016210249',
'2016210250',
'2016210244',
'2016210253',
'2016212326',
'2016212241',
'2016212256',
'2016212264',
'2016212255']
"""

"""
str = [
'00001',
'00002',
'00003',
'00004',
'00005',
'00006',
'00007',
'00008',
'00009',
'00010',
'00011',
'00012',
'00013',
'00014',
'00015',
'00016',
'00017',
'00018',
'00019',
'00020',
'00021',
'00022',
'00023',
'00024'
]
"""

f = open('tmp.txt', 'w')
for s in str:
    f.write(generate_password_hash(s) + '\n')
