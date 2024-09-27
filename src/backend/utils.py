from passlib.context import CryptContext
from passlib.utils import consteq
import random
import smtplib
import hashlib
import hmac
from email.mime.text import MIMEText


# Define CryptContext with pbkdf2_sha256
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256"
)

# Function to hash a password with salt

# Password hashing function (synchronous)
def get_password_hash(password: str, salt: str) -> str:
    # Hash the password with the salt using SHA256
    hashed_password = hmac.new(salt.encode(), password.encode(), hashlib.sha256).hexdigest()
    # Return the salt along with the hashed password
    return hashed_password

# Function to verify a password
# def verify_password(stored_password: str, provided_password: str) -> bool:
#     # Extract the salt and the hashed password
#     salt, hashed_password = stored_password.split('$', 1)
#     # Verify the provided password with the extracted salt
#     return pwd_context.verify(provided_password + salt, hashed_password)


def send_recovery_code(email: str):
    random_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # יצירת Hash באמצעות SHA-1
    recovery_code = hashlib.sha1(random_code.encode()).hexdigest()

    # הצגת התוצאה
    print(f"Random Code: {random_code}")
    print(f"SHA-1 Hash: {recovery_code}")

    # Create the email message
    msg = MIMEText(f"Your recovery code is: {recovery_code}")
    msg['Subject'] = 'Password Recovery Code'
    msg['From'] = 'comunicationltdproject2024@gmail.com'
    msg['To'] = email

    try:
        # Connect to the Gmail SMTP server
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('comunicationltdproject2024@gmail.com', 'zdfv dwpx kqzs xjiu')  # Use app-specific password if needed
        smtp.sendmail('comunicationltdproject2024@gmail.com', email, msg.as_string())
        smtp.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    return recovery_code