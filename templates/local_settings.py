DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{{item.djangoapp_db_engine}}', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '{{item.djangoapp_projectname}}',                      # Or path to database file if using sqlite3.
        # 'NAME': os.path.join(PROJECT_ROOT, 'data.db'),                      # Or path to database file if using sqlite3.
        'USER': '{{item.djangoapp_projectname}}',                      # Not used with sqlite3.
        'PASSWORD': '{{item.djangoapp_projectname}}',                  # Not used with sqlite3.
        'HOST': '{{item.djangoapp_db_host}}',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}