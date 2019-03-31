import socket
import os
import sys
import struct
import _thread
import datetime

import process as process
# import identifyPic as ip

def socket_service_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.bind(('127.0.0.1', 6666))
        s.bind(('', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait for Connection.....................")

    while True:
        sock, addr = s.accept()  #addr是一个元组(ip,port)
        try:
            _thread.start_new_thread(deal_image, (sock, addr))
        except:
            print("ERROR: unable to start thread!")    

def makePath(addr):
    dt = datetime.datetime.now()
    # new_path = addr[0] + '\\' + dt.strftime('%Y%m%d%H%M%S%f') # for win
    new_path = addr[0] + '/' + dt.strftime('%Y%m%d%H%M%S%f') # for linux
    try: 
        os.makedirs(new_path)
        return new_path
    except:
        return makePath(addr)


def deal_image(sock, addr):
    print("Accept connection from {0}".format(addr))  #查看发送端的ip和端口

    while True:
        print("")
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)   #接收图片名
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')

            new_path = makePath(addr)
            new_filename = os.path.join(new_path, fn)  #在服务器端新建图片名

            recvd_size = 0
            fp = open(new_filename, 'wb')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)  #写入图片数据
            fp.close()
        break

    # os.system("python process.py %s %s"%(new_path, fn))   # for win
    if os.popen("python3 process.py %s %s"%(new_path, fn)):   # for linux
        sock.send("1".encode())

    sock.close()
    # import emailSender as emailSender
    # identifier = ip.identifyPic(new_path)
    # prediction = identifier.predict()
    # if prediction < 0.5:
    #     mail_username='zh4055526@gmail.com'
    #     mail_password='!1q@2w#3e'
    #     # from_addr = mail_username
    #     to_addrs="646618065@qq.com"
         
    #     # HOST & PORT
    #     HOST = 'smtp.gmail.com'
    #     PORT = 587
         
    #     # mail_username, mail_password, to_addrs, HOST, PORT
    #     email = emailSender.emailSender(mail_username, mail_password, to_addrs, HOST, PORT, new_path+'\\'+fn)
    #     email.send()

    # print("finish")
    # _thread.exit()
        
if __name__ == '__main__':
    socket_service_image()