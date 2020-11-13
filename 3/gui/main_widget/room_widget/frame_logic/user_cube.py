from PySide2.QtGui import QPainter


class UserCube:

    def __init__(self, start_position=(0, 0)):
        self.__cur_position = list(start_position)
        self._center_shift = 10
        self._cur_path = None

    def set_xy(self, x, y):
        self.__cur_position[0] = x
        self.__cur_position[1] = y

    def get_cur_position(self):
        return self.__cur_position

    def draw_cube(self, qp: QPainter):
        x, y = self.__cur_position
        qp.drawLine(x-self._center_shift, y-self._center_shift, x+self._center_shift, y-self._center_shift)
        qp.drawLine(x+self._center_shift, y-self._center_shift, x+self._center_shift, y+self._center_shift)
        qp.drawLine(x+self._center_shift, y+self._center_shift, x-self._center_shift, y+self._center_shift)
        qp.drawLine(x-self._center_shift, y+self._center_shift, x-self._center_shift, y-self._center_shift)

