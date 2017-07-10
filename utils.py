from termcolor import cprint


def log_error(message):
    cprint(message, 'red')


def log_warn(message):
    cprint(message, 'yellow')


def log_info(message):
    cprint(message, 'cyan')


def log_success(message):
    cprint(message, 'green')