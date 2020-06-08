# encode: utf-8
import os
from subprocess import Popen, PIPE, TimeoutExpired


def service_running(command: str, name_app: str) -> int or False:
    """
    Поместите ваш пароль от пользователя в .bash_profile, или введите его вручную в .communicate('ваш пароль').

    :param command: status, start, stop, restart.
    :param name_app: Имя приложения, для которого выполняется команда.
    :return: int: command='status' возвращает "0" если приложение работает или '3' - не работает.
    """
    try:
        with open(os.devnull, 'wb') as output:
            exit_code = Popen(['sudo', '-S', 'systemctl', command, name_app], stdout=output, stdin=PIPE,
                              stderr=output, universal_newlines=True)
            exit_code.communicate(os.environ.get("USER_PASSWORD"), timeout=3)  # ввод пароля, если это потребуется.
            status_execution = exit_code.wait()
        return status_execution
    except TimeoutExpired:  # создается при истечении времени ожидания в .communicate(timeout=3)
        return False


if __name__ == "__main__":
    pass
