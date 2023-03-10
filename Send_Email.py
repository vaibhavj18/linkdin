# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:06:11 2023

@author: user
"""
import smtplib, ssl
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Jobs scrapped from LinkedIn"
body = "This is an email with attachment sent from Python"
sender_email = "automatedmailreport@gmail.com"
password = 'lrqncravnsocvlkn'
# receiver_email = "mayursuryavan@gmail.com"


def send_the_data(receiver_email,save_dir,save_file_name,curr,mail_content):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    # message = mail_content
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message['CC'] = receiver_email
    # message["Bcc"] = receiver_email  # Recommended for mass emails
    # print('receiver_email',receiver_email)
    # Add body to email
    message.attach(MIMEText(mail_content, "plain"))
    os.chdir(save_dir)
    filename = save_file_name#"Demo_data.csv"  # In same directory as script
    # filename = "Linkedin_Job_Today.csv"
    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)
    
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    ) 
    
    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    os.chdir(curr)
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email.split(","), text)
        # server.sendmail(sender_email,  receiver_email.split(",") + (receiver_email.split(",") if receiver_email else []), text)
