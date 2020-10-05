# import re
# coding: utf-8
# with open(r'C:\Users\310295192\Desktop\data.txt') as file:
#     content = file.read()
#
#     print(content)
#     # najpierw ustalamy wzor
#
#     pattern = re.compile('\d{3}.\d{3}.\d{4}')
#     # potem ustalamy elementy, przez ktory bedziemy szukac
#     matches = pattern.finditer(content)
#
#     for match in matches:
#         print(match)
#
#
# sentence = "Ms. Johns \
# Mr. Carolina \
# Mrs Jallo \
# Mr Karlito \
# Mrs. Bambuco"
#
# wzor = re.compile('Mr\.?\s[A-Z]')
# matches = wzor.finditer(sentence)
#
# for match in matches:
#     print(match)
#
# # list of what symbols mean
# # . is for  any character except new line
# # \d is for digit
# # D is not for digits
# # w is for word character (a-zA-Z0-9_)
# # W not a word characdter
# # s i(s for white space (space, tab, new line)
# # S not a white space
#
#
# # every letter that is upper just negacts smaller ones
#
# # so for d and digits, D will negate that
#
# # for w and word charcdter, W will negate that
# # s is for white space (space, tab, new line) and S negates that
#
# # we can use quantifiers
# # * can match 0 or more characters
# # + can match 1 or more charcters
# # ? can match 0 or one character
# # {} will match exact number of characters
# # {3,4} will match the range of numbers (minimum,maximum)
#
# example ='Maciej jedzie na salonie bo nie plonie'
#
# # najpierw ustawiamy pattern
# pattern = re.compile(r'\w+ie\b')
#
# matches = pattern.finditer(example)
#
# for match in matches:
#     print(match)
#
#
#
#
# import re
# #18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
#
#
#
# # .       - Any Character Except New Line
# # \d      - Digit (0-9)
# # \D      - Not a Digit (0-9)
# # \w      - Word Character (a-z, A-Z, 0-9, _)
# # \W      - Not a Word Character
# # \s      - Whitespace (space, tab, newline)
# # \S      - Not Whitespace (space, tab, newline)
# #
# # \b      - Word Boundary
# # \B      - Not a Word Boundary
# # ^       - Beginning of a String
# # $       - End of a String
# #
# # []      - Matches Characters in brackets
# # [^ ]    - Matches Characters NOT in brackets
# # |       - Either Or
# # ( )     - Group
# #
# # Quantifiers:
# # *       - 0 or More
# # +       - 1 or More
# # ?       - 0 or One
# # {3}     - Exact Number
# # {3,4}   - Range of Numbers (Minimum, Maximum)
#
#
# string = "Exercises number 1, 12, 13, and 345 are important"
#
# pattern = re.compile("\d{1,3}")
#
# matches = pattern.finditer(string)
#
# for match in matches:
#     print(match)
#
# # Write a Python program to find all words starting with 'a' or 'e' in a given string
# #string_1 = 'During his in Świnoujścieut I hope that it will sail to the whole Central Europe. It"s a matter of not only our security, Poland"s security, but also the security of the Central Europe, the region where the so-called Three-Seas countries meet up," he added. (www.tvn24.pl)'
# string_1 = "Update #4, Saturday, 12:35 pm: The trade is expected to become official on July 6 but this could be amended to July 30, Wojnarowski reports. Waiting until July 30 would allow L.A. to include the cap hit from the No. 4 pick and thus free up enough room on their end to sign another max free agent. Wojnarowski adds that this is assuming Davis refuses to waive his $4 million trade kicker. Update #3, 11:08 pm: I’ve updated the body of the article with a number of details about the draft picks that the Pelicans will acquire. You can also read our complete breakdown of those draft assets New Orleans will acquire. Update #2, 7:35 pm: Wojnarowski reports that Ingram is expected to be back on the court in July and a full go by training camp. Ingram’s 2018-19 campaign ended prematurely with deep venous thrombosis. Update #1, 7:09 pm: The Pelicans have already received significant interest in the No. 4 pick, Wojnarowski tweets. The deal could essentially grow even larger. The Los Angeles Lakers have agreed to acquire Anthony Davis from the New Orleans Pelicans, Adrian Wojnarowski of ESPN reports. In exchange for the superstar the Pels will bring aboard Lonzo Ball, Brandon Ingram, Josh Hart and a bevy of picks. The Lakers will send a total of three first-round picks to New Orleans, including the No. 4 pick in next week’s NBA Draft. They’ll additionally get the right to swap draft picks with the L.A. in two other years. Tim Bontemps of ESPN has revealed that the Pels will get a top-8 pick in 2021 <it’s reverse protected>, which would become unprotected in 2022 if it doesn’t transfer the first time through. They’ll also get an unprotected first rounder in 2024, when LeBron James is 39 years old. Further, in 2023 New Orleans will have the option to swap first picks with Los Angeles and they’ll be able to defer their 2024 pick to 2025 if they so choose, giving the Pelicans as firm a grasp on the Lakers’ picks over the course of the next half decade as the Celtics had on Brooklyn’s when they acquired Kevin Garnett. We wrote earlier this week about how Pels vice president of basketball operations David Griffin had wanted several days prior to the draft to scout potential candidates if they were to acquire a pick. Now they’ll have just that, which will help them scout prospective choices or work out another deal with a third party team. The trade cannot become official until July 6, ESPN’s Bobby Marks adds. Depending on when exactly they pull the trigger formally, however, will impact how much cap space the Lakers will have afterward. Marks tweets that L.A. could have either $27.8 million in room or $32.5 million in room, depending on timing and whether or not Davis waives his $4 million trade kicker. The combination of Anthony Davis and LeBron James should make the Lakers an instant contender in an unpredictable Western Conference. Now, with just about enough cap space to sign another max talent, Marc Stein of the New York Times tweets that the franchise is expected to make a run at Kemba Walker. The young assets heading to New Orleans, conversely, give the Pelicans a multitude of high ceiling prospects to develop alongside projected 2019 first-overall pick Zion Williamson. As we wrote about in another article earlier this week, the Lakers were intent on holding Kyle Kuzma back in any trade package for Davis. They managed to do so but the Pelicans seem to have acquired additional draft picks than what was initially floated. At times throughout this process it seemed likely that a third team would have to get involved to appease the Pels but the haul they managed to nab from Los Angeles alone is a formidable one. Ultimately the Lakers managed to convince New Orleans to pull the trigger. Marc Stein of the New York Times additionally tweets that the Boston Celtics refused to include Jayson Tatum in any AD offer."
# # pattern = re.compile(r'\b[a|e|A|E]\w*')
# pattern = re.compile("Update")
#
# matches = pattern.finditer(string_1)
#
# for match in matches:
#     print(match)
#
# # 5 letters words that starts with a and end with b to s
#
# pattern = re.compile(r'\ba\w{3}[b-t]\b')
#
# matches = pattern.finditer(string_1)
#
# for match in matches:
#     print(match)
#
#
#
# # find a number
#
# pattern = re.compile(r'\d')
# matches = pattern.finditer(string_1)
# for x in matches:
#     print(x)
# # start with t and second is a
#
# pattern = re.compile(r'\bta\w*\b')
#
# matches = pattern.finditer(string_1)
#
# for match in matches:
#     print(match)
#
# pattern = re.compile(r'\b\w*[bB]all\w*\b')
#
# matches = pattern.finditer(string_1)
#
# for match in matches:
#     print(match)
# # matches = pattern.finditer(string_1)
# #
# # for match in matches:
# #     print(match)
# #
# # # Write a Python program to separate and print the numbers and their position of a given string
# # pattern = re.compile(r'\d+')
# #
# # matches = pattern.finditer(string_1)
# #
# # for match in matches:
# #     print(match)
# #
# # # Write a Python program to find all five characters long word in a string
# #
# # pattern = re.compile(r'\b\w{5}\b')
# #
# # matches = pattern.finditer(string_1)
# #
# # for match in matches:
# #     print(match)
# #
# # pattern = re.compile(r'\b[a]b+\b')
#
# # string = "Hello 12345 World"
# # variable = [number  for number in string if number.isdigit()]
# # print(variable)
#
# print(3 % 10)


'''abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

[\w\.\-]*@[\w\-]*.\w{3}


google.com
coreyms.com
youtube.com
nasa.gov

'''

import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson


Mr. T   


CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'\s\w{3}\s')


# subbed_urls = pattern.sub(r'\2\3',urls)

# print(subbed_urls)
matches = pattern.search(sentence)

# for x in matches:
#     print(x)
print(matches)
import os

directory = os.getcwd()[:-6]

# with open(directory + '\data.txt','r') as f:
#     content = f.read()
#     matches = pattern.finditer(content)
#
#     for x in matches:
#         print(x)

# print(directory)
import json

with open(directory+'states.json','r') as f:
    data = json.load(f)

    for x in data['states']:
        x['abbreviation'] = x['name'][:2]
        del x['name']

        print(x)

    with open(directory+'new states.json','w') as writing:
        json.dump(data,writing,indent=2)
