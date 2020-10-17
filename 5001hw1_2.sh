#!/bin/bash
Dirname="DDM"
for i in {1..100}
do
    dir="$Dirname"$i  
    mkdir -p $dir #注意p后面一定要有空格
    cd $dir           #每一次写文件都要进入路径
    echo "nanoseconds since 1970-01-01 00:00:00 UTC:" > time_till_now.txt 
    #还可以用touch DDM{1..5}/1.txt来生成文件
    stamp=$(date +%s.%N)  #如果不要精确到毫微秒就是%s
    echo "< $stamp >" >> time_till_now.txt
    cd ..                #cd..:返回上一层，cd ：返回根目录
done