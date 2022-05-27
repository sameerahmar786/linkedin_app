from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    USER_TYPE = (
        ('jobseeker', 'Job Seeker'),
        ('company', 'Company'),
    )
    user_id = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE)
    usertype_name = models.CharField(
        max_length=9, choices=USER_TYPE, null=True)

    def get_usertype(id):
        return UserAccount.objects.get(user_id=id).usertype_name


class SeekerProfile(models.Model):
    ANNUALY_MONTHLY = (
        ('annualy', 'Annualy'),
        ('monthly', 'Monthly'),
    )
    useraccount_id = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    current_salary = models.IntegerField()
    is_annualy_monthly = models.CharField(
        max_length=7, choices=ANNUALY_MONTHLY)
    currency = models.CharField(max_length=50)

    def current_object(id):
        return SeekerProfile.objects.get(useraccount_id=id)


class EducationDetail(models.Model):
    seekerprofile_id = models.ForeignKey(
        SeekerProfile, on_delete=models.CASCADE)
    degree_name = models.CharField(max_length=50, primary_key=True)
    institute_name = models.CharField(max_length=50)
    starting_date = models.DateField()
    completition_date = models.DateField()
    percentage = models.FloatField()
    cgpa = models.FloatField()

    def seeker_education(jobseeker):
        return jobseeker.educationdetail_set.first()

    def seeker_education_all(jobseeker):
        return jobseeker.educationdetail_set.all()


class ExperienceDetail(models.Model):
    IS_CURRENT_JOB = (
        ('true', 'True'),
        ('false', 'False'),
    )
    seekerprofile_id = models.ForeignKey(
        SeekerProfile, on_delete=models.CASCADE)
    is_current_job = models.CharField(
        max_length=5, choices=IS_CURRENT_JOB)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()
    start_date = models.DateField(primary_key=True)
    end_date = models.DateField()
    company_name = models.CharField(max_length=50)
    company_address = models.TextField()

    def seeker_experience(jobseeker):
        return jobseeker.experiencedetail_set.first()

    def seeker_experience_all(jobseeker):
        return jobseeker.experiencedetail_set.all()


class SeekerSkillSet(models.Model):
    SKILL_LEVEL = (
        ('beginner', 'Beginner'),
        ('average', 'Average'),
        ('skilled', 'Skilled'),
        ('specialist', 'Specialist'),
        ('expert', 'Expert'),
    )
    seekerprofile_id = models.ForeignKey(
        SeekerProfile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50, primary_key=True)
    skill_level = models.CharField(
        max_length=10, choices=SKILL_LEVEL)

    def seeker_skillset(jobseeker):
        return jobseeker.seekerskillset_set.first()

    def seeker_skillset_all(jobseeker):
        return jobseeker.seekerskillset_set.all()


class Company(models.Model):
    useraccount_id = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=50)
    company_description = models.TextField()
    establishment_date = models.DateField()
    company_website_url = models.URLField()

    def current_object(id):
        return Company.objects.get(useraccount_id=id)


class JobType(models.Model):
    JOB_TYPE = (
        ('fulltime', 'Full Time'),
        ('parttime', 'Part Time'),
    )
    jobtype = models.CharField(max_length=8, choices=JOB_TYPE)


class JobLocation(models.Model):
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.IntegerField()


class JobPost(models.Model):
    IS_ACTIVE = (
        ('true', 'True'),
        ('false', 'False'),
    )
    jobtype_id = models.ForeignKey(JobType, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    joblocation_id = models.ForeignKey(JobLocation, on_delete=models.CASCADE)
    job_description = models.TextField()
    created_date = models.DateField()
    is_active = models.CharField(max_length=5, choices=IS_ACTIVE)

    def company_jobpost_all(company):
        return company.jobpost_set.all()


class JobPostActivity(models.Model):
    seekerprofile_id = models.ForeignKey(
        SeekerProfile, on_delete=models.CASCADE)
    jobpost_id = models.ForeignKey(
        JobPost, on_delete=models.CASCADE)
    apply_date = models.DateField()
