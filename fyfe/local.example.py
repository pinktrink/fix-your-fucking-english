LOCALENV = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.mysql', #Using MySQL for the live instance, though anything will work
            'NAME': 'fyfe', #DB name, everything else is self-explanatory
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    },
    
    #The following can be omitted
    'STATIC_ROOT': '', #If using a WSGI instance, where Apache should serve static files from
    'STATIC_URL': '/static/', #URL from which static files should be served from
    'MEDIA_ROOT': '', #If using a WSGI instance, where Apache should serve media files from
    'MEDIA_URL': '', #URL from which media files should be served from
}
