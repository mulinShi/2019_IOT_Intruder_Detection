import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class emailSender(object):
	"""docstring for emailSender"""
	def __init__(self, mail_username, mail_password, to_addrs, HOST, PORT):
		self.mail_username = mail_username
		self.mail_password = mail_password
		self.from_addr = self.mail_username
		self.to_addrs = to_addrs
		
		self.HOST = HOST
		self.PORT = PORT

	def generateMsg(self):
		msg = MIMEMultipart()
		msg['Subject'] = "Warning"
		msg['From'] = "Watchdog"
		msg['To'] = self.to_addrs
		# print("================")
		# print(";".join(self.to_addrs))

		mail_msg = """
			<p>Hey!</p> 
			<p>Take care! Someone entered your house!</p>
			<p>Here is the picture:</p>
			<p><img src="cid:img" style="width:100%"></p>
		"""
		
		msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))

		f = open(r"./raw/test/0.jpg", 'rb')
		img = MIMEImage(f.read())
		f.close()

		img.add_header('content-ID', '<img>')
		msg.attach(img)

		return msg

	def send(self):
		msg = self.generateMsg()
		smtp = smtplib.SMTP()

		# try:
		try:
			print("*** Connecting...")
			smtp.connect(self.HOST, self.PORT)
		except:
			print("*** connect error!")
		smtp.starttls()
		try:
			print("*** Logging in...")
			smtp.login(self.mail_username, self.mail_password)
		except:
			print("*** Login error!")
		print("*** Sending...")
		smtp.sendmail(self.from_addr, self.to_addrs, msg.as_string())
		smtp.quit()
		print('Success!')
		
		return

 
if __name__ == '__main__':
	# my test mail
	mail_username='zh4055526@gmail.com'
	mail_password='!1q@2w#3e'
	# from_addr = mail_username
	to_addrs="617946318@qq.com"
	 
	# HOST & PORT
	HOST = 'smtp.gmail.com'
	PORT = 587
	 
 	# mail_username, mail_password, to_addrs, HOST, PORT
	email = emailSender(mail_username, mail_password, to_addrs, HOST, PORT)
	email.send()