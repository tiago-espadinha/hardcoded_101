import argparse
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from utils import logger

def send_email(args):
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    
    if not user or not password:
        logger.error("EMAIL_USER or EMAIL_PASS environment variables not set.")
        return

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = args.to
    msg['Subject'] = args.subject

    # Handle body
    body_content = args.body
    if Path(args.body).exists():
        with open(args.body, 'r', encoding='utf-8') as f:
            body_content = f.read()
    
    body_type = 'html' if body_content.strip().startswith('<') else 'plain'
    msg.attach(MIMEText(body_content, body_type))

    # Handle attachments
    if args.attach:
        for attachment in args.attach.split(','):
            attach_path = Path(attachment.strip())
            if not attach_path.exists():
                logger.warn(f"Attachment not found: {attachment}")
                continue
            
            with open(attach_path, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={attach_path.name}",
            )
            msg.attach(part)

    try:
        with smtplib.SMTP(args.smtp, args.port) as server:
            server.starttls()
            server.login(user, password)
            text = msg.as_string()
            server.sendmail(user, args.to.split(','), text)
            logger.info(f"Email sent successfully to {args.to}")
    except Exception as e:
        logger.error(f"Failed to send email: {e}")

def main():
    parser = argparse.ArgumentParser(description="CLI Email Sender.")
    parser.add_argument("--to", required=True, help="Recipient email(s) separated by commas")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Inline text or path to .txt/.html file")
    parser.add_argument("--attach", help="Paths to files to attach, comma-separated")
    parser.add_argument("--smtp", default="smtp.gmail.com", help="SMTP host (default: smtp.gmail.com)")
    parser.add_argument("--port", type=int, default=587, help="SMTP port (default: 587)")

    args = parser.parse_args()
    send_email(args)

if __name__ == "__main__":
    main()
