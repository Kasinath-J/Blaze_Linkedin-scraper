# https://github.com/SergeyPirogov/webdriver_manager

# pyinstaller 
# cd current
# pyinstaller without_login_selenium.py --onefile
# use above code to convert it into .exe file

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
import requests
from bs4 import BeautifulSoup
import random
import datetime


user_agent = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240',
'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/7.1.8 Safari/537.85.17',
'Mozilla/5.0 (iPad; CPU OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4',
'Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16',
'Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.18',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_1_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B440 Safari/600.1.4',
'Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
'Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53',
'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/7.1.6 Safari/537.85.15',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.10 (KHTML, like Gecko) Version/8.0.4 Safari/600.4.10',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/45.0.2454.68 Mobile/12H321 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4',
'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53',
'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; TNJB; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.0; Touch; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; rv:11.0) like Gecko',
'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H143 Safari/600.1.4',
'Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFASWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:40.0) Gecko/20100101 Firefox/40.0',
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4',
'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MATBJS; rv:11.0) like Gecko',
'Mozilla/5.0 (Linux; U; Android 4.0.4; en-us; KFJWI Build/IMM76D) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36',
'Mozilla/5.0 (iPad; CPU OS 7_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D167 Safari/9537.53',
'Mozilla/5.0 (X11; CrOS armv7l 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0',
'',]

# BLAZE_BACKEND_URL='http://127.0.0.1:8000/'   #local deployment
BLAZE_BACKEND_URL='https://csbsblaze.pythonanywhere.com/'   #production deployment

BLAZE_BACKEND_URL+= "update/user/"


cur_Date = datetime.datetime.now(datetime.timezone.utc).date().strftime("%Y-%m-%d")

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")

# https://github.com/SergeyPirogov/webdriver_manager

def retreive_cookies():

    # https://github.com/SergeyPirogov/webdriver_manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    driver.get("https://www.linkedin.com/company/linkedin/")
    sleep(1)
    cookies_dict = {}
    for cookie in driver.get_cookies():
        cookies_dict[cookie['name']] = cookie['value']
    driver.close()
    return cookies_dict

def remove_unwanted_char(str):
    str = str.encode("ascii", "ignore").decode()  #removing utf-8 characters �
    str = str.replace("\r","").replace("\n","").replace("\t","")   #removing \n\r\t
    str = str.strip()
    return str

def decode_url(url):
    # https://www.w3schools.com/tags/ref_urlencode.asp?_sm_au_=iVVDMg0TSmrMV6Dm
    # escaping url
    splitted = url.split("url=")[1]
    encoded = splitted.split("&urlhash",1)[0]
    decoded = encoded

    decoded = decoded.replace("%21","!")
    decoded = decoded.replace("%22",'"')
    decoded = decoded.replace("%23","#")
    decoded = decoded.replace("%24","$")

    decoded = decoded.replace("%26","&")
    decoded = decoded.replace("%27","'")
    decoded = decoded.replace("%28","(")
    decoded = decoded.replace("%29",")")
    decoded = decoded.replace("%2A","*")
    decoded = decoded.replace("%2B","+")
    decoded = decoded.replace("%2C",",")
    decoded = decoded.replace("%2D","-")
    decoded = decoded.replace("%2E",".")
    decoded = decoded.replace("%2F","/")

    decoded = decoded.replace("%3A",":")
    decoded = decoded.replace("%3B",";")
    decoded = decoded.replace("%3C","<")
    decoded = decoded.replace("%3D","=")
    decoded = decoded.replace("%3E",">")
    decoded = decoded.replace("%3F","?")
    decoded = decoded.replace("%40","@")

    decoded = decoded.replace("%5B","]")
    decoded = decoded.replace("%5C","\\")
    decoded = decoded.replace("%5D","]")
    decoded = decoded.replace("%5E","^")
    decoded = decoded.replace("%5F","_")
    decoded = decoded.replace("%60","`")

    decoded = decoded.replace("%7B","{")
    decoded = decoded.replace("%7C","|")
    decoded = decoded.replace("%7D","}")
    decoded = decoded.replace("%7E","~")
    decoded = decoded.replace("%7F"," ")

    decoded = decoded.replace("%25","%")

    return decoded

