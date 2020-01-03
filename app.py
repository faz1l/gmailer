import os
import sys
import smtplib
from termcolor import cprint

def send_mail():
    cprint("Enter your gmail username:", "blue")
    gmail_user = input(">>> ")
    cprint("Enter your gmail password: ", "blue")
    gmail_password = input(">>> ")

    sent_from = gmail_user
    cprint("Enter the destination email: ", "blue")
    to = input(">>> ")
    cprint("Enter the email subject: ", "blue")
    subject = input(">>> ")
    cprint("Enter the email body: ", "blue")
    body = input(">>> ")

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        cprint("\n[Success] Email have been sent!", "green")
        cprint("\nDo you want to send more email's?\n", "blue")
        more = input(">>> ")

        if more.lower() == "yes" or more.lower() == "y":
            os.system("clear")
            send_mail()
        else:
            cprint("\n\nGoodbeye!\n", "blue")
    except:
        cprint("\n[Error] Something went wrong...", "red")
        cprint("\nDo you wish to restart the app?", "blue")
        restart = input(">>> ")
        if restart.lower() == "yes" or restart.lower() == "y":
            os.system("clear")
            os.execl(sys.executable, sys.executable, * sys.argv)
        else:
            os.system("clear")
            cprint("\n\nGoodbeye!\n", "blue")

if __name__ == "__main__":
    os.system("clear")
    cprint("\n\n***___GMAIL MESSAGE SENDER___***\n\n", "green")
    send_mail()