import re
import smtplib
from email.mime.text import MIMEText

from dundie.settings import SMTP_HOST, SMTP_PORT, SMTP_TIMEOUT
from dundie.utils.log import get_logger

log = get_logger()


def check_valid_email(address):
    """Return True if email is valid"""
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return bool(re.fullmatch(pattern, address))


def send_email(from_, to_, subject, text):
    if not isinstance(to_, list):
        to_ = [to_]

    try:
        with smtplib.SMTP(
            hst=SMTP_HOST, port=SMTP_PORT, timeout=SMTP_TIMEOUT
        ) as server:
            message = MIMEText(text)
            message["Subject"] = subject
            message["From"] = from_
            message["To"] = ",".join(to_)
            server.sendmail(from_, to_, message.as_string())

    except Exception:
        log.error("Cannot send email to %s", to_)
