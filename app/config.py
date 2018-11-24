class DevelopmentConfig:
    DEBUG = True
    ENV = 'development'
    HOST = '0.0.0.0'
    PORT = 5000

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@127.0.0.1:5432/advent_calendar'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
