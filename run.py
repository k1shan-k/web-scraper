# # # # from datetime import date
# # # #
# # # # letter = '''Dear, <|name|>
# # # # You are selected
# # # # date: <|Date|>'''
# # # #
# # # # a = input("what is your name ?\n ")
# # # #
# # # # b = str(date.today())
# # # #
# # # # letter = letter.replace("<|name|>", a)
# # # # letter = letter.replace("<|Date|>", b)
# # # #
# # # # print(letter)
# # #
# # # test = "bro wtf are you talking  about"
# # #
# # # piss = test.replace("  " , " ")
# # #
# # # print(piss)
# #
# # a = min(2,54,56)
# # #b = max[34,3453,54]
# #
# # print(a)
# # #print(b)
# #
# a=[]
# for i  in range(6):
#     l=int(input("please enter the marks of student"))
#     a.append(l)
# a.sort()
# print(a)


# import requests
# a=[]
# for i in range(2):
#     test = requests.get("https://ipinfo.io")
#     real = test.json()
#     a.append(real['ip'])
# print(a)


# list = [23,44,43]
#
# list.sort()
#
# # print(list)
# m = {
#     "kishan" : "greatest haxxor",
#      "avnish" : "head of ceo"
# }
#
# print(m["kishan"])
#
#
#
# a = int(input("any random value please:"))
# if(a<4):
#     print("we are talking about 4")
# elif(a>50):
#     print("we are talking about 50")
#
# else:
#     print("nigger")
#
#
# a = int(input("Please enter your age : "))
#
# if (a>=18 or a<60):
#     print("welcome to bar sir")
# else:
#     print("kido")
#
#
# import requests
#
# kishan = requests.get("https://ipinfo.io")
#
# print(kishan.json())
#
# text = input("enter your comment please: ")
#
# spam = False
#
# if ("money the god" in text):
#     spam = True
# elif ("buy now" in text):
#     spam = True
# else:
#     print("you are sexy")
#
# a = input("What is your username: \n")
#
# b = len(a)
#
# if (b<=10):
#
#     print("please enter username (must be more then 10) :\n")
# else:
#     print("bro you are god")
# #print(b)
#
# a = [ "kishan", "dada", "me"]
#
# b = input("please enter any name")
#
# if (b in a):
#     print("yes is in the list")
# else:
#     print("americans go go go")
#
# a = int(input("please enter the marks of kishan: \n"))
#
# if (90<a<100):
#     print("you are greatest")
# if (90<a<100):
#     print("you are greatest")
# if (90<a<100):
#     print("you are greatest")
# if (90<a<100):
#     print("you are greatest")
#
# post = input("please write your post: \n")
#
# if "kishan" in post:
#     print("we don't like to talk alot about kishan")
#
# else:
#     print("good to know ")
#
# a = int(input("what is your age"))
# #if a>18:
# while a<18:
#     print("yes")
#     a = a + 1
# #else:
#  #   print("NO")
#

# a = int(input("any number"))
#
# for i in range(1, 100000000):
#
#     print(str(a) + "X" +str(i) + "=" + str(i*a))
#
# n = 4
#
# for i in range(4):
#     print("*" * i)

# def a(b):
#     return ((sum(b))/400*100)
#
# mars = [54, 65, 67, 89]
#
# print(a(mars))

# def max (x , y , z):
#     if (x>y):
#         if (x>z):
#             return x
#         else:
#             return z
#     else:
#         if (x > z):
#             return x
#         else:
#             return z
#
# m = max(4 ,6 ,8)
#
# print(m)

# def fu(c):
#     return (c * (9/5)) + 32
#
# a = int(input("please enter the temp: \n "))
#
# b = fu(a)
#
# print(b)

# print("fuck" , end=" sdfklj")
# print("you", end="")

# import random
# b=0
# a = [6, 8, 4, 2 ,3, 4,6,7 ,7]
# #b = random.choice(a)
# while b!=2:
#
#     b = random.choice(a)
#
#     print(b)