def Linkedin_retreieve_fn(soup):

    ret = {}
    ret['aboutus'] = None	
    ret['headline'] = None
    ret['geoLocationName'] = None
    ret['experience'] = []
    ret['education'] = []
    ret['certifications'] = []
    ret['projects'] = []
    ret['honors'] = []
    ret['publications'] = []
    ret['connectionsCount'] = None

    try:
        ret['aboutus'] = remove_unwanted_char(soup.find_all("section",class_="summary")[0].p.text)
    except:
        pass

    try:
        ret['headline'] = remove_unwanted_char(soup.find_all("h2",class_="top-card-layout__headline")[0].text)
    except:
        pass

    
    try:
        temp = soup.find_all("h3",class_="top-card-layout__first-subline")[0]
        ret['geoLocationName'] = remove_unwanted_char(temp.find_all("div",class_="top-card__subline-item")[0].text)

        cc = remove_unwanted_char(temp.find_all("span",class_="top-card__subline-item--bullet")[0].text.split(" ")[0])
        ret['connectionsCount'] = int(cc if cc[-1]!='+' else cc[:-1])

    except:
        pass

    # education
    try:
        ans = []
        experience_list = soup.find_all("ul",class_="experience__list")[0].find_all("li",class_="experience-item")
        for exp in experience_list:
            temp = {}
            temp["title"] = None
            temp["companyName"] = None
            temp["description"] = None
            temp["period"] = None

            try:
                temp["title"] = remove_unwanted_char(exp.find_all("h3",class_="profile-section-card__title")[0].text)
            except:
                pass

            try:
                temp["companyName"] = remove_unwanted_char(exp.find_all("h4",class_="profile-section-card__subtitle")[0].a.text)
            except:
                pass

            try:
                more_description = exp.find_all("p",class_="show-more-less-text__text--more")
                if len(more_description)==1:
                    temp["description"] = remove_unwanted_char(more_description[0].text)
                
                if len(more_description)==0:
                    less_description = exp.find_all("p",class_="show-more-less-text__text--less")
                    temp["description"] = remove_unwanted_char(less_description[0].text)
            except:
                pass

            try:
                item__duration = exp.find_all("p",class_="experience-item__duration")[0]
                temp["period"] = remove_unwanted_char((item__duration.text).replace(item__duration.find_all("span",class_="date-range__duration")[0].text,""))
            except:
                pass
            
            ans.append(temp)

        ret["experience"] = ans
    except:
        pass

    # education
    try:
        ans = []
        education_list = soup.find_all("ul",class_="education__list")[0].find_all("li",class_="education__list-item")
        for edu in education_list:
            temp = {}
            temp["schoolName"] = None
            temp["degreeName_fieldOfStudy_grade"] = None
            
            try:
                temp["schoolName"] = remove_unwanted_char(edu.find_all("h3",class_="profile-section-card__title")[0].text)
            except:
                pass
            
            try:
                degree_info = edu.find_all("span",class_="education__item--degree-info")
            except:
                pass

            try:
                temp["degreeName_fieldOfStudy_grade"]=""
                for i in degree_info:
                    temp["degreeName_fieldOfStudy_grade"]+=i.text+"-"
            except:
                pass

            ans.append(temp)

        ret["education"] = ans
    except:
        pass

    # certifications
    try:
        ans = []
        cert_list = soup.find_all("ul",class_="certifications__list")[0].find_all("li",class_="profile-section-card")
        for cert in cert_list:
            temp = {}
            temp['name'] = None
            temp['authority'] = None
            temp['period'] = None
            temp['licenseNumber'] = None
            temp['url'] = None

            try:
                temp['url'] = decode_url(cert.find_all("a",class_="profile-section-card__title-link")[0]["href"])
            except:
                pass
            
            try:
                temp['name'] = remove_unwanted_char(cert.find_all("h3",class_="profile-section-card__title")[0].text)
            except:
                pass

            try:
                temp["authority"] = remove_unwanted_char(cert.find_all("h4",class_="profile-section-card__subtitle")[0].text)
            except:
                pass

            try:
                temp["period"] = remove_unwanted_char(cert.find_all("div",class_="certifications__date-range")[0].text)
            except:
                pass

            try:
                temp["licenseNumber"] = remove_unwanted_char(cert.find_all("div",class_="certifications__credential-id")[0].text)
            except:
                pass

            ans.append(temp)

        ret["certifications"] = ans
    except:
        pass

    # projects
    try:
        ans = []
        proj_list = soup.find_all("ul",class_="projects__list")[0].find_all("li",class_="personal-project")
        for proj in proj_list:
            temp = {}
            temp['title'] = None
            temp["period"] = None
            temp['description'] = None
            temp['url'] = None
            temp['members'] = None

            try:
                temp["title"] = remove_unwanted_char(proj.find_all("h3",class_="profile-section-card__title")[0].a.text)
            except:
                pass

            try:
                temp["period"] = remove_unwanted_char(proj.find_all("h4",class_="profile-section-card__subtitle")[0].text)
            except:
                pass
            
            try:
                more_description = proj.find_all("p",class_="show-more-less-text__text--more")
                if len(more_description)==1:
                    temp["description"] = remove_unwanted_char(more_description[0].text)
                
                if len(more_description)==0:
                    less_description = proj.find_all("p",class_="show-more-less-text__text--less")
                    temp["description"] = remove_unwanted_char(less_description[0].text)
            except:
                pass

            try:
                temp['url'] = decode_url(proj.find_all("a",class_="profile-section-card__title-link")[0]['href'])
            except:
                pass
            
            
            try:
                temp['members'] = [li.a['title'] for li in proj.find_all("ul",class_="personal-project__contributors")[0].find_all("li",class_="face-pile__list-item")]

            except:
                pass

            ans.append(temp)

        ret["projects"] = ans
    except:
        pass

    # honors
    try:
        ans = []
        honor_list = soup.find_all("ul",class_="awards__list")[0].find_all("li",class_="profile-section-card")
        for honor in honor_list:
            temp = {}
            temp['title'] = None
            temp['description'] = None
            temp['issuer'] = None
            temp['issueDate'] = None

            try:
                temp["title"] = remove_unwanted_char(honor.find_all("h3",class_="profile-section-card__title")[0].text)
            except:
                pass

            try:
                more_description = honor.find_all("p",class_="show-more-less-text__text--more")
                if len(more_description)==1:
                    temp["description"] = remove_unwanted_char(more_description[0].text)
                
                if len(more_description)==0:
                    less_description = honor.find_all("p",class_="show-more-less-text__text--less")
                    temp["description"] = remove_unwanted_char(less_description[0].text)
            except:
                pass

            try:
                temp["issuer"] = remove_unwanted_char(honor.find_all("h4",class_="profile-section-card__subtitle")[0].text)
            except:
                pass

            try:
                temp["issueDate"] = remove_unwanted_char(honor.find_all("span",class_="date-range")[0].text)
            except:
                pass

            ans.append(temp)

        ret["honors"] = ans
    except:
        pass

    # publications
    try:
        ans = []
        publications_list = soup.find_all("ul",class_="publications__list")[0].find_all("li",class_="profile-section-card")
        for pub in publications_list:
            temp = {}
            temp['name'] =None
            temp['description'] =None
            temp['publisher_issueDate'] =None
            temp['url'] =None

            try:
                temp["name"] = remove_unwanted_char(pub.find_all("h3",class_="profile-section-card__title")[0].text)
            except:
                pass

            try:
                more_description = pub.find_all("p",class_="show-more-less-text__text--more")
                if len(more_description)==1:
                    temp["description"] = remove_unwanted_char(more_description[0].text)
                
                if len(more_description)==0:
                    less_description = pub.find_all("p",class_="show-more-less-text__text--less")
                    temp["description"] = remove_unwanted_char(less_description[0].text)
            except:
                pass
            
            try:
                pu = pub.find_all("span",class_="personal-project__subtitle-item")
                dummy = ""
                for p in pu:
                    dummy+=remove_unwanted_char(p.text)+"-"
                temp['publisher_issueDate'] = dummy
            except:
                pass

            try:
                temp["url"] = decode_url(pub.find_all("a",class_="personal-project__button")[0]["href"])
            except:
                pass

            ans.append(temp)

        ret["publications"] = ans
    except:
        pass

    return ret    



