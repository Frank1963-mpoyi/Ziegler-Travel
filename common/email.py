from threading import Thread

from django.conf import settings
from django.core.mail import send_mail


class MakeAppointmentNotificationEmail(Thread):

    def __init__(self, appointment):
        super(MakeAppointmentNotificationEmail, self).__init__()
        self.appointment = appointment
        self.receiver = appointment.email1
        self.sender = settings.EMAIL_SENDER
        self.password = settings.EMAIL_PASSWORD
        self.subject = 'Appointment Confirmation'
        Thread.__init__(self)

    def run(self):
        self.send_appointment_notification()

    def send_appointment_notification(self):
        self.name = self.appointment.fullname
        self.firstname = self.name.upper()
        self.msg = f"""

Hi, {self.firstname}.
Phone Number: +27 (0) 781114041. 

Acacia Health got your email we will contact you soon to confirm the appointment.

Should you have any question, please contact Acacia Health.

Thanks,
ACACIA HEALTH,
Email: acacia@gmail.com
        """
        send_mail(
            f"{self.subject}",
            f"{self.msg}",
            self.sender,
            [f'{self.receiver}', ],
            fail_silently = False,
            auth_user = self.sender,
            auth_password = self.password
        )
        return