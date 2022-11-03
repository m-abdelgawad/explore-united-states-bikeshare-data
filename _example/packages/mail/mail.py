# Import mail modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path


def send(sender_mail, receivers_list, subject, body, attachs_list):

    smtpObj = smtplib.SMTP("10.230.95.91:25")
    sender = sender_mail

    receivers = receivers_list

    for receiver in receivers:
        report_message = MIMEMultipart()
        report_message["From"] = sender
        report_message["To"] = receiver
        report_message["Subject"] = subject
        # report_message.attach(MIMEText(email_body, 'html'))

        # email_body = MIMEText(mail_text)
        email_body = MIMEText(body, "html")
        report_message.attach(email_body)

        # Attach static plot files
        attachs = attachs_list

        for a in attachs:
            part = MIMEBase("application", "octet-stream")
            with open(a, "rb") as file:
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                'attachment; filename="{}"'.format(Path(a).name),
            )
            report_message.attach(part)

        try:
            smtpObj.sendmail(sender, receiver, report_message.as_string())
            
            print("Successfully sent report email to: ", str(receiver))
                        
        except smtplib.SMTPException as e:      
            print(e)       
            smtpObj.quit()

