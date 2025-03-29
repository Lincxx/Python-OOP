# abstraction
#reduce complexity by hiding unnecessary details and exposing only the necessary information to the user.

class EmailService:

    def _connect(self):
        print("Connecting to email server...")

    def _authenticate(self):
        print(f"Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print(f"Sending email to...")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from email server...")


email_service = EmailService()
email_service.send_email()

    