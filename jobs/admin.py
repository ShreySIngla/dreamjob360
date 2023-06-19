from django.contrib import admin
from .models import jobseeker,job,AppliedJob,userdetails,Contact,Subscription,blog
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from .filters import AlphabeticFilter
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    search_fields = ['subject', 'email',]
    readonly_fields = ('send_email',)

    def send_email(self, obj):

        subject = obj.rev_subject
        message = obj.rev_message
        from_email = 'shreylearning@gmail.com'
        recipient_list = ['shreylearning@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
        return format_html('<a href="#" class="btn btn-primary">Send Email</a>')
    
    send_email.short_description = 'Actions'
    
admin.site.register(Contact, ContactAdmin)

# class AlphabeticFilter(admin.SimpleListFilter):
#     title = _('Starting with Alphabet')
#     parameter_name = 'title'

#     def lookups(self, request, model_admin):
#         return (
#             ('a-z', 'A-Z'),
#             ('z-a', 'Z-A'),
#         )

#     def queryset(self, request, queryset):
#         if self.value() == 'a-z':
#             return queryset.order_by('title')
#         elif self.value() == 'z-a':
#             return queryset.order_by('-title')


class blogAdmin(admin.ModelAdmin):

    
    list_display = ('title', 'slug','created_on')
    # ordering = ['title']
    list_filter = [AlphabeticFilter,]
    search_fields = ['title', 'created_on']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(blog, blogAdmin)







class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email','subscribed_on')
    list_filter = ['subscribed_on']
    search_fields = ['email']
admin.site.register(Subscription, SubscriptionAdmin)

class jobseekerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','name','role_id')
    list_filter = ['role_id']
    search_fields = ['username', 'email']
admin.site.register(jobseeker, jobseekerAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('company','title', 'slug','img','created_on')
    list_filter = [AlphabeticFilter]
    search_fields = ['title', 'company']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(job, JobAdmin)

class userdetailsAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'experience')
    # Customize the displayed fields and behavior as needed

    def get_username(self, obj):
        return obj.jobseeker.username

    get_username.short_description = 'User'

admin.site.register(userdetails, userdetailsAdmin)

class AppliedJobAdmin(admin.ModelAdmin):
    list_display = ( 'jobseeker_email','job_title','job_company', 'view_job_details')
    search_fields = ['jobseeker__email', 'job__title']
    readonly_fields = ('jobseeker_name','jobseeker_email','jobseeker_phone','jobseeker_experience','jobseeker_age','jobseeker_gender','jobseeker_address','jobseeker_summery','job_title','job_company','job__created_on','job_location','job_salary')
    
    def view_job_details(self, obj):
        url = reverse('admin:jobs_appliedjob_change', args=[obj.job_id])
        return format_html('<a href="{}">View</a>', url)

    view_job_details.short_description = 'View Details'
 
    def jobseeker_gender(self, obj):
         return obj.jobseeker.userdetails.gender

    jobseeker_gender.short_description = 'Jobseeker Gender'



    def jobseeker_experience(self, obj):
        return obj.jobseeker.userdetails.experience
    
    jobseeker_experience.short_description = 'Jobseeker experience'


    def jobseeker_address(self, obj):
       return obj.jobseeker.userdetails.address
    
    jobseeker_address.short_description = 'Jobseeker address'



    def jobseeker_summery(self, obj):
        return obj.jobseeker.userdetails.summery
    
    jobseeker_summery.short_description = 'Jobseeker summery'


    def jobseeker_phone(self, obj):
        return obj.jobseeker.userdetails.phone
    
    jobseeker_phone.short_description = 'Jobseeker Phone'
     
    def jobseeker_age(self, obj):
        return obj.jobseeker.userdetails.age
    
    jobseeker_age.short_description = 'Jobseeker age'


    def jobseeker_name(self, obj):
       return obj.jobseeker.name
    
    jobseeker_name.short_description = 'Jobseeker name'

    def jobseeker_email(self, obj):
        return obj.jobseeker.email
    
    jobseeker_email.short_description = 'Jobseeker email'




    def job_title(self, obj):
        return obj.job.title

    job_title.short_description = 'Job Title'


    def job__created_on(self, obj):
        return obj.job.created_on
    
    job__created_on.short_description = 'job created on'


    def job_location(self, obj):
        return obj.job.location

    job_location.short_description = 'Job location'

    def job_salary(self, obj):
        return obj.job.salary

    job_salary.short_description = 'Job salary'

    def job_company(self, obj):
        return obj.job.company

    job_company.short_description = 'Job company'


    def has_add_permission(self, request):
        return False
    

    
    exclude=('job','jobseeker')

admin.site.register(AppliedJob, AppliedJobAdmin)







