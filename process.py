import identifyPic as ip
import emailSender as emailSender
import sys
import shutil

def process(path, fn):
    print("****path: ", path)
    identifier = ip.identifyPic(path)
    prediction = identifier.predict()
    if prediction < 0.5:
        mail_username='zh4055526@gmail.com'
        mail_password='!1q@2w#3e'
        # from_addr = mail_username
        to_addrs="646618065@qq.com"
         
        # HOST & PORT
        HOST = 'smtp.gmail.com'
        PORT = 587
         
        # mail_username, mail_password, to_addrs, HOST, PORT
        # email = emailSender.emailSender(mail_username, mail_password, to_addrs, HOST, PORT, path+'\\'+fn)  # for win
        email = emailSender.emailSender(mail_username, mail_password, to_addrs, HOST, PORT, path+'/'+fn)     # for linux

        email.send()
    else:
	    shutil.rmtree(path)
	    print("*** Folder deleted! ***")

if __name__ == "__main__":
    process(sys.argv[1], sys.argv[2])