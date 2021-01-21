from client import *

class Conn:
		
	def __init__(self):
		try:
			cred=open("mdp.txt","r").read().split(":")
			
			self.user=cred[0]
			self.password=cred[1]
		except:
			print("file mdp not found you have to tape your cred\n the file have to be in the format <username>:<password>")
			self.user=input("username:")
			self.password=input("password:")
		self.conn=Connection()
		self.helpdesk="/bin/crypto_helpdesk"
		self.path_home="/home/"+self.user
		self.mail=self.path_home+"/INBOX"
		while(True):
			try:
				rep=self.conn.post("/bin/login",user=self.user,password=self.password)
				break
			except:
				print("error in the credential please give the right username or quit and give a file with the crendtial")
				self.user=input("give username:")
				self.password=input("give password:")

		print(rep)

	
	def echo(self,msg):
		return self.conn.post("/bin/echo",msg=msg)
		
	

	def get(self,path):
		return self.conn.get(path)
	
	
	def post(self,path,thing):
		return self.conn.post(path,thing)

	
	def get_inbox(self):
		return self.get(self.mail)

#this help to get the last email


	def gLmail(self):
		return self.get_mail2(int(self.get_inbox().split("\n")[5].split("  ")[1]))
	
	def get_mail2(self,number):
		return (self.conn.get(self.mail+"/"+str(number)))
	
	def getAllmailInFile(self,file):
		mail=self.get_inbox().split("\n")[5:]
		l=[]
		for i in mail:
			if i =="":
				mail.remove("")
		for i in mail:
			try:
				l.append(int(i.split("  ")[1]))
			except:
				continue
		with open(file,"w") as f:
			for e in l:
				f.write(self.get_mail2(e))	

	def getNLastmail(self,file,n):
		mail=self.get_inbox().split("\n")[5:]
		l=[]
		for i in mail:
			if i =="":
				mail.remove("")
		for i in mail:
			try:
				l.append(int(i.split("  ")[1]))
			except:
				continue
		print(l)
		l=l[:n]
		print("après")
		print(l)			
		with open(file,"w") as f:
			for e in l:
				f.write(self.get_mail2(e))			
			
	def get_mail(self,f,number):
		mail=self.conn.get(self.path_home+"/INBOX/"+str(number))
		f = open(f,"w")
		f.write(mail)
		f.close()
	
	def send_mail(self,to,sub,cont):
		self.conn.post("/bin/sendmail",to=to,subject=sub,content=cont)

	def get_ticket_all(self):
		return self.get(self.helpdesk)
		

	def close_ticket(self,num):
		return self.post("/bin/crypto_helpdesk/ticket/"+str(num)+"close"," ")



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

