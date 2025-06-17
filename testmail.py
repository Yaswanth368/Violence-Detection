import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

def send_email(
    sender_email: str,
    sender_password: str,
    recipient_emails: List[str],
    subject: str,
    body: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587
) -> bool:
    """
    Send an email using SMTP.
    
    Args:
        sender_email: Email address of the sender
        sender_password: Password or app-specific password for the sender's email
        recipient_emails: List of recipient email addresses
        subject: Subject line of the email
        body: Body content of the email
        smtp_server: SMTP server address (default: smtp.gmail.com)
        smtp_port: SMTP server port (default: 587)
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ', '.join(recipient_emails)
        message['Subject'] = subject
        
        # Add body to email
        message.attach(MIMEText(body, 'plain'))
        
        # Create SMTP connection
        server = smtplib.SMTP_SSL(smtp_server, 465)  # Changed to SMTP_SSL and port 465
        
        # Login
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(message, sender_email, recipient_emails)
        
        # Close connection
        server.quit()
            
        return True
        
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False