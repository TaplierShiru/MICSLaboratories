from logic.exceptions.failed_game_exception import FiledGameException
from .user_cube import UserCube
from logic import GunLogic
from logic.gun_utils.gun_states import GunStates
from logic.gun_utils.gun_paths import STORAGE_PATHS
from ..signals.data_sender import DataSender
import numpy as np


class GameController:

    DIVIDER = 40

    def __init__(self, data_sender: DataSender):
        self.__gun_logic = GunLogic(data_sender)
        self.__data_sender = data_sender
        self.__generator_states = self.__gun_logic.create_generator_quest()
        self.reset_params()

    def get_data_sender(self):
        return self.__data_sender

    def reset_params(self):
        self.__gun_logic.reset_params()
        self.__user_cube = UserCube(start_position=(20, 20))
        self.__path_que = None
        self.__cur_path = None
        self.__steps_xy = None
        self.__is_last_path = False

    def take_a_step(self) -> bool:
        if self.__path_que is None or len(self.__path_que) == 0:
            if not self.__is_last_path:
                try:
                    prev_p, next_p = next(self.__generator_states)

                    if next_p == GunStates.STATE_FINISH:
                        self.__data_sender.game_finished.emit()
                        self.__data_sender.game_finished_info.emit("Вася смог\nКонец!")
                        return False

                    print(f'prev: {prev_p}, next_p: {next_p}')
                    self.__path_que = list(reversed(STORAGE_PATHS[prev_p][next_p]))

                except FiledGameException as ex:
                    self.__is_last_path = True
                    next_state = self.__gun_logic.get_prev_state()
                    prev_state = self.__gun_logic.get_next_state()
                    self.__path_que = list(reversed(STORAGE_PATHS[next_state][prev_state]))

        if self.__is_last_path and self.__path_que is None and \
            (self.__cur_path is None or len(self.__cur_path) == 0):
            self.__data_sender.game_finished.emit()
            self.__data_sender.game_finished_info.emit("Вася не успел собраться!")
            return False
        elif self.__cur_path is None or len(self.__cur_path) == 0:
            new_paths = self.__path_que.pop()
            if new_paths is None:
                self.__path_que = None
                return False
            x_from, y_from = new_paths[0]
            x_to, y_to = new_paths[1]

            x_new_paths = np.linspace(x_from, x_to, self.DIVIDER)[::-1].tolist()
            y_new_paths = np.linspace(y_from, y_to, self.DIVIDER)[::-1].tolist()

            self.__cur_path = [
                [single_x, single_y]
                for single_x, single_y in zip(x_new_paths, y_new_paths)
            ]

        new_coord = self.__cur_path.pop()
        self.__user_cube.set_xy(new_coord[0], new_coord[1])

        return True

    def get_user_cube(self):
        return self.__user_cube

    def is_stop(self):
        return len(self.__path_que) == 0


