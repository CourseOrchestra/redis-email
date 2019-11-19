import datetime
import mimetypes
import smtplib
from email.message import EmailMessage
from email.utils import make_msgid
from typing import List

from redis import Redis
from rq import Queue
import config

conn = Redis.from_url(config.REDIS_URL)
smtp = smtplib.SMTP_SSL if config.MAIL_USE_SSL else smtplib.SMTP
server = smtp(config.MAIL_SERVER, config.MAIL_PORT)

if config.MAIL_USE_TLS:
    server.starttls()
server.ehlo()

if config.MAIL_USERNAME:
    server.login(config.MAIL_USERNAME, config.MAIL_PASSWORD)
q = Queue('email', connection=conn, default_timeout=config.DEFAULT_TIMEOUT)


def email(sender: str, receiver: List, subject: str, **kwargs):
    content = kwargs.pop('content', '')
    content_html = kwargs.pop('content_html')
    attachments = kwargs.pop('attachments', {})
    if isinstance(receiver, str):
        receiver = [receiver]
    msg = EmailMessage()

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(receiver)
    msg['Date'] = datetime.datetime.utcnow()
    msg.add_header('MIME-Version', '1.0')
    msg.add_header('Message-Id', make_msgid())
    msg.add_alternative(content)

    if content_html:
        msg.add_alternative(content_html, subtype='html')
    for filename, data in attachments.items():
        c_type, encoding = mimetypes.guess_type(filename)
        if c_type is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            c_type = 'application/octet-stream'
        maintype, subtype = c_type.split('/', 1)
        msg.add_attachment(data,
                           maintype=maintype,
                           subtype=subtype,
                           filename=filename)
    server.send_message(msg)