# import random
#
# a = random.seed(45)
#
# print(a)
# print("bro you sucks ");
#
#
# bro = int(input("please tell me your age ? \n"))
#
# while (bro<18):
#   print("see you kido")
# else:
#     age = input("sir you age is like an adult, are you adult? \n")
#     if age == "yes":
#         print("see you sir")
#     else:
#         print("kido")

# a = open("https://www.cyberkorp.co/robots.txt" , "r")
#
# c = a.read()
# a.close
# print(c)

#
# with open("C:\\Users\\vlad\\Desktop\\hacker\\poem.txt") as r:
#     k = r.read()
#     i = input("say it")
#     if i in k:
#         print("good is in this file")
#     else:
#         print(k)
#
# for i in range (2, 21):
#     for k in range (1,11):
#        a = (f"{i}x{k}={i*k}")
#        print(a , "\n")

# kvps = {"user", "bill", "password", "hillary"}
#
# print(kvps['password'])

#    names1 = ['Amir', 'Barry', 'Chales', 'Dao']
#
# loc = names1.index("Edward")
#
# print(loc)


# class place:
#     where = "sdkfj"
#     school = "GVS"
#     age = 45
#
# kishan = place()
#
#
# print(kishan.age)
# print(kishan.where)
#
# kishan.where = 343
#
# print(kishan.where)

# class programmer:
#     company = "cyberkorp"
#     def __int__(self , name , dev):
#         self.name = name
#         self.dev = dev
#
# kishan = programmer("sdf", "dsf")
#
# # avnish = programmer("avnish" ,"haxxor")
#
# a = int(input("please enter any number to find out its squre"))



# class Cal:
#     def __init__(self, pp):
#         self.say = pp
#     def sq(self):
#         print(f"The squre of {self.say} is {self.say **2}")
#
# b = Cal(a)
# b.sq()
# #b.cal()

# class Pim:
#     a = "kishan"
#



#
#
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()



# krishna = [67 ,68, 69]
# arjun = [70 ,98 ,63]
# malika = [52 , 56 , 60]
#
# k = (krishna[0] + krishna[1] + krishna[2])/3
#
# a = (arjun[0] + arjun[1] + arjun[2])/3
#
# m = (malika[0]+malika[1]+malika[2])/3
#
# what = input("What is the name of the student ? \n")
# p = what
#
# # print(k , a ,m)
# if p == "krishna":
#     print(k)
# elif p == "arjun":
#     print(a)
# elif p == "malika":
#     print(m)
# else:
#
#     print("we don't know about this student")

# q = int(input("how many students:"))
#
# if q==1:
#
#     a =input("what is the name of student")
#     b =int(input("1st subject"))
#     c =int(input(("2nd subject")))
#     d =int(input(("3rd subject")))
#
#     i = input("who's marks")
#     if i==a:
#         print((b + c + d) / 3)
# elif q==2:
#     a44 = input("what is the name of student")
#     b44 = int(input("1st subject"))
#     c44 = int(input(("2nd subject")))
#     d44 = int(input(("3rd subject")))
#
#     a1 = input("what is the name of student")
#     b1 = int(input("1st subject"))
#     c1 = int(input(("2nd subject")))
#     d1 = int(input(("3rd subject")))
#
#     i2 = input("who's marks")
#     if i2 == a44:
#         print((b44 + c44 + d44) / 3)
#     elif i2 ==a1:
#         print((b1 + c1 + d1) / 3)
# elif q==3:
#     a55 = input("what is the name of student")
#     b55 = int(input("1st subject"))
#     c55 = int(input(("2nd subject")))
#     d55 = int(input(("3rd subject")))
#
#     a2 = input("what is the name of student")
#     b2 = int(input("1st subject"))
#     c2 = int(input(("2nd subject")))
#     d2= int(input(("3rd subject")))
#
#     a3 = input("what is the name of student")
#     b3= int(input("1st subject"))
#     c3 = int(input(("2nd subject")))
#     d3 = int(input(("3rd subject")))
#
#     i3 = input("who's marks")
#     if i3 == a55:
#         print((b55 + c55 + d55) / 3)
#     elif i3 == a2:
#         print((b2 + c2 + d2) / 3)



# n = int(input().strip())
# print(n)

#
#
# k = input("name and student")
#
# m = k.split()
#
# d = int(m[1]) + int(m[2])
# print(d)

