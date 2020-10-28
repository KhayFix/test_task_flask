# encode: utf-8
import os
from subprocess import Popen, PIPE, TimeoutExpired

from webapp.config import USER_PASSWORD


class ServiceApp(object):

    def __init__(self, user_password=None):
        self._sudo = "sudo"
        self._s = "-S"
        self._init_sys = "systemctl"
        self.user_password = user_password
        self.timeout = 3

    def running(self, command: str, name_app: str) -> int or False:
        """Управляет например приложением Apache2 или другим др.приложением.

        command='status' возвращает "0" если приложение работает, '3' - не работает,
        4 - сервис не найден в системе, False - ошибка.

        command: status, start, stop, restart и т.д.
        name_app: Имя приложения, для которого выполняется команда.
        """
        try:
            with open(os.devnull, 'wb') as output:
                exit_code = Popen([self._sudo, self._s, self._init_sys, command, name_app],
                                  stdout=output, stdin=PIPE, stderr=output, universal_newlines=True
                                  )
                exit_code.communicate(
                    self.user_password, timeout=self.timeout
                )  # ввод пароля, если это потребуется.

                return exit_code.wait()
        except TimeoutExpired:  # создается при истечении времени ожидания в .communicate(timeout=3)
            return False


service_app = ServiceApp(USER_PASSWORD)
