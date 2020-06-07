Job :
    - title
    - location
    - job type
    - description
    - published at
    - vacanvy
    - salary
    - category
    - experience
    - gender

    - apply job
    - post job

Blog :
    - title
    - descriptipn
    - create at 
    - category
    - tags
    - author

    - search
    - comment
    - recent post

Contact
Home
Login



    JOB
    JOBVacanvy = models.CharField()
    JOBSalary = models.DecimalField()
    JOBCategory = models.ForeignKey()
    JOBExperience = models.CharField()
    JOBGender = models.CharField()
    '''

 
 
   class Meta:
        verbose_name = _("job")
        verbose_name_plural = _("jobs")