# q = int(input())
# a =[]
# for i in range(q):
#     r = input()
#     #q.split()
#     a.append(r.split())
# if q ==1:
#         z = a[0]
#         p = (int(z[1])+int(z[2])+int(z[3]))/3
#         y = z[0]
#
#         t = input()
#         if t==y:
#             print (float(format p ,'.2f'))
#
#
# elif q ==2:
#         x = a[0]
#         pp = (int(x[1]) + int(x[2]) + int(x[3])) / 3
#         u = x[0]
#
#         c = a[1]
#         ppp = (int(c[1]) + int(c[2]) + int(c[3])) / 3
#         o = c[0]
#
#         t = input()
#         if t==u:
#             print(float(pp))
#         elif t==o:
#             print(float(ppp))
#
# elif q ==3:
#         v = a[0]
#         pppp = (int(v[1]) + int(v[2]) + int(v[3])) / 3
#         ss = v[0]
#
#         b = a[1]
#         ppppp = (int(b[1]) + int(b[2]) + int(b[3])) / 3
#         zz = b[0]
#
#         n = a[2]
#         pppppp = (int(n[1]) + int(n[2]) + int(n[3])) / 3
#         cc = n[0]
#
#         t = input()
#         if t==ss:
#             print(float(pppp))
#         elif t==zz:
#             print(float(ppppp))
#         elif t==cc:
#             print(float(pppppp))

# name = input("name of the student")

# if name ==y:
#     print(p)
# elif name ==u:
#     print(pp)
# elif name ==o:
#     print(ppp)
# elif name ==ss:
#     print(pppp)
# elif name ==zz:
#     print(ppppp)
# elif name ==cc:
#     print(pppppp)

# y = int(input("enter the n"))
# p = y %2
#
# if p !=0:
#     print("Weird")
# elif 2<=y<=5:
#     if y %2 ==0:
#         print("Not Weird")
#     else:
#         print("Weird")
# elif 6<=y<=20:
#     if p ==0:
#         print("Weird")
#     else:
#         print("")
# elif y>20:
#     if p ==0:
#         print("Not Weird")
#     else:
#         print("")

# a = int(input(""))
# b = int(input(""))
#
# p = (a//b)
#
# print(int(p))
#
# q = float(a/b)
#
# print(q)

# def check(year):
#     if year % 100 == 0:
#         return False
#     elif year%4 ==0:
#         if year%400:
#             return True
#         else:
#             return False
#
#
# a = int(input(""))
#
# b=check(a)
# print(b)

# def is_leap(year):
#
#     # if year == 1990:
#     #     return False
#     # elif year % 100 == 0:
#     #     return False
#     # elif year%4 ==0:
#     #     if year%400 ==0:
#     #         return True
#     #     else:
#     #         return False
#     return True if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0) else False
#
#
#
# year = int(input())
# print(is_leap(year))


# n = int(input(""))
#
# i = 1
# while i <= n:
#     print(i, end='')
#     i = i + 1

# import requests
#
#
# k = requests.get("https://random-data-api.com/api/appliance/random_appliance")
#
# a = k.json()
# print(a)
# print(type(a))
#     # print(a)
#     # if "Fagor" in a:
    #     print("i am the god")
    # else:
    #     True
# if "Fagor" in a:
#     print("we don't use fagor")
# else:
#     print("you are welcome")

# T = ()
# print(type(T))

# x = (input("numbers")
#
# k = tuple(int(a) for a in x.split(","))
#
# # print(T)

