import smtplib, ssl

class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "bengsklockserver@gmail.com"
        self.password = "wallnutC4"

    def send(self, email, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()


if __name__ == '__main__':
    email = "bengs.joel@gmail.com"
    subject = "test1"
    content = "test2"

    mail = Mail()
    mail.send(email, subject, content)
