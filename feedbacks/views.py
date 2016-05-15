# encoding: utf-8
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import CreateView

from feedbacks.models import Feedback
from pybursa.settings import ADMINS

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives



class FeedbackView(CreateView):
    model = Feedback
    template_name = 'feedback.html'
    success_url = reverse_lazy('feedback')
    fields = '__all__'

    def form_valid(self, form):
        mail_form = form.save()
        mail_to = list()
        for name, mail in ADMINS:
            mail_to.append(mail)
        #send_mail(mail_form.subject, mail_form.message, mail_form.from_email, mail_to, fail_silently = False)
        mail = EmailMultiAlternatives(
            subject="Your Subject",
            body=mail_form.message, #"Text from my feedback form",
            from_email="Nick_admin_Pybursa <nickmetal92@gmail.com>",
            to=mail_to,
            headers={"Reply-To": "nickmetal92@gmail.com"}
        )

        mail.send()

        message =  u"Thank you for your feedback! We will keep in touch with you very soon!"
        messages.success(self.request, message)
        return super(FeedbackView, self).form_valid(form)
