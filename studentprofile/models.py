from django.db import models
from django.core.validators import EmailValidator

from core.models import BaseModel

class PersonalInfo(BaseModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True, null=True)
    summary = models.TextField()
    
    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"
    
    def __str__(self):
        return self.name

class Education(BaseModel):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.CharField(max_length=50)  # Can be "2018-2022" or similar
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-year']
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(BaseModel):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    period = models.CharField(max_length=50)  # Can be "2022 - Present" or similar
    description = models.TextField()
    
    class Meta:
        ordering = ['-period']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class SkillCategory(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Skill(BaseModel):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='skills')
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ['personal_info', 'category', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Project(BaseModel):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=500, blank=True)  # Comma-separated list
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Certification(BaseModel):
    personal_info = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name