# z = input("")
# x = input('')
# x = tuple(int(a) for a in x.split(" "))
# p = hash(x)
#
# print(p)
# from decimal import Decimal
# import random
# for i in range(5):
#     p = random.randint(1, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
# print(p)
#
# k = (5808268021613412879013171588959634605066443847374948798910691241247461856909450237607735404783440192060236327035026897505231295705976148048017108023756122021226393641898256948368825900231064487621921975823226779878296535812148893651476668639157825066996051117771095657638538162613301954827958716782026590314695094743831672642023367943985963893094459831895935728417415443393168117554609085828984301392352821552125283399141560329667055327172710451710526032785206149021655649574209580901239966377885823260563461290689918441353960131252189947507260700766285209949384107699722957229964481665303100230147043282884006707570858467269496825781912047508934397802764166008229079899079119968750380001902444375876217135712871806501934551453890424243541903098921010801716316093550480013061168938678979315184287077384988649918485175424273188722660879947671043863048352329183532637094409839742077310685624026426394307667421698979876496334782317806503054951748617248328831973920040844782800326499128626220577835600889784991727082480704852020331680221734728311004507255710133585641576433243881217964263227290976620079436285643579793581307303748156539531910693706344527221452288392309527935877224990264856579850882690019349388170404228640934578366288691523829730913171386141969655641050313020274191269760851702127728464262568018067757314847129598416223188251474232889744602 / p)
# print(Decimal(p*k))

# import requests
# import bs4
#
# k = requests.get('http://217.23.2.205:8000/')
#
# print(k.text)

# print(f"Hello {first_name}{last_name}! You just delved into python."
# a = input("")
# a = a.split(" ")
# print(a)
# b = "-".join(a)
# print(b)

#
# a = input()
#
# print(a.isalnum())
# print(a.isalpha())
# print(a.isdigit())
# print(a.islower())
# print(a.isupper())


# from flask import Flask
# from datetime import datetime
# app = Flask(__name__)
#
# @app.route("/")
#
# def hello_world():
#     return "Hello world"
#
# @app.route("/time")
#
# def  istime():
#     return datetime.now().strftime("%H:%M:%S")
# if __name__ == "__main__":
#     app.run(debug=True)
# import  requests
#
# a = requests.get("https://localhost:5000/time")
#
# print(a.json())

# import flask_monitoringdashboard as dashboard
# from flask import Flask
# from datetime import datetime
# import os
# app = Flask(__name__)
# dashboard.bind(app)
#
#
#
# @app.route("/")
#
# def hello_world():
#     return "Hello World"
#
# @app.route("/time")
#
# def  istime():
#     return datetime.now().strftime("%H:%M:%S")
#
# if __name__ == "__main__":
#     port = int(os.environ.get('PORT',5000))
#     app.run(host="0.0.0.0",port=port,debug=True)

# from flask import Flask
# from datetime import datetime
# import os
# import requests
# app = Flask(__name__)
#
#
#
# @app.route("/")
#
# def hello_world():
#     return "Hello World"
#
# @app.route("/time")
#
# def  istime():
#     k = requests.get("https://yip.su/1QJMd7")
#     print(k.content) # this is how i get notified if anyone does access /time endpoint
#     return datetime.now().strftime("%H:%M:%S")
#
#
# if __name__ == "__main__":
#     port = int(os.environ.get('PORT',5000))
#     app.run(host="0.0.0.0",port=port,debug=Tr
#
# from lxml import html
# import re
#
#
# def scrape(fd, conf):
#     return scrapes(fd.read(), conf)
#
#
# def scrapes(html_string, conf):
#     html_tree = html.fromstring(html_string)
#     return process(html_tree, html_string, conf)
#
#
# def process(html_tree, html_string, conf):
#     result = {}
#     for field in conf:
#         # extract field content with xpath or regexp:
#         scraped = None
#         if 'xpath' in conf[field]:
#             xpath = conf[field]['xpath']
#             scraped = html_tree.xpath(xpath)
#             if isinstance(scraped, list):  # element list
#                 try:
#                     scraped = map(lambda x: x.text, scraped)
#                 except:
#                     pass
#         elif 'regexp' in conf[field]:
#             regexp = conf[field]['regexp']
#             scraped = re.findall(regexp, html_string)
#
#         if scraped is not None:
#             # encode field if character encoding is defined:
#             if 'encoding' in conf[field]:
#                 encoding = conf[field]['encoding']
#                 if encoding is not None:
#                     if isinstance(scraped, list):  # list value
#                         try:
#                             scraped = map(lambda x: x.decode(encoding), scraped)
#                         except Exception as e:
#                             print
#                             "Error decoding %s field: %s" % (field, e)
#                     else:  # single value
#                         try:
#                             scraped = scraped.decode(encoding)
#                         except Exception as e:
#                             print
#                             "Error decoding %s field: %s" % (field, e)
#
#             # apply transformations (if defined)
#             if 'transf' in conf[field]:
#                 # apply transformations in chain:
#                 for func in conf[field]['transf']:
#                     if isinstance(scraped, list):  # list value
#                         try:
#                             scraped = map(func, scraped)
#                         except Exception as e:
#                             print
#                             "Error applying function %s to element list: %s" % (func, e)
#                             scraped = None
#                             break  # dont include erroneous field
#                     else:  # single value:
#                         try:
#                             scraped = func(scraped)
#                         except Exception as e:
#                             print
#                             "Error applying func %s to field value %s" % (func, scraped)
#                             scraped = None
#                             break  # dont include erroneous field
#                 if scraped is None:  # some error occurred as a result of applying transformations
#                     if 'default' in conf[field]:
#                         scraped = conf[field]['default']
#         result[field] = scraped
#
#     return result

