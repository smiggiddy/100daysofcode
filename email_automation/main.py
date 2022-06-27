################################################################
#
# #100daysofcode Day-97 - Automation project
#
# By: SmigTech 
#
# email automation script for contacting agency 
################################################################


from email.mime.text import MIMEText
import smtplib
import datetime as dt 
import os 
from dotenv import load_dotenv 


load_dotenv()
MY_EMAIL = os.getenv('MY_EMAIL')
EMAIL_PASS = os.getenv('EMAIL_PASS')
TO_ADDY = os.getenv('TO_ADDY')



def send_email(subject, message):
    """Function sends email from message"""

    print(type(message))
    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = MY_EMAIL
    msg['To'] = TO_ADDY


    with smtplib.SMTP('smtp.mail.yahoo.com') as c: 
        c.starttls() 
        c.login(user = MY_EMAIL, password = EMAIL_PASS)

        try: 
            c.sendmail(
                from_addr= MY_EMAIL,
                to_addrs= TO_ADDY,
                msg=msg.as_string()
            )
            return True 

        except smtplib.SMTPResponseException as e:
            error_code = e.smtp_code 
            error_message = e.smtp_error 
            print(f'Errors found.\n{error_code}\n{error_message}')

            return False 
        
        except Exception as e:
            print(e)
            
            return False 


def load_message(): 
    """Reads message from text file and then sends message"""

    try: 
        with open('day-97/message.txt') as f: 
            message = f.readlines()
            subject = message[0]
            message = ' '.join(message[1:])
            return subject, message
    
    except FileNotFoundError as e: 
        print(f'Error File not found!! {e}')
        return None, None 



if __name__ == '__main__':

    subject, message = load_message() 
    if message:
        sent = send_email(subject=subject, message=message)
        if sent:
            print('Email message sent')
        else: 
            print('Email failed')
    else:
        print('Message file not found')


    





