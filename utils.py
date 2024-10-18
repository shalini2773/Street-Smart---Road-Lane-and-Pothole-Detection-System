"""
Utility Module
This module contains utility functions for sending email alerts.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

  def send_alert_email(toaddr, subject, body, attachment_path):
  """
  Send an alert email with an attachment.
  Args:
  toaddr (str): Recipient's email address.
  subject (str): Subject of the email.
  body (str): Body of the email.
  attachment_path (str): Path to the file to be attached.
  """

  fromaddr = "samplemail@gmail.com"
  
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))
  
  # Attach the file
  
  attachment = open(attachment_path, "rb")
  p = MIMEBase('application', 'octet-stream')
  p.set_payload(attachment.read())
  encoders.encode_base64(p)
  p.add_header('Content-Disposition', f"attachment; filename={attachment_path}")
  msg.attach(p)
 
 # Send the email
 
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login(fromaddr, "sample_password")  
  text = msg.as_string()
  s.sendmail(fromaddr, toaddr, text)
  s.quit()