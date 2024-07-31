from imap_tools import MailBox, AND
import os
def retrieve_messages(number_of_emails):
    with MailBox('imap.gmail.com').login(os.getenv('EMAIL_ID'), os.getenv('EMAIL_PASSWORD')) as mailbox:
        count=0
        message_details=[]
        for msg in mailbox.fetch():
            message_details.append([msg.date, msg.subject,msg.from_])
            print(msg.date, msg.subject, len(msg.text or msg.html),msg.from_)
            count+=1
            if count==number_of_emails:
                break
        return message_details

