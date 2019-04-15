NAME_LIMIT = 30
STUDENT_ID_MAX_LIMIT = 8
STUDENT_ID_MIN_LIMIT = 6
ACTIVATION_CODE_LIMIT = 12  # django.crypto default length
FIRST_NAME = 0
LAST_NAME = 1
ATCNUEDU = '@cnu.edu'
hall_director_list = [
    'mary.taylor1@cnu.edu', 'melissa.lourie@cnu.edu', 'elizabeth.beavers@cnu.edu', 'rachel.conners@cnu.edu',
    'danny.lee@cnu.edu', 'beth.tucker@cnu.edu', 'rachael.beattie@cnu.edu '
]

desk_account_email_list = [
    'jamesriverhall@cnu.edu', 'eastcampus@cnu.edu', 'yorkrivereast@cnu.edu', 'yorkriverwest@cnu.edu',
    'potomacrivernorth@cnu.edu', 'potomacriversouth@cnu.edu',
    'rappahannockriverhall@cnu.edu', 'santorohall@cnu.edu', 'warwickriverhall@cnu.edu'
]

desk_account_permissions = [
    'change_equipmentlog', 'view_equipmentlog', 'add_equipmentlogentry', 'change_equipmentlogentry',
    'view_equipmentlogentry', 'change_guestlog', 'view_guestlog', 'add_guestlogentry', 'change_guestlogentry',
    'view_guestlogentry', 'add_lockoutcode', 'change_lockoutcode', 'view_lockoutcode', 'change_lockoutlog',
    'view_lockoutlog', 'view_lockoutlogentry', 'change_passdownlog', 'view_passdownlog', 'add_passdownlogentry',
    'change_passdownlogentry', 'view_passdownlogentry', 'change_securityquestions', 'view_securityquestions',
    'view_studentinformationcard', 'change_studentinformationcard'
]

student_account_permissions = [
    'change_studentinformationcard', 'view_studentinformationcard', 'change_securityquestions', 'view_securityquestions'
]

resident_assistant_account_permissions = [
    'add_room', 'change_room', 'view_room', 'add_suite', 'change_suite', 'view_suite', 'change_tracker', 'view_tracker',
    'change_studentinformationcard', 'view_studentinformationcard', 'change_securityquestions', 'view_securityquestions'
]

hall_director_account_permissions = [
    'view_securityquestions', 'change_securityquestions', 'add_room', 'change_room', 'view_room', 'add_suite',
    'change_suite', 'view_suite',
    'change_tracker', 'view_tracker', 'view_studentinformationcard', 'change_studentinformationcard'
]
