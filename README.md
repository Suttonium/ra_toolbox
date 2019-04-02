# RA Toolbox

The data for residence life is currently stored in numerous google sheets, forms, and docs. This data is manually transferred from application to application and can cause inaccuracy when it comes to roster verifications, student security information, and room availability throughout campus. As a result of this confusion, RA toolbox is designed to centralize all of this data into one, unified database and will allow hall directors, resident assistants, and students to view a live update on information that pertains to their roles on campus. Hall directors will be able to view rosters for their building as well as view the student trackers maintained by their individual resident assistant staff members. Resident Assistants will be able to view their individual student rosters and maintain their trackers throughout the semester, and students and resident assistants alike will be able to view / update their student security information. 

## General Workflow
The system grants resident assistants and students the ability to sign up, designating which type of user they are (RA or student). If an RA attempts to sign up, the hall director for the building is emailed a verification email to assure non-resident assistant students cannot signup as RAs. After signing up, RAs are  sent an email to showcase their registration occurred correctly. This email houses a link for the RA to fill out their student security questions and student information cards. RAs will also be sent an access code in this email that they may send out to their residents. Once the residents receive this code, they then sign up and submit the activation code to get their RA and hallway assignment. They also receive an email with a security questions link. This builds a residence hall in the system and also builds the roster for the specified RA. RAs can then view their roster and view the individual trackers for each student. 

## Local Deployment 
In order to run this system, a few steps must be taken.
1) Pull the existing repository code to the IDE of your choice.
2) Once the code has been pulled, you must remove all of the current migrations folders.
     - Please refer to the following [link](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)  about resetting migrations.
3) If you followed any steps showcased throughout the above link, you should have already ran the below terminal commands while within your project directory to initialize your database and migrate your models.
     - ```python/python3 manage.py makemigrations```
     - ```python/python3 manage.py migrate```
     - If a models.py file is ever modified, be sure to run the above commands once again. 
     - If a db error occurs involving the ResidentAssistant model not existing, comment out the entirety of the          account/forms.py and accounts/views.py files, and comment our the urls within the accounts/urls.py file. Run the above commands once again and uncomment the files. 
4) Run the following commands to initialize the database with the proper data needed for site functionality including residence halls, desk accounts, and other needed models that need to be created upon residence hall generation. 
     - ```python/python3 manage.py create_residence_halls```
     - ```python/python3 manage.py genesis```

## Built With
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)


## Version Control
```
Python                    3.7
Django                    2.1.7
django-bootstrap-4        0.0.7
django-easy-audit         1.0.0
django-formtools          2.1
django-session-security   2.6.5
django-widget-tweaks      1.4.3
jQuery                    3.3.1
Bootstrap                 4.3.1
```



