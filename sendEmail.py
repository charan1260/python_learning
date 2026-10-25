import os
import smtplib
import mimetypes
from email.message import EmailMessage


def create_message(sender, receiver, subject, body, attachment_path=None):
    """
    Builds the email object.
    - sender / receiver: email addresses
    - subject: the email subject line
    - body: the plain text content
    - attachment_path: optional path to a file to attach
    """
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        add_attachment(msg, attachment_path)

    return msg


def add_attachment(msg, file_path):
    """
    Attaches a file to an existing message.
    It guesses the file type (pdf, png, etc.) from the file name,
    then reads the file in binary mode and adds it to the email.
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = "application/octet-stream"
    maintype, subtype = mime_type.split("/", 1)

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype=maintype,
            subtype=subtype,
            filename=os.path.basename(file_path),
        )


def send_email(msg, smtp_server, port, username, password):
    """
    Connects to the SMTP server, logs in, and sends the message.
    - SMTP_SSL on port 465 encrypts the connection from the start.
    - The 'with' block closes the connection automatically.
    """
    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(username, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Login failed: check your email or app password.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    """
    Collects the settings and ties everything together.
    Credentials are read from environment variables so the
    password is never written in the code.
    """
    sender = "lingalacharan777@gmail.com"
    password = "sqakrfpjuvizfbgq"

    msg = create_message(
        sender=sender,
        receiver="lingalasricharan66@gmail.com",
        subject="Hello from Python",
        body="Hi,\n\nThis email was sent using a Python script.\n\nRegards,\nCharan",
        attachment_path=None,  # e.g. "resume.pdf"
    )

    send_email(msg, "smtp.gmail.com", 465, sender, password)


if __name__ == "__main__":
    main()