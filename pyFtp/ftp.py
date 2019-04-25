import sys,os,socket
from ftplib import FTP
host = '47.107.129.125'  #FTP主机
user = "ftpuser"
password = "wq540074./"
buffer_size = 8192
port = 21
localDir  = 'D:\\py3-study-master\\pyFtp\\test'
remoteTarget = "test" 
remoteRoot  = ""
def ftpconnect():
    ftp_server = host
    username = user
    passwords = password
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(ftp_server, port)
    ftp.login(username, passwords)
    ftp.set_pasv(False)  # 如果被动模式由于某种原因失败，请尝试使用活动模式。
    # ftp帐号登入后默认是在/home/ftpuser目录下(根据当前帐号的家目录来定)，remoteDir只需要指定此目录下的某个文件夹名，
    # 就可以把文件上传到/home/ftpuser目录下指定的目录中去
    remoteDir = remoteTarget  # 把文件上传到 /home/ftpuser/test 下，只需要填写 test目录即可
    ftp.cwd(remoteDir)  # 需要cd 切换到 test目录下

    return ftp
 
 
# def downloadfile():
#     remotepath = "/home/pub/dog.jpg"
#     ftp = ftpconnect()
#     print(ftp.getwelcome())
#     bufsize = 1024
#     localpath = 'f:\\test\\dog.jpg'
#     fp = open(localpath, 'wb')
#     ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
#     ftp.set_debuglevel(0)
#     fp.close()
#     ftp.quit()
 
 
def uploadfile(ftp):
    # print(ftp.pwd())  # 当前路径

    localpath = 'D:\\py3-study-master\\pyFtp\\uploadFile\\mmp.py'

   
    readFile = open(localpath, 'rb')
    fileName = os.path.basename(localpath)
    # print(os.path.basename(localpath))
    # print(os.path.dirname(localpath))
    ftp.storbinary("STOR %s" % fileName, readFile, buffer_size)

    readFile.close()

    # ftp.set_debuglevel(0)

    # ftp.quit()  #关闭ftp连接

def startUploadToFtp():
    ftp = ftpconnect()
    uploadfile(ftp)



if __name__ == "__main__":
    # startUploadToFtp()
    items =os.listdir(localDir)  # 遍历目录下所有文件名或文件夹名 返回一个list
    # dirs  = []
    # files = []
    # for path in items:
    #     item = os.path.join(localDir,path)
    #     if os.path.isdir(item):
    #         dirs.append(item)
    #     elif os.path.isfile(item):
    #         files.append(item)
    for root, dirs, files in os.walk(localDir):
        print(root)
        print(dirs)
        print(files)
        print("=========================")
        # break
