import requests
import time
import sys
import os
import queue
from bs4 import BeautifulSoup


def get_content(url):

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }

        r = requests.get(url=url, headers=headers)
        r.encoding = 'utf-8'
        content = r.text
        return content
    except:
        s = sys.exc_info()
        print("Error '%s' happened on line %d" % (s[1], s[2].tb_lineno))
        return " ERROR "





html = '''
    '\r\n\r\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\r\n\r\n<html>\r\n\r\n\t<head>\r\n\t\t<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\r\n\t\t\r\n\t\t<title>南京大学教务系统</title>\r\n\t\t<link href="css/homepage.css" rel="stylesheet" type="text/css">\r\n\r\n\t</head>\r\n\t<script type="text/javascript">\r\n\r\n\tfunction CheckForm()\r\n\t{\r\n\t\tvar ssValidateCode = "null";\r\n\t\t\r\n\t\tvar oName = document.getElementById("userName");\r\n\t\tif(oName.value.length == 0)\r\n\t\t{\r\n\t\t\talert("请输入用户名称!");\r\n\t\t\toName.focus();\r\n\t\t\treturn false;\r\n\t\t}\r\n\t\t\r\n\t\tvar oPassword = document.getElementById("password");\r\n\t\tif(oPassword.value == "")\r\n\t\t{\r\n\t\t\talert("请输入密码!");\r\n\t\t\toPassword.focus();\r\n\t\t\treturn false;\r\n\t\t}\r\n\t\t\r\n\t\t\r\n\t\tvar oValidateCode = document.getElementById("ValidateCode");\r\n\t\tif(oValidateCode.value.length == 0)\r\n\t\t{\r\n\t\t\talert("请输入验证码！");\r\n\t\t\toValidateCode.focus();\r\n\t\t\treturn false;\r\n\t\t}\r\n\t\t\r\n\t\t/*if(oName.value.length == 9 && (oName.value.substr(0,2) == \'07\' || oName.value.substr(0,2) == \'08\'))\r\n\t\t{\r\n\t\t\toName.value = "";\r\n\t\t\toPassword.value = ""\r\n\t\t\toName.focus();\r\n\t\t\treturn false;\r\n\t\t}*/\r\n\t\t\r\n\t\t// document.write("session:>" + ssValidateCode + "---img:>" + oValidateCode.value);\r\n\t\treturn true;\r\n\t}\r\n\t\r\n\tfunction RefreshValidateImg(sValidateImgId)\r\n\t{\r\n\t\tdocument.getElementById(sValidateImgId).src = "ValidateCode.jsp?TimeCode=" + Math.random() + "100";\r\n\t}\r\n\r\n</script>\r\n\t<body>\r\n\t\t<div id="Wrapper">\r\n\t\t\t<table width="740" height="100%" align="center" cellpadding="0"\r\n\t\t\t\tcellspacing="0">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td height="136">\r\n\t\t\t\t\t\t<div id="Logo">\r\n\t\t\t\t\t\t\t<a href="#"><img src="image/homepage/IndexLogo.jpg"\r\n\t\t\t\t\t\t\t\t\tborder="0"> </a>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td height="39"></td>\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\t\t\t\t\t\r\n\t\t\t\t\t<td height="341" id="Main">\t\t\t\t\t\t    \t\t\t\t\t\r\n\t\t\t\t\t\t<div id="Login">\r\n\t\t\t\t\t\t<font style="font-size: 12px;font-weight:bold;color: #FF0000"></font><br>\r\n\t\t\t\t\t\t<form method="post" action="login.do" onsubmit="JavaScript: return CheckForm();">\r\n\t\t\t\t\t\t\t<label>\r\n\t\t\t\t\t\t\t\t用户\r\n\t\t\t\t\t\t\t</label>\r\n\t\t\t\t\t\t\t<input id="userName" name="userName" type="text" class="InputBox Username" />\r\n\t\t\t\t\t\t\t<br />\r\n\t\t\t\t\t\t\t<label>\r\n\t\t\t\t\t\t\t\t密码\r\n\t\t\t\t\t\t\t</label>\r\n\t\t\t\t\t\t\t<input type="password" id="password" name="password" class="InputBox Password">\r\n\t\t\t\t\t\t\t<input type="hidden" name="returnUrl" value="null" />\r\n\t\t\t\t\t\t\t<br /><br />\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t<img style="margin-left:30px;" border="0" id="ValidateImg" src="ValidateCode.jsp" />\r\n\t\t\t\t\t\t\t<a href="JavaScript: RefreshValidateImg(\'ValidateImg\');">看不清？</a>\r\n\t\t\t\t\t\t\t<br />\r\n\t\t\t\t\t\t\t<label>\r\n\t\t\t\t\t\t\t\t验证\r\n\t\t\t\t\t\t\t</label>\r\n\t\t\t\t\t\t\t<input type="text" id="ValidateCode" name="ValidateCode" class="InputBox Username">\r\n\t\t\t\t\t\t\t<br />\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t<input type="submit" class="Btn" value="" style="margin-left:30px;"/>\r\n\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t<a target="_blank" href="help/index.htm" style="margin-left:30px;">使用帮助</a>\r\n\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t</form>\r\n\t\t\t\t\t\t</div>\t\t\t\t\t\t\r\n\t\t\t\t\t\t<div id="News">\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t<ul>\r\n\t\t\t\t\t\t\t\t<label style="color: red;font-size: 12px;">教师登录：</label>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t 用户名为工资号，初始密码为工资号，请及时更改密码。\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t 可进入帮助了解如何使用本系统。\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<br/>\r\n                                                                <label style="color: red;font-size: 12px;">新生登陆：</label>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t 用户名为学号，初始密码为录取号的<strong>后6位</strong>（或学号）。\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<label style="color: red;font-size: 12px;">新生登录注意事项：</label>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t 1. 请初次登录后进入【个人信息】核对您的基本信息。\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t 2. 如果出生日期或身份证号有误请及时与辅导员联系。\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li>\r\n\t\t\t\t\t\t\t\t\t 3. 请填写个人联系方式，便于与您及时联系，谢谢。\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</td>\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<td valign="top" id="Footer">\r\n\t\t\t\t\t\tCopyright &copy; 2007 All Rights Reserved. 版权所有：南京大学教务处\r\n\t\t\t\t\t\t<a href="#">联系我们</a>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n\t\t\t</table>\r\n\t\t</div>\r\n\t</body>\r\n\t\t\r\n</html>\r\n'

'''


# 解析内容
def praseContent(content):
    soup = BeautifulSoup(content,'html.parser')
    chapter = soup.find(name='div',class_="bookname").h1.text
    content = soup.find(name='div',id="content").text

    next1 = soup.find(name='div',class_="bottem1").find_all('a')[2].get('href')
