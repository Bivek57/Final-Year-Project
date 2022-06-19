from django.conf import settings  
from django.core.mail import EmailMultiAlternatives  
from django.template.loader import get_template


def mail_system(
    param_mail_subject, param_template_name, param_context_mail, param_user_mail  #required parameters passed
):
    # MAIL SYSTEM
    htmly = get_template(param_template_name)
    subject, form_mail, to = (
        param_mail_subject,
        settings.EMAIL_HOST_USER,
        param_user_mail,  #making variables
    )

    
    html_content = htmly.render(param_context_mail)  #context mail data kept in html template
    msg = EmailMultiAlternatives(subject, html_content, form_mail, [to])   #variable message stores subject, html content and form mail
    msg.attach_alternative(html_content, "text/html")  #All the binded data of html are attached in message and was sent
    return msg.send()
