# encode: utf-8
import os
from subprocess import Popen, PIPE, TimeoutExpired

from webapp.config import USER_PASSWORD


def service_running(command: str, name_app: str) -> int or False:
    """
    Функция может управлять приложением Apache2.
    command='status' возвращает "0" если приложение работает или '3' - не работает.

    :param command: status, start, stop, restart.
    :param name_app: Имя приложения, для которого выполняется команда.
    :return: int
    """
    try:
        with open(os.devnull, 'wb') as output:
            exit_code = Popen(['sudo', '-S', 'systemctl', command, name_app], stdout=output, stdin=PIPE,
                              stderr=output, universal_newlines=True)
            exit_code.communicate(USER_PASSWORD, timeout=3)  # ввод пароля, если это потребуется.
            status_execution = exit_code.wait()
        return status_execution
    except TimeoutExpired:  # создается при истечении времени ожидания в .communicate(timeout=3)
        return False


if __name__ == "__main__":
    pass
