from decouple import config


class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='gess-me')
    DEBUG = False
    TESTING = False
    CSFR_ENABLED = True


class ProductionConfig(config):
    DEBUG = False
    MAIL_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentCongif(config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(config):
    TESTING = True
