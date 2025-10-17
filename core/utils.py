
from django.core.mail import EmailMultiAlternatives
from requests.auth import HTTPBasicAuth
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def send_emails(subject, message, recipient_list:list, html_message: str = None):
    if not recipient_list or not message:
        return {"error": "Missing recipient or message"}
    email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list
    )

    if html_message:
        email.attach_alternative(html_message, "text/html")

    return email.send(fail_silently=False)


def send_sms(destinations:list, message):
    """
    Send an SMS using SMSPortal REST API
    """
    auth = HTTPBasicAuth(str(settings.SMS_API_KEY), str(settings.SMS_API_SECRET))

    payload = {
        "messages": [
            {"content": message, "destination": dest}
            for dest in destinations
        ]
    }

    try:
        response = requests.post(
            settings.SMS_PROVIDER_URL,
            auth=auth,
            json=payload,
            timeout=10  # optional: avoid hanging forever
        )

        # Check for success
        if response.status_code == 200:
            data = response.json()
            logger.info(f"SMS sent successfully: {data}")
            return {"success": True, "response": data}
        else:
            error = response.json()
            logger.error(f"SMS sending failed: {error}")
            return {"success": False, "error": error}

    except requests.RequestException as e:
        logger.exception("Error sending SMS")
        return {"success": False, "error": str(e)}