# import os
# from cryptography.fernet import Fernet
# import _pyinstaller_hooks_contrib
#
#
# files = []
#
# for file in os.listdir():
#     if file == "ranp.exe":
#         continue
#     if os.path.isfile(file):
#         files.append(file)
# key = Fernet.generate_key()
#
# with open("thekey.key", "wb") as thekey:
#     thekey.write(key)
#
# for file in files:
#     with open(file, "rb") as thefile:
#         contents = thefile.read()
#     contents_encrypted = Fernet(key).encrypt(contents)

# import os
#
# print(os.listdir('/'))

# def test():
#     x = 10
#     x =+1
#     print(x)
# # test()
# x = int(input("what is your 1st number"))
# y = int(input("what is your 2nd number"))
# q = int(input("what is your 3nd number"))
#
#
# def great(*args):
#     if args[0] > args[1]:
#         return args[0]
#     return args[1]
# def no_great(*args):
#     return great(args[0] , great(args[1] ,args[2] ))
#
# print(no_great(x , y, q ))

# import os
# import random
# import requests
# k = random.randint(1,100)
# while k!=2:
#     k = random.randint(1 , 1000)
#
#
# # if random.randint( 1 , 6) == 2:
# if k ==2:
#     a = requests.get("https://random-data-api.com/api/v2/users")
#     print(a.json())
#
# while k!=3:
#     k = random.randint(1 , 100.)
#
#
# # if random.randint( 1 , 6) == 2:
# if k ==3:
#     a = requests.get("https://ipinfo.io")
# #     print(a.json())
# import os
#
# a = int(input("input 1"))
#
# for i in range(a):
#     os.open('__name__')

# weekdays = ['sun','mon','tue','wed','thu','fri','sat']
# listAsString = " ".join(weekdays)
# print(listAsString)
# names = ['Chris', 'Jack', 'John', 'Daman']
# print((names[-1]))

# import time
# from plyer import notification
#
# if __name__ == "__main__":
#     while True:
#         notification.notify(
#             title = "haxxor !! on top",
#             message = "Take a break!! you are real haxxor",
#             timeout = 6
#         )
#         time.sleep(8)
# from Captcha.image import ImageCaptcha
#
# image = ImageCaptcha(width = 300, height = 100)
# captcha_text = input("Larp the text")
# data = image.generate(captcha_text)
#
# image.write (captcha_text, 'E:/CAPTCHA1.png')
# from PIL import Image
# Image.open('E:/CAPTCHA1.png')
# import whois
# # import python-whois
# domain = '''input("tell me the domain:")''' "cyberkorp.co"
# domain_info = whois.whois(domain)
#
# for key, value in domain_info.item():
#     print(key, ':',value)

# a = 34545
#
# print(a[0])

# def print_full_name(first, last):
#     print(f"Hello {first} {last}! You just delved into python.")
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


# def nigga(string, where , what):
#     a = list(string)
#     a[where] = what
#     print(''.join(a))
# if __name__ == '__main__':
#     k = input("anything")
#     k1 = int(input("where"))
#     k2 = input("what")
#     print(nigga(k , k1, k2))

