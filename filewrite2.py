#pip install pyhdfs 

import pyhdfs 
import contextlib

#연결상태만 확인 HdfsClient 
fs = pyhdfs.HdfsClient(hosts="192.168.56.101:9870", user_name='hduser')
status = fs.list_status("/")
print( status )

#폴더 생성하기
path ="/fruit"
filename = path+"/apple"
if not fs.exists(path):  #존재안할때 폴더만들기 
    fs.mkdirs("/fruit")     #이미 생성한 폴더를 다시 생성하면 예외가 발생한다 
    fs.mkdirs("/fruit/x/y") 


#파일을 생성 -> hdfs에 파일 올리기 
if  fs.exists(filename):
    fs.delete(filename)
    print("삭제")

fs.create(filename, "사과는 ".encode("utf-8"))  #처음에 데이터를 입력해줘야 한다 
fs.append(filename, "맛있는  ".encode("utf-8")) #앞의 파일에 추가를 한다   
fs.append(filename, "음식입니다 ".encode("utf-8"))      #앞의 파일에 추가를 한다 

#hdfs 명령어 : hadoop fs -cat /fruit/apple 
#파일을 읽어서 화면에 뿌린다. 
#파일끝까지 읽어서 뿌린다. 
s=""
with contextlib.closing( fs.open("/fruit/apple")) as f:
    s = s+ f.read().decode()

print(s)



#/webhdfs/v1/data/news?op=CREATE&user.name=hduser&namenoderpcaddress=master:9000&createflag=&createparent=true&overwrite=false