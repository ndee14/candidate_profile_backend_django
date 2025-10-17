import os
import sys
import django

# --- Add project root (directory containing manage.py) to PYTHONPATH ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- Tell Django where to find your settings ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# --- Setup Django ---
django.setup()

# --- Now import and test ---
from core.utils import send_sms, send_emails


def test_sms():
    phone_number = ["0711324481", "0713329064", "0601571897"]  # Replace with your test number
    result = send_sms(phone_number, "Hello from Django + SMSPortal!")
    print(result)

def test_email():
    subject = "test message"
    recipient_list = ["khumbeloprince@gmail.com"]
    message = "hy just testing"
    result = send_emails(subject, message, recipient_list)
    print(result)

if __name__ == "__main__":
    test_email()
