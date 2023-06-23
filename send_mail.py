import smtplib
from email.mime.text import MIMEText
#this is a sample text
def send_email():
    sender_email = "ravipreethi645@gmail.com"
    receiver_email = "vijayjohn7345@gmail.com"
    subject = "Test Email"
    message = "Hi this is Preethi. You Have a Scrum call @10:30 A.M ."

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, "vejm hvle fgun ioxt")
        smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
        smtp_server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Error: unable to send email.")
        print(e)

if __name__ == "__main__":
    send_email()
