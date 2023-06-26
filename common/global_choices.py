# USER TYPES
USER_TYPE = (
    (1, 'MPT Systems'),# Mpoyi Tshibuyi Systems
    (2, 'HP Staff'),# Tshibuyi Hospiteal Staff
    (3, 'Customer'),# Customer
)

# USER LEVEL TYPES
USER_LEVEL = (
    (1,1),# View & Popular for All
    (2,2),
    (3,3),# View Most but Edit limited
    (4,4),
    (5,5) # All Access
)

DEPARTMENTS = (
    ('General Health', 'General Health'),
    ('Orthopaedic', 'Orthopaedic'),
    ('Neurology', 'Neurology'),
    ('Cardiologist','Cardiologist'),
    ('Dermatologists','Dermatologists'),
    ('Emergency Medicine Specialists','Emergency Medicine Specialists'),
    ('Allergists/Immunologists','Allergists/Immunologists'),
    ('Anesthesiologists','Anesthesiologists'),
    ('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
    ('Dental', 'Dental')
)

# ISSUES TYPES
ISSUE_TYPE = (
    (1, 'Bug'), # Bug
    (2, 'Enhancement'), # Enhancement
)

# LANGUAGES
LANGUAGES = (
    ('EN', 'English'),
    ('FR', 'French'),
    ('DE', 'German'),
    ('PT', 'Portuguese'),
    ('ES', 'Spanish'),
)

# STATUS TYPES
STATUS_TYPE = (
    (1, 'Assigned'), # Assigned
    (2, 'Resolved'), # Resolved
    (3, 'Closed'), # Closed
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
)