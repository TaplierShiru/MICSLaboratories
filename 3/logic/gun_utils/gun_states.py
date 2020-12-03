

class GunStates:
    """
    Keep all possibible statements and their conditions

    """

    TIME = 'time'
    LUCKY = 'lucky'
    BRAIN_STRENGTH = 'brain_strength'

    # States
    STATE_1_SLEEP = 1
    STATE_2_WAKEUP = 2
    STATE_3_SLEEP_5MIN_MORE = 3
    STATE_4_TAKE_CLOTHS = 4
    STATE_5_TAKE_SCHOOLBAG = 5
    STATE_6_WASHFACE = 6
    STATE_7_EAT = 7
    STATE_8_GO_TO_UNIVERSITY = 8
    STATE_FINISH = 9

    # States and their conditions
    # Time - should be less than
    # Lucky - should be more than
    # Brain - should be more than
    STATE_DICT = {
        STATE_1_SLEEP:                  {TIME: -1,  LUCKY: -1, BRAIN_STRENGTH: -1},
        STATE_2_WAKEUP:                 {TIME: 60,  LUCKY:  3, BRAIN_STRENGTH:  5},
        STATE_3_SLEEP_5MIN_MORE:        {TIME: 60,  LUCKY:  0, BRAIN_STRENGTH:  0},
        STATE_4_TAKE_CLOTHS:            {TIME: 50,  LUCKY:  2, BRAIN_STRENGTH:  3},
        STATE_5_TAKE_SCHOOLBAG:         {TIME: 40,  LUCKY:  2, BRAIN_STRENGTH:  5},
        STATE_6_WASHFACE:               {TIME: 40,  LUCKY:  2, BRAIN_STRENGTH:  3},
        STATE_7_EAT:                    {TIME: 40,  LUCKY:  4, BRAIN_STRENGTH:  4},
        STATE_8_GO_TO_UNIVERSITY:       {TIME: 60,  LUCKY:  2, BRAIN_STRENGTH:  2},
    }

    @staticmethod
    def is_cur_situation_good_for(cur_state: int, time: int, lucky: int, brain_strength: int):
        """
        Return True, if current parameters are good for `cur_state`

        """
        data_state = GunStates.STATE_DICT[cur_state]

        if time < data_state[GunStates.TIME] and \
                (lucky > data_state[GunStates.LUCKY] or brain_strength > data_state[GunStates.BRAIN_STRENGTH]):
            return True
        return False
