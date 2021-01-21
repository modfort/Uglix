from client import *

class Conn:
		
	def __init__(self,user="rodgersbrett",password="!uFSXeNd%2"):
		self.user=user
		self.password=password
		self.conn=Connection()
		self.helpdesk="/bin/crypto_helpdesk"
		self.path_home="/home/"+self.user
		self.mail=self.path_home+"/INBOX"
		rep=self.conn.post("/bin/login",user=user,password=password)
		print(rep)

	
	def echo(self,msg):
		return self.conn.post("/bin/echo",msg=msg)
		
	

	def get(self,path):
		return self.conn.get(path)
				
	def get_inbox(self):
		return self.get(self.mail)
	def get_mail2(self,number):
		return (self.conn.get(self.mail+"/"+str(number)))
	
	
	def get_mail(self,f,number):
		mail=self.conn.get(self.path_home+"/INBOX/"+str(number))
		f = open(f,"w")
		f.write(mail)
		f.close()
	
	def send_mail(self,to,sub,cont):
		self.conn.post("/bin/sendmail",to=to,subject=sub,content=cont)

	def get_ticket_all(self):
		return self.get(self.helpdesk)
		
	
	def get_ticket(self,num):
		return self.get(self.helpdesk+"/ticket/"+str(num))
	
	def get_storage(self,num):
		return self.get("/bin/long-term-storage/"+str(num))



	
	def print_att(self,num,att):
		return self.get(self.helpdesk+"/ticket/"+str(num)+"/attachment/"+str(att))
	

	"""
	def get_all_mail(self,f,mode="w"):
		with open("all_mail.txt",mode) as f:
			

	def 
"""

"""

fichier a voir /bin/crypto_helpdesk

with open("mail.txt","a") as f:
	for i in range(4009,4033):
		txt=a.get("/home/"+a.user+"/INBOX/"+str(i))
		if(txt == None):
			break
		print(txt)
		f.write(str(txt))
"""

