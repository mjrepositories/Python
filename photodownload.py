import requests
import time

baptize_counter = 11
baptize = "http://www.naszacukiernia.pl/wp-content/uploads/2/"
baptize_folder = 'M:\\my VS Code\\My Pages\\Nasza Cukiernia\\cakes\\baptize\\'

birthday_counter = 300
birthday = "http://www.naszacukiernia.pl/wp-content/uploads/4/"
birthday_folder = "M:\\my VS Code\\My Pages\\Nasza Cukiernia\\cakes\\birthday\\"

# should be 103 but they changed the link
wedding_counter = 74
wedding = 'http://www.naszacukiernia.pl/wp-content/uploads/1/'
wedding_folder = 'M:\\my VS Code\\My Pages\\Nasza Cukiernia\\cakes\\wedding\\'


communion_counter = 35

communion = "http://www.naszacukiernia.pl/gallery/5/"
communion_folder = 'M:\\my VS Code\\My Pages\\Nasza Cukiernia\\cakes\\communion\\'

# # looping over baptize
# for x in range(1,baptize_counter+1):
#     if x <10:
#         number = '000{}.jpg'.format(x)
#     else:
#         number = '00{}.jpg'.format(x)
#     target_url = baptize + number
    
#     # getting the GET response
#     res = requests.get(target_url)

#     print(target_url)
#     print(baptize_folder+number)

#     # writing to file
#     with open(baptize_folder+number,'wb') as f:
#         f.write(res.content)
#     time.sleep(1)


# looping over birthday
for x in range(1,birthday_counter+1):

    number = '{}.jpg'.format(x)

    target_url = birthday + number


    # getting the GET response
    res = requests.get(target_url)
    
    print(target_url)
    print(birthday_folder+number)

    # writing to file
    with open(birthday_folder+number,'wb') as f:
        f.write(res.content)
    time.sleep(1)

# # looping over wedding
# for x in range(1,wedding_counter+1):
#     if x <10:
#         number = '0000{}.jpg'.format(x)
#     elif x <100:
#         number = '000{}.jpg'.format(x)
#     else:
#         number = '00{}.jpg'.format(x)
#     target_url = wedding + number

    
#     # getting the GET response
#     res = requests.get(target_url)
    
#     print(target_url)
#     print(wedding_folder+number)

#     # writing to file
#     with open(wedding_folder+number,'wb') as f:
#         f.write(res.content)
#     time.sleep(1)

# # looping over communion
# for x in range(1,communion_counter+1):
#     if x <10:
#         number = '000{}.jpg'.format(x)
#     else:
#         number = '00{}.jpg'.format(x)
#     target_url = communion + number

    
#     # getting the GET response
#     res = requests.get(target_url)
    
#     print(target_url)
#     print(communion_folder+number)

#     # writing to file
#     with open(communion_folder+number,'wb') as f:
#         f.write(res.content)
#     time.sleep(1)