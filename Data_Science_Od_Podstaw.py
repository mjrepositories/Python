# import random
#
# for_nums = [random.random() for _ in range(4)]
# print(for_nums)
#
# ranging = [random.randrange(5,10) for _ in range(5)]
# print(ranging)
#
# random_values = [x for x in range(10)]
# random.shuffle(random_values)
# print(random_values)


x = '2019'

def abc(maciej):
    global x
    print(x + "Karol ()".format('monika'))
    return maciej



abc('karol')

import requests

r = requests.get('https://ot3.optilo.eu/opt_ext_smxc9a/p001/druid.php?m=multi&s=MultiJobList')
print(r.text)