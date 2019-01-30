from django.utils.translation import ugettext_lazy as _

PHONE_NUMBER_MAX_LIMIT = 17
PHONE_NUMBER_MIN_LIMIT = 10
ADDRESS_MAX_LIMIT = 100
STATE_LENGTH = 100
STATE_ABBREVIATIONS = (
    ('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'),
    ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'),
    ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'),
    ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'),
    ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'),
    ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'),
    ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'),
    ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'),
    ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'),
    ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'),
    ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'),
    ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'),
    ('American Samoa', 'American Samoa'), ('District of Columbia', 'District of Columbia'),
    ('Federated States of Micronesia', 'Federated States of Micronesia'), ('Guam', 'Guam'),
    ('Marshall Islands', 'Marshall Islands'), ('Northern Mariana Islands', 'Northern Mariana Islands'),
    ('Palau', 'Palau'), ('Puerto Rico', 'Puerto Rico'), ('Virgin Islands', 'Virgin Islands')
)
ZIP_CODE_LENGTH = 5
EC_NAME_LENGTH = 30
EC_RELATIONSHIP_TO_STUDENT_LENGTH = 20
MAX_DATE_LENGTH = 10
ALLERGIES = _('Please list any allergies.')
MEDICATIONS = _('Please list any medications you are currently using.')
