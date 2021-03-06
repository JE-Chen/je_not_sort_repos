import datetime
import json
import threading


class LogSystem(threading.Thread):

    def __init__(self, lock):
        super().__init__()
        # thread lock
        self.lock = lock
        # log level
        self.normal = 0
        self.info = 1
        self.debug = 2
        self.warning = 3
        self.error = 4
        self.critical = 5
        self.everything_broken = 10
        # save level
        self.boardcast = 3
        # show log time ?
        self.showtime = True

    # log level normal
    def log_normal(self, *args) -> str:
        return self.log_state(self.normal, self.boardcast, "Log.jelog", 'normal', *args)

    def log_info(self, *args) -> str:
        return self.log_state(self.info, self.boardcast, "Log.jelog", 'info', *args)

    def log_debug(self, *args) -> str:
        return self.log_state(self.debug, self.boardcast, "Log.jelog", 'debug', *args)

    def log_warning(self, *args) -> str:
        return self.log_state(self.warning, self.boardcast, "Log.jelog", 'warning', *args)

    def log_error(self, *args) -> str:
        return self.log_state(self.error, self.boardcast, "Log.jelog", 'error', *args)

    def log_critical(self, *args) -> str:
        return self.log_state(self.critical, self.boardcast, "Log.jelog", 'critical', *args)

    def log_everything_broken(self, *args) -> str:
        return self.log_state(self.everything_broken, self.boardcast, "Log.jelog", 'everything_broken', *args)

    # set boardcast level
    def set_boardcast_lv(self, lv: int) -> int:
        if lv <= -1:
            self.boardcast = 3
            return -1
        else:
            self.boardcast = lv
            return self.boardcast

    def set_showtime(self, time_able: bool) -> bool:
        self.showtime = time_able
        return self.showtime

    def log_state(self, lv1: int, lv2: int, log_file_name: str, error: str, *args) -> str:

        try:
            if lv1 >= lv2 and self.showtime is True:
                text = ''
                text += (datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S') + ':')
                text += (str(error) + ':' + str(args))
                self.save_log(text, log_file_name)
                return "Log in file " + text
            elif self.critical >= self.boardcast:
                return "Not log in file " + str(error) + ':' + str(args)
        except Exception as e:
            print(e)
        return "Not Run"

    def load_setting(self, setting_name: str, type):
        with open(setting_name, 'r+')as file:
            try:
                if type is "json" or type is None:
                    setting_json = json.loads(file.read())
                    self.showtime = setting_json['showtime']
                    self.boardcast = setting_json['broadcast']
            except Exception as e:
                print(e)

    def save_log(self, error_text: str, log_name: str) -> str:
        self.lock.acquire()
        with open(log_name, 'a')as file:
            file.write(error_text + '\n')
        self.lock.release()
        return error_text + log_name

    def clean_log(self, log_name: str) -> str:
        self.lock.acquire()
        with open(log_name, 'w')as file:
            file.write('')
        self.lock.release()
        return log_name
