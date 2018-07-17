import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-*yfowfm(*$v7w^5d7ko$#c&9u$rv0a%7*!x&57pd$ona0=8bj'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '-*yfowfm(*$v7w^!x&57pd$ona0=8bj')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*', 'www.lylinux.net', '127.0.0.1', 'example.com']

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'polls.apps.PollsConfig',
    'pagedown',
    'haystack',
    'blog',
    'accounts',
    'comments',
    'oauth',
    'servermanager',
    'owntracks',
    'compressor'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.OnlineMiddleware'
    'django.middleware.http.ConditionalGetMiddleware',
]

ROOT_URLCONF = 'July_Django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'July_Django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_app',
        'USER': os.getenv('DJANGO_MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('DJANGO_MYSQL_PASSWORD', 'password'),
        'HOST': os.getenv('DJANGO_MYSQL_HOST', '127.0.0.1'),
        'PORT': os.getenv('DJANGO_MYSQL_PORT', 3306),
        'OPTIONS': {
            'read_default_file': os.path.join(BASE_DIR, 'my.cnf'),
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.abspath(os.path.join(SITE_ROOT, '../'))

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'DjangoBlog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}
# 自动更新搜索索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
# 允许使用用户名或密码登录
AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']

STATIC_ROOT = os.path.join(SITE_ROOT, 'collectedstatic')

STATIC_URL = '/static/'
STATICFILES = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'accounts.BlogUser'
LOGIN_URL = '/login/'

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

# bootstrap颜色样式
BOOTSTRAP_COLOR_TYPES = [
    'default', 'primary', 'success', 'info', 'warning', 'danger'
]

# 分页
PAGINATE_BY = 10
# http缓存时间
CACHE_CONTROL_MAX_AGE = 2592000
# cache setting
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'django_test' if TESTING else 'djangoblog',
        'TIMEOUT': 60 * 60 * 10
    },
    'locmemcache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 10800,
        'LOCATION': 'unique-snowflake',
    }
}

SITE_ID = 1
BAIDU_NOTIFY_URL = "http://data.zz.baidu.com/urls?site=https://www.lylinux.net&token=1uAOGrMsUm5syDGn"

# Emial:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST')
EMAIL_PORT = os.environ.get('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = os.environ.get('DJANGO_EMAIL_USER')
# 设置debug=false 未处理异常邮件通知
ADMINS = [('xuzhijiang', 'xuzhijiang@gmail.com')]
# 微信管理员密码(两次md5获得)
WXADMIN = '995F03AC401D6CABABAEF756FC4D43C7'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'djangoblog.log',
            'maxBytes': 16777216,  # 16 MB
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'djangoblog': {
            'handlers': ['log_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True


COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]