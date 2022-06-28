from calendar import c
import smtplib, ssl

class Mail:
    def __init__(self):
        self.port = 465 # The correct port when using SMTP_SSL below
        self.smpt_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "bengsklockserver@gmail.com"
        self.reciever_mail = "bengs.joel@gmail.com"
        self.password = input("Type your password and press enter: ")


    # SSL is encrypted
    def send(self, forum, title, userName, url):
        # Sets protocols, certificates etc
        ssl_context = ssl.create_default_context() 
        # Conects to an encrypted server at gmail port 465
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        # Login using credientials from constructor
        service.login(self.sender_mail, self.password)

        subject = f"{forum}: {title}"
        content = f"\"{title}\" was just listed on {forum} by {userName}\nURL: {url}"
        
        result = service.sendmail(self.sender_mail, self.reciever_mail, f"Subject: {subject}\n{content}")
        service.quit()

if __name__ == '__main__':
    mails = input("Enter emails: ").split()
    subject = input("Enter subject: ")
    content = input("Enter content: ")

    mail = Mail()
    mail.send(mails, subject, content)