class PDController:
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0
    
    def control(self, current_error):
        control_signal = self.Kp * current_error + self.Kd * (current_error - self.previous_error)
        self.previous_error = current_error
        return control_signal
