# production.py
from .base import *
from google.cloud import secretmanager
import io

# Production-specific settings
DEBUG = False

try:
    # --- Be sure to update these values for your project ---
    PROJECT_ID = "land-and-lease-app"
    SECRET_ID = "django-secret-key"
    VERSION_ID = "latest"
    # ----------------------------------------------------

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}/versions/{VERSION_ID}"
    response = client.access_secret_version(name=name)
    SECRET_KEY = response.payload.data.decode("UTF-8")
except Exception as e:
    # Log the error and fall back to a less secure key if needed, or raise an exception
    print(f"Error fetching secret key: {e}")
    SECRET_KEY = "a-fallback-key-for-emergency-only" # Or raise Exception("Could not fetch SECRET_KEY")

ALLOWED_HOSTS = ['app.crimsonmammoth.com'] # Your future domain

# Enforce HTTPS and other security headers
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# --- 2. DATABASE SETTINGS ---

# Database configuration will be read from environment variables
# provided by Cloud Run, connecting securely via a Cloud SQL socket.
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'), # e.g., '/cloudsql/project:region:instance'
        'PORT': '5432',
    }
}


# --- 3. STATIC & MEDIA FILES (Google Cloud Storage) ---

# --- Be sure to update this with your unique bucket name ---
GS_BUCKET_NAME = "project-umbrella-assets"
# --------------------------------------------------------

# Use django-storages to manage files in GCS
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# These settings will be used by django-storages
GS_DEFAULT_ACL = 'publicRead'
GS_FILE_OVERWRITE = False
