from django.shortcuts import render

from rest_framework import generics,permissions,mixins,status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import User #import vote and post object
from .serializers import UserSerializer
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from datetime import datetime
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS,AllowAny
from phonenumber_field.formfields import PhoneNumberField
import phonenumbers




# Create your views here.

class UserCreate(generics.CreateAPIView):# list is not taken as no one want to see individual vote
	#this will make new vote object

	serializer_class=UserSerializer
	queryset = User.objects.all()
	permission_classes = [AllowAny]






	def perform_create(self,serializer):#name of this function must be same

		#validate email
		dob1 = self.request.POST['dateofbirth']
		#dob=datetime.strptime(dob)
		dob=datetime.strptime(dob1, "%Y-%m-%d").date()
		today = datetime.now()
		if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
			raise ValidationError('Must be at least 18 years old to register')
		    #return dob

		#validate phone no
		phone_number = self.request.POST['mobile_no']
		z = phonenumbers.parse(phone_number, "SG")
		if not phonenumbers.is_valid_number(z):
			raise ValidationError("Number not in SG format")
		    #return phone_number

		serializer.save()
		#current_site = get_current_site(request)
		mail_subject = 'Your detail saved succesfully'
		message = render_to_string('details/form_saved.html', {
		'name': self.request.POST['name'],
		'email': self.request.POST['email'],
		'mobile_no': self.request.POST['mobile_no'],
		'dateofbirth': self.request.POST['dateofbirth'],


		})
		#form1 = CreateUserForm(request.POST)
		#to_email = form1.cleaned_data.get('email')
		to_email=self.request.POST['email']
		email = EmailMessage(
				mail_subject, message, to=[to_email]
		)
		email.send()
