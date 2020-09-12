class Signal:
    def __init__(self, active, price, change, movement, update_time):
        self._active = active
        self._price = price
        self._change = change
        self._movement = movement
        self._update_time = update_time

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active):
        self._active = active
