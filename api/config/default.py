import os
SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a79 36789'

POPAGATE_EXCEPTIONS = True

#Database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                        'sqlite:///films.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False # suppress logging

ERROR_404_HELP = False