# with open('z_kasi.html', 'r',encoding='utf-8') as content_file:
# with open('z_selvaram.html', 'r',encoding='utf-8') as content_file:
    # content = content_file.read()

# soup = BeautifulSoup(content,'html.parser')
# temp = Linkedin_retreieve_fn(soup)



def get_request():
    # lst = [
    #     {
    #         "id":"kasinath@student.tce.edu",
    #         "linkedin":"kasinath-j-2881a6200"
    #     },
    #     {
    #         "id":"selvaram@student.tce.edu",
    #         "linkedin":"selvaramg"
    #     },
    #     {
    #         "id":"harihara@student.tce.edu",
    #         "linkedin":"harihara-subramanian-m-007"
    #     },
    #     {
    #         "id":"sriram@student.tce.edu",
    #         "linkedin":"sriram-g-k-a415b7218"
    #     }
    # ]
    # return lst

    profile_res = requests.get(BLAZE_BACKEND_URL+"receiving_Data/")
    return profile_res.json()
    
profiles = get_request()
cookies_dict = retreive_cookies()

for i in range(len(profiles)):

    ret = {
                "id":profiles[i]["id"],
                "name":profiles[i]["name"],
                "linkedin":None,
            }
    
    try:
        if profiles[i]["linkedin"]==None or profiles[i]["linkedin"]=="":
            ret["linkedin"] = None 
        else:
            if ("linkedin_date" not in profiles[i]) or (profiles[i]["linkedin_date"]!=cur_Date):

                ua = random.choice(user_agent)
                resp = requests.get("https://www.linkedin.com/in/{}/?trk=public-profile-join-page".format(profiles[i]["linkedin"]),
                cookies=cookies_dict,
                headers={
                    'user-agent': ua,
                    'accept':'application/vnd.linkedin.normalized+json+2.1',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.6',
                    'upgrade-insecure-requests':'1',
                    'scheme': 'https',
                })                

                print(resp)
                if resp.status_code==404:
                    print("Invalid user profile")
                    continue

                if(resp.status_code!=200):
                    i-=1
                    print("retreieveing cookies")
                    cookies_dict = retreive_cookies()
                    continue

                html_doc = resp.text
                soup = BeautifulSoup(html_doc, 'html.parser') 

            
                ret["linkedin"] = Linkedin_retreieve_fn(soup)

                requests.put(BLAZE_BACKEND_URL+"{}/".format(profiles[i]["id"]) ,json=ret)

            # else:
            #     print("updated today")

    except:
        pass


sleep(5)
