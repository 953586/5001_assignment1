import re #正则表达式必用库
#清屏命令：%clear
with open('blocklist.xml') as f: #在同一个路径可以直接打开
    lst=f.read().splitlines()
    #splitlines() 按换行符切割，返回以各行为元素的list
#(1)i or g start + digital end
for s in lst:
#    tmp=re.findall('blockID="i(.*?)\d"|blockID="g(.*?)\d"',s)
    tmp=re.findall('blockID="g(.*?)\d"',s)
    #re.findall(pattern, string)：匹配所有适配值，以list返回; 
    #re.match ：只在开始位置匹配；re.search ：返回第一个匹配
    #(.*)：*表除换行符外所有字符,a.*b:匹配以a开始以b结束的字符串；(.*?):非贪婪，匹配到了不再继续
    #\d:数字（digital）；\D：非数字；\s:空格；\w：字母数字下划线；
    if  tmp:
        print(s)
        
#(2)邮箱基本格式：名称@域名 eg:12345@qq.com
for s in lst:
    tmp=re.findall('id="[a-zA-Z0-9._%+-]+@(?!.*\.\..*)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"',s)
    #名称部分：[a-zA-Z0-9._%+-]，[a-zA-Z0-9]：任何字母和数字
    #域名部分：@[a-zA-Z0-9_-]+\.[a-zA-Z]{2,4}，{n,m}：重复匹配至少n次,至多m次（com或com.cn）
    #.：除换行符外的任何字符；\:引用符（转义）；\.：匹配点字符
    #.*\.\..*: 断句为.* \. \. .*
    if  tmp:
        print(s)


