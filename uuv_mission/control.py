class PDController:
    def __init__(self, Kp=0.15, Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0
    
    def control(self, current_error):
        # Calculate control signal with preliminary PD controller design
        control_signal = self.Kp * current_error + self.Kd * (current_error - self.previous_error)

        # Set error as previous error for next iteration
        self.previous_error = current_error
        return control_signal
