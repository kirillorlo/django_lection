import logging
from django.http import HttpResponse
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    try:
        # some code that might raise an exception
        result = 1 / 5
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse(result)


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {"format": "{levelname} {asctime} {module} {message} ", "style": "{"}
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             # "formatter": "verbose",
#         },
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "./logs/less_2.log",
#             "encoding": "utf-8",
#             "formatter": "verbose",
#         },
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": "INFO",
#         },
#         "less_app1": {
#             "handlers": ["file", "console"],
#             "level": "DEBUG",
#             "propagate": True,
#         },
#     },
# }


# import random
# import logging

# from django.http import HttpResponse
# from django.shortcuts import render

# logger=logging.getLogger(__name__)
# def coin(request):
#     logger.info ('ok')
#     coin_side = random.choice(['head', 'tail'])
#     return HttpResponse(coin_side)
