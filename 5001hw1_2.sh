#!/bin/bash
Dirname="DDM"
for i in {1..100}
do
    dir="$Dirname"$i  #$表示取值，双引号翻译变量，单引号不翻译变量
    mkdir -p $dir #注意p后面一定要有空格
    cd $dir           #每一次写文件都要进入路径
    echo "nanoseconds since 1970-01-01 00:00:00 UTC:" > time_till_now.txt 
    #还可以用touch DDM{1..5}/1.txt来生成文件
    stamp=$(date +%s.%N) #如果不要精确到毫微秒就是%s
    r=$(echo "$stamp * 1000000000"|bc)  #浮点数运算
    rr=${r%.*} #浮点数转化为小数，只适用于bash
    echo "<$rr>" >> time_till_now.txt 
    cd ..                #cd..:返回上一层，cd ：返回根目录
done