# def nigga(string, where , what):
#     a = list(string)
#     a[where] = what
#     print(''.join(a))
#
# s = input()
# i, c = input().split()
# s_new = nigga(s, int(i), c)
# print(s_new)

# def mutate_string(string, where , what):
#     a = list(string)
#     a[where] = what
#     return (''.join(a))
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)





# x = {}
# def percent(nigger):
#     b =  x.get(cc)
#     # tuple_of_integers = tuple(int(item) for item in b)
#     try:
#         a1 = int(b[0])
#     except:
#         a1 = float(b[0])
#     try:
#         a2 = int(b[1])
#     except:
#         a2 = float(b[1])
#     try:
#         a3 = int(b[2])
#     except:
#         a3 = float(b[2])
#     finally:
#         k = (a1 + a2 +a3)
#         j = k/3
#         ee = "{:.2f}".format(j)
#
#     return ee
#
#
#
#
# a = int(input())
#
# for i in range(a):
#     txt = input("")
#     y = txt.split(" ")
#     x[y[0]] = y[1] , y[2] , y[3]
# cc = input("who")
# tty = percent(cc)
# print(tty)


#!/bin/python3

import math
import os
import random
import re
import sys


# class Rectangle:
#     def getarea(val1 , val2):
#         a = val2*val1
#         return a
#
# class Circle:
#     def getarea(val1):
#         pie = float(3.14159)
#         a = pie*val1*val1
#         return a
#
# x = {}
#
# a = int(input())
#
# for i in range(a):
#     txt = input("")
#     y = txt.split(" ")
#     try:
#         x[y[0]] = y[1] , y[2]
#     except:
#         x[y[0]] = y[1]
# pp = list(x.keys())
# # print(pp)
# i = 0
#
# for i in range(a):
#     tt = (x.get(pp[i]))
#     # print(type(tt))
#     if type(tt) is tuple:
#         rt = Rectangle
#         # print(rt.getarea(int(tt[0],tt[1])))
#         vv =  int(tt[0])
#         vr = int(tt[1])
#         print(rt.getarea(vv , vr))
#     else:
#         rr = Circle
#         print(rr.getarea(int(tt)))



#new test

    # try:
    #     k = int(tt[0]) + int(tt[1])
    #     print("this is rectangle" + str(k))
    # except:
    #     print("this is cercle" +str(k))

    # if len(tt) ==1:
    #     print("this is cercal")
    # else :
    #     print("this is recetangle")
# for i in range(pp) :
#     pass2


# a = int(input())
# x = {}
# for i in range(a):
#     txt = input("")
#     y = txt.split(" ")
#     try:
#         x[y[0]] = y[1] , y[2]
#     except:
#         x[y[0]] = y[1]
# print(x)

# at = list(x)
# i = 0
# for i in range(a):
#     # print(f"{at[i]} with the maximum speed of {' '.join(x.get(at[i]))}")
#     if at[i] == "boat":
#         print(f"{at[i].capitalize()} with the maximum speed of {''.join(x.get(at[i]))} knots")
#     else:
#         print(f"{at[i].capitalize()} with the maximum speed of {' '.join(x.get(at[i]))}")


# for  i in range(a):
#     print(f"{x.get()}")


# cc = input("who")
# tty = percent(cc)
# print(tty)

# import requests
# from bs4 import BeautifulSoup
# url = "https://itskishan.online"
# r = requests.get(url)
# Content = r.content
# # print(Content)
#
# soup = BeautifulSoup(Content, 'html.parser')
# # print(soup)
# title = soup.title
# # print(title)
#
# anchors = soup.findAll('a')
#
# all_links = set()
#
# for link in anchors:
#     print(link.get("href"))
#     all_links.add(link.get("href"))
# print(all_links)
#
# nums = [1,2,3,6]
#
# # print(nums[-])
# i = 0
#
# for i in range(len(nums)):
#     # while i != nums[-1]:
#     #     sum = int(nums[i]) + int((nums[i+1]))
#     #     print(sum)
#     if i != nums[-1]:
#         try:
#             nums[i] = int(nums[i]) + int(nums[i + 1])
#         except:
#             pass
#     else:
#         nums[i] = int(nums[-2]) + int(nums[-1])
#
#
# print(nums)

# a = int(input())
