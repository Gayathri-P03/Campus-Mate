from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GroupMessage
from .models import Result
from .models import Feedback
from .models import NoDueVerification
from .models import StudentProfileVerification
from .models import Assignment

admin.site.register(GroupMessage)
admin.site.register(Result)
admin.site.register(Feedback)
admin.site.register(NoDueVerification)
admin.site.register(StudentProfileVerification)
admin.site.register(Assignment)