from bs4 import BeautifulSoup
import re
#
# html = '''
#
# <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
# <html xmlns="http://www.w3.org/1999/xhtml">
#   <head>
#     <title>南京大学教务系统</title>
#     <base href="http://elite.nju.edu.cn:80/jiaowu/">
#     <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
# 	<link href="css/inner.css" rel="stylesheet" type="text/css">
#   </head>
#   <!--[if lte IE 6.0000]>
#   	<script language="javascript" src="js/pngfix.js"></script>
#   <![endif]-->
#   <body >
#
# 	<div id="Header">
#
#
#
#
#
#
# <div id="Logo"><a href="student/index.do#"><img src="image/student/Logo_Student.jpg" border="0"></a></div>
# <div id="TopLink"><img src="image/Icon_Help.gif"><a href="student/index.do#">帮助</a>&nbsp;&nbsp;&nbsp;&nbsp;<img src="image/Icon_Exit.gif"><a href="exit.do?type=student">退出</a></div>
# <div id="UserInfo">欢迎您：张士煜&nbsp;&nbsp;&nbsp;&nbsp;当前身份：学生</div>
#
# <script type="text/javascript" language="javascript" src="js/prototype.js"></script>
# <div id="Nav">
#   <ul>
#     <li id="homepage"><a href="student/index.do">首  页</a></li>
#     <li id="studentinfo"><a href="student/studentinfo/index.do">个人信息</a></li>
#     <li id="teachinginfo"><a href="student/teachinginfo/index.do">教学信息</a></li>
#     <li id="teachinginfo"><a href="student/elective/index.do">学期选课</a></li>
#     <li id="teachinginfo"><a href="student/signup/index.do">业务办理</a></li>
#     <li id="studentinfo"><a href="student/dissertation/index.do">论文信息</a></li>
#     <li id="studentinfo"><a href="student/evalcourse/list.do">课程评估</a></li>
#     <li id="studentinfo"><a href="student/exchange/index.do">校际交换</a></li>
#   </ul>
# </div>
# 	</div>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# <script type="text/javascript">
#
#   	function Init()
#    	{
#
#
#
#  	}
#
#   	function doAchieveConfirm(){
#   		window.confirm("你确认已经核对过所有课程的名字、英文名、学分、成绩吗?\n确认所有信息准确请按‘确定’，否则请按‘取消’") ? window.location.href="http://elite.nju.edu.cn:80/jiaowu/"+"student/studentinfo/achievementinfo.do?method=searchTermList&achieveConfirm=yes" : "";
#   	}
#   	function doApplyCourseCancel(id,termCode,courseName){
#   	   if(window.confirm("你确认申请注销课程<<"+courseName+">>的成绩吗?\n注销成功后本课程将没有成绩")){
#
#   	    window.location.href='/jiaowu/student/studentinfo/achievementinfo.do?method=applyAchievemntGiveUp&achievementId='+id+"&termCode="+termCode;
#
#   	   }
#
#   	}
# </script>
#
# <html>
#   <head>
#     <base href="http://elite.nju.edu.cn:80/jiaowu/">
#     <title>成绩信息</title>
# 	<meta http-equiv="pragma" content="no-cache">
# 	<meta http-equiv="cache-control" content="no-cache">
# 	<meta http-equiv="expires" content="0">
#
#     <link href="css/table.css" rel="stylesheet" type="text/css">
#   <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
#
# <style type="text/css">
# <!--
# .STYLE2 {
# 	font-size: 14px;
# 	font-weight: bold;
# 	color: #ffffff;
# }
# -->
# </style>
#
#   <body class="BODY"  leftmargin="50" rightmargin="50" onLoad="javascript:Init();">
#
#   <div  align="center">
#     <TABLE width="100%"  height="100%" align="left" >
#       <TR>
#         <TD colspan="4">&nbsp;</TD>
#       </TR>
#
#       <TR align="left">
#       	<TD width="50">&nbsp;</TD>
#         <TD width="150"  align="right" valign="top">
# 			<div>
# 				<table  width="100%" height="100%" border="0"  bordercolor="#3366CC">
# 				  <tr class="TEXT_TITLE"><td>请选择学期 </td></tr>
# 				  <tr height="5"><td > </td>
# 				  </tr>
#
#
#
# 						<tr align="center" height="22">
# 						  <td><a  href="student/studentinfo/achievementinfo.do?method=searchTermList&termCode=20182"/>2018-2019学年第二学期</a> </td>
# 						</tr>
#
#
# 						<tr align="center" height="22">
# 						  <td><a  href="student/studentinfo/achievementinfo.do?method=searchTermList&termCode=20181"/>2018-2019学年第一学期</a> </td>
# 						</tr>
#
#
# 						<tr align="center" height="22">
# 						  <td><a  href="student/studentinfo/achievementinfo.do?method=searchTermList&termCode=20172"/>2017-2018学年第二学期</a> </td>
# 						</tr>
#
#
# 						<tr align="center" height="22">
# 						  <td><a  href="student/studentinfo/achievementinfo.do?method=searchTermList&termCode=20171"/>2017-2018学年第一学期</a> </td>
# 						</tr>
#
#
#
#
#
# 				       <tr></tr><tr></tr>
#
# 					   <tr class="TEXT_TITLE"><td><a  href="student/studentinfo/achievementinfo.do?method=searchCreditStat" class="ButtonLink "> 学分统计</a> </td></tr>
#
# 				       <tr height="5"><td > </td></tr>
#
# 			   </table>
# 			</div>
# 		</TD>
# 		<TD width="10" >&nbsp;</TD>
#         <TD align="left" valign="top">
#
#
# 	        		<DIV align=center style="margin-bottom: 5px">
# 					<a style="font-size: 14px; text-align: center;font-weight: bold;">2018-2019学年第二学期</a>
# 					</DIV>
# 					<table width="95%" class="TABLE_BODY" bordercolor="#777777" border="1" style="border-collapse:collapse">
#
# 						<tr class="TABLE_TH">
# 						  <th align="center">序号</th>
# 						  <th align="center">课程编号</th>
# 						  <th align="center">课程名称</th>
# 						  <th align="center">英文名称</th>
# 						  <th align="center">课程类型</th>
# 						  <th align="center">学分</th>
# 						  <th align="center">总评</th>
# 						 <!--<th align="center">备注</th>-->
# 						  <th align="center">交换成绩对应课程</th>
# 						  <!--  <th align="center">操作</th>-->
# 						</tr>
#
#
#
#
# 								<tr align="left"
#
# 									 class="TABLE_TR_01"
#
#
# 								  >
# 								  <td align="center" valign="middle">1</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=00000030B&classid=90460" target="_blank"><u>00000030B</u></a>
# 								  </td>
# 								  <td valign="middle">毛泽东思想和中国特色社会主义理论体系概论（实践部分）</td>
# 								  <td valign="middle">Mao Zedong’s Thought  and  the Theoretical System of Socialism with Chinese Characteristics</td>
# 								  <td align="center" valign="middle">
# 								  	通修
# 								  </td>
# 								  <td align="center" valign="middle">3</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					80
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
#
# 									 class="TABLE_TR_02"
#
# 								  >
# 								  <td align="center" valign="middle">2</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=00000040&classid=86167" target="_blank"><u>00000040</u></a>
# 								  </td>
# 								  <td valign="middle">中国近现代史纲要</td>
# 								  <td valign="middle">Chinese Modern History Outline </td>
# 								  <td align="center" valign="middle">
# 								  	通修
# 								  </td>
# 								  <td align="center" valign="middle">2</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					75
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
# 									 class="TABLE_TR_01"
#
#
# 								  >
# 								  <td align="center" valign="middle">3</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=00010011B&classid=85600" target="_blank"><u>00010011B</u></a>
# 								  </td>
# 								  <td valign="middle">微积分II(第一层次)</td>
# 								  <td valign="middle">Calculus II(Band One)</td>
# 								  <td align="center" valign="middle">
# 								  	通修
# 								  </td>
# 								  <td align="center" valign="middle">5</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					78
#
# 									  						(重修)
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
#
# 									 class="TABLE_TR_02"
#
# 								  >
# 								  <td align="center" valign="middle">4</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=00040030A&classid=87472" target="_blank"><u>00040030A</u></a>
# 								  </td>
# 								  <td valign="middle">篮球初级</td>
# 								  <td valign="middle">Basketball (Basic)</td>
# 								  <td align="center" valign="middle">
# 								  	通修
# 								  </td>
# 								  <td align="center" valign="middle">1</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					92
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
# 									 class="TABLE_TR_01"
#
#
# 								  >
# 								  <td align="center" valign="middle">5</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=25000070&classid=84967" target="_blank"><u>25000070</u></a>
# 								  </td>
# 								  <td valign="middle">数据科学基础</td>
# 								  <td valign="middle">Statistical Method of Software Engineering</td>
# 								  <td align="center" valign="middle">
# 								  	核心
# 								  </td>
# 								  <td align="center" valign="middle">3</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					80
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
#
# 									 class="TABLE_TR_02"
#
# 								  >
# 								  <td align="center" valign="middle">6</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=25000440&classid=84969" target="_blank"><u>25000440</u></a>
# 								  </td>
# 								  <td valign="middle">软件工程与计算II</td>
# 								  <td valign="middle">Software Engineering and Computing II</td>
# 								  <td align="center" valign="middle">
# 								  	核心
# 								  </td>
# 								  <td align="center" valign="middle">4</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					82
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
# 									 class="TABLE_TR_01"
#
#
# 								  >
# 								  <td align="center" valign="middle">7</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=25000450&classid=84965" target="_blank"><u>25000450</u></a>
# 								  </td>
# 								  <td valign="middle">互联网计算</td>
# 								  <td valign="middle">Internet based Computing</td>
# 								  <td align="center" valign="middle">
# 								  	核心
# 								  </td>
# 								  <td align="center" valign="middle">4</td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					78
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
# 								<tr align="left"
#
#
# 									 class="TABLE_TR_02"
#
# 								  >
# 								  <td align="center" valign="middle">8</td>
# 								  <td align="center" valign="middle">
# 								  	<a href="http://elite.nju.edu.cn:80/jiaowu/student/elective/courseList.do?method=getCourseInfoM&courseNumber=00440090&classid=87327" target="_blank"><u>00440090</u></a>
# 								  </td>
# 								  <td valign="middle">《白领：美国的中产阶级》阅读</td>
# 								  <td valign="middle">Reading 'White collar: Middle Class of  the United States of America'</td>
# 								  <td align="center" valign="middle">
# 								  	选修
# 								  </td>
# 								  <td align="center" valign="middle"></td>
# 								  <td align="center" valign="middle">
#
#
#
#
#
#
#
#
# 									  				<ul
#
# 									  					 style="color:black"
# 									  				>
# 									  					94
#
# 									  				</ul>
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td align="center" valign="middle">
#
# 								  </td>
# 								  -->
# 								  <td align="left" valign="middle">
#
#
#
#
# 								  </td>
# 								  <!--
# 								  <td>
#
#
# 								  <input type="button" style="font-size:12px;border: #7b9ebd 1px solid;padding:1px;text-align:center;width:90px;" value="申请注销" onclick="javascript:doApplyCourseCancel('13127270','20182','《白领：美国的中产阶级》阅读')"/><br/>
#
#
#
#
# 								  </td>
# 								   -->
# 								</tr>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 					</table>
# 					<p style="color: #0000FF">注：如果成绩有疑问，请联系本院系教务员老师。</p>
# 					<p style="color: #0000FF">关于成绩的说明：<br>
# 											1、课程性质为“通修”、“平台”、“核心”的课程是属于必修课，如果不及格，必须申请重修并通过后才能满足毕业要求；<br>
# 											2、课程性质为“选修”的课程，除了部分专业会指定某些课程必须修读之外，一般只需选修总学分达到一定要求即可，单门课程不做要求；<br>
# 											3、公选课（即课程号以77、78、61开头的课程），无单独的学分要求，仅算入毕业总学分；<br>
# 											4、通识课（即课程号以002、003、004、005、37、500开头的课程），只需及格的课程总学分达到14的要求即可；<br>
#
# 					</p>
# 					<p style="color: #0000FF">
#
# 					<input type="button" style="font-size:12px;border: #7b9ebd 1px solid;padding:1px;text-align:center;width:90px;" onclick="javascript:doAchieveConfirm()" value="成绩确认"/>
#
# 					</p>
# 					<p style="color:red">提醒：如果英文名缺失或者觉得翻译不确切，建议你将课程号、中文名、以及正确的英文名发送至shenqun@nju.edu.cn，邮件标题为“课程英文名问题”。发送邮件1~2天后再次点击确认。</p>
#
#
#
#
#
#
# 		</TD>
#       </TR>
#     </TABLE>
#   </div>
#   </body>
# </html>
#
#   </body>
#
#
# </html>
#
# '''





def getPages():
    return None



# 将教务系统的html网页转化成【课程名称，学分，得分】的一个二维数组
def praseContent(content):
    ClassesList = []
    soup = BeautifulSoup(content,'html.parser')
    tempTable = soup.find_all("table")[2]
    trs = tempTable.find_all("tr")
    for i in range(1,len(trs)):
        tr = trs[i]
        tds = tr.find_all("td")
        # 采用二维数组来存储每一门课程的信息
        classes = []
        classes.append(tds[2].text)
        credit = tds[5].text
        if credit == '':
            credit = 0
        else:credit = int(credit)
        classes.append(credit)
        pattern = re.compile(r'\d+')
        points = int(pattern.findall(tds[6].ul.text)[0])
        classes.append(points)
        ClassesList.append(classes)
    return (ClassesList)




#
#
# if __name__ == "__main__":
#     praseContent(html)