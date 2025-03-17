'''Provides the inputs for testing the control software for a thermostaticly
   controlled shower valve.'''

class ValveSim:
    '''Methods and propeties for ValveSim'''
    def __init__(self, wait_value):
        '''Constructor method'''
        self.cold_temp = None
        self.hot_temp = None
        self.mix_temp = None

        self.wait_after_adjust = wait_value

    # Properties
    @property
    def cold_temp(self):
        '''cold_temp getter'''
        return self.cold_temp

    @cold_temp.setter
    def cold_temp(self, value):
        '''setter'''
        self.cold_temp = value

    @cold_temp.deleter
    def cold_temp(self):
        '''deleter'''
        del self.cold_temp

    @property
    def hot_temp(self):
        '''hot_temp getter'''
        return self.hot_temp

    @hot_temp.setter
    def hot_temp(self, value):
        '''setter'''
        self.hot_temp = value

    @hot_temp.deleter
    def hot_temp(self):
        '''deleter'''
        del self.hot_temp

    @property
    def cold_valve_setting(self):
        '''cold valve setting getter'''
        return self.cold_valve_setting

    @cold_valve_setting.setter
    def cold_valve_setting(self, value):
        '''setter'''
        self.cold_valve_setting = value

    @cold_valve_setting.deleter
    def cold_valve_setting(self):
        '''deleter'''
        del self.cold_valve_setting

    @property
    def hot_valve_setting(self):
        '''hot_temp getter'''
        return self.hot_valve_setting

    @hot_valve_setting.setter
    def hot_valve_setting(self, value):
        '''setter'''
        self.hot_valve_setting = value

    @hot_valve_setting.deleter
    def hot_valve_setting(self):
        '''deleter'''
        del self.hot_valve_setting

    # Methods
    def cold_change(self, value):
        '''adjusts the cold water valve'''
        if 1 == 1: # TODO: This line of code would trigger the mechanism to
                   # move the valve and return false if the move failed
            self.cold_valve_setting = self.cold_valve_setting + value
            return True
        else:
            return False

    def hot_change(self, value):
        '''adjusts the cold water valve'''
        if 1 == 1: # TODO: This line of code would trigger the mechanism to
                   # move the valve and return false if the move failed
            self.hot_valve_setting = self.hot_valve_setting + value
            return True
        else:
            return False
