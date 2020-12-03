from gui.main_widget.room_widget.signals.data_sender import DataSender

from .gun_states import GunStates
from logic.utils.num_generation import UniformGenerator
from ..exceptions.failed_game_exception import FiledGameException


class GunLogic:
    """
    Implements finite-state machine
    Which goes thoutgh different statements
    And provide generator for finite-state machine

    """

    # Some states
    GUN_PATH = {
        GunStates.STATE_1_SLEEP: [GunStates.STATE_2_WAKEUP, GunStates.STATE_3_SLEEP_5MIN_MORE],
        GunStates.STATE_2_WAKEUP: [GunStates.STATE_6_WASHFACE, GunStates.STATE_3_SLEEP_5MIN_MORE],
        GunStates.STATE_3_SLEEP_5MIN_MORE: [GunStates.STATE_2_WAKEUP],
        GunStates.STATE_4_TAKE_CLOTHS: [
            GunStates.STATE_7_EAT, GunStates.STATE_8_GO_TO_UNIVERSITY,
            GunStates.STATE_3_SLEEP_5MIN_MORE
        ],
        GunStates.STATE_5_TAKE_SCHOOLBAG: [
            GunStates.STATE_4_TAKE_CLOTHS, GunStates.STATE_8_GO_TO_UNIVERSITY,
            GunStates.STATE_3_SLEEP_5MIN_MORE
        ],
        GunStates.STATE_6_WASHFACE: [
            GunStates.STATE_5_TAKE_SCHOOLBAG, GunStates.STATE_4_TAKE_CLOTHS,
            GunStates.STATE_3_SLEEP_5MIN_MORE
        ],
        GunStates.STATE_7_EAT: [GunStates.STATE_8_GO_TO_UNIVERSITY, GunStates.STATE_3_SLEEP_5MIN_MORE],
        GunStates.STATE_8_GO_TO_UNIVERSITY: [GunStates.STATE_FINISH],
    }

    MAX_TIME = 60
    # Parameters for uniform dist (min_value, max_value)
    LEFT_TIME, RIGHT_TIME = (5, 10)
    LEFT_LUCKY, RIGHT_LUCKY = (0, 6)
    LEFT_BRAIN, RIGHT_BRAIN = (0, 7)

    def __init__(self, data_sender: DataSender, start_time=0):
        self.__all_time = start_time
        self.reset_params()

        self.__data_sender = data_sender

    def reset_params(self):
        # We start at 1 state
        self._cur_state = GunStates.STATE_1_SLEEP
        self._prev_state = None
        self._cur_path = None

    def get_prev_state(self):
        return self._prev_state

    def get_next_state(self):
        return self._cur_state

    def create_generator_quest(self):
        while self._cur_state != GunStates.STATE_FINISH:
            # Keep previous state
            self._prev_state = self._cur_state
            # Generate some parameters
            self.__all_time += UniformGenerator.generate_single(self.LEFT_TIME, self.RIGHT_TIME)
            lucky = UniformGenerator.generate_single(self.LEFT_LUCKY, self.RIGHT_LUCKY)
            brain_strength = UniformGenerator.generate_single(self.LEFT_BRAIN, self.RIGHT_BRAIN)
            # Break if we loose in time
            if self.__all_time > self.MAX_TIME:
                self._cur_state = GunStates.STATE_1_SLEEP
                self._send_data(lucky, brain_strength)
                raise FiledGameException()

            # Go somewhere
            were_any_state = False
            for may_states in GunLogic.GUN_PATH[self._cur_state][:-1]:
                if GunStates.is_cur_situation_good_for(may_states, self.__all_time, lucky, brain_strength):
                    self._cur_state = may_states
                    were_any_state = True
                    break

            # If we could not go anywhere, go to last state in state dict
            if not were_any_state:
                self._cur_state = GunLogic.GUN_PATH[self._cur_state][-1]

            # Update data for viewer
            self._send_data(lucky, brain_strength)
            yield self._prev_state, self._cur_state

    def _send_data(self, lucky: int, brain_strength: int):
        """
        Send data to viewer

        """
        self.__data_sender.send_lucky.emit(lucky)
        self.__data_sender.send_brain_strength.emit(brain_strength)
        self.__data_sender.send_cur_state.emit(self._cur_state)
        self.__data_sender.send_remain_time.emit(self.__all_time)

