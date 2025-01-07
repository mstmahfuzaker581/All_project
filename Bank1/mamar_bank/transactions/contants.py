from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
DEPOSIT = 1
WITHDRAWAL = 2
LOAN = 3
LOAN_PAID = 4
SEND_MONEY = 5
RECEIVE_MONEY = 6
TRANSACTION_TYPE = (
    (1, 'Deposit'),
    (2, 'Withdrawal'),
    (3, 'Loan'),
    (4, 'Loan paid'),
    (5, 'Send money'),
    (6, 'Receive money'),
)


def send_mail_to_user(subject, template_name, context, receiver):
    mail_subject = subject
    sender_mail_message = render_to_string(template_name, context)
    mail = EmailMultiAlternatives(mail_subject, '', to=[receiver])
    mail.attach_alternative(sender_mail_message, 'text/html')
    mail.send()