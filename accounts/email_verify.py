from django.core.mail import send_mail
from django.conf import settings

def sendemail(email, token):
    subject = "Your account verification email"
    message = f'Please click on this link for account verification: http://127.0.0.1:8000/api/accounts/verifytoken/{token}'
    email_from = settings.EMAIL_HOST_USER

    html_message = f"""
    <html>
    <body>
        <h1 style="color: #333;">Account Verification</h1>
        <p style="color: #666;">
            Please click on the link below to verify your account:
        </p>
        <p>
            <a href="http://127.0.0.1:8000/api/accounts/verifytoken/{token}" 
               style="display: inline-block; padding: 10px 20px; font-size: 16px; color: #fff; background-color: #007bff; text-decoration: none; border-radius: 5px;">
                Verify Account
            </a>
        </p>
        <p style="color: #666;">
            If you did not request this verification, please ignore this email.
        </p>
    </body>
    </html>
    """

    send_mail(subject, message, email_from, [email], html_message=html_message)
