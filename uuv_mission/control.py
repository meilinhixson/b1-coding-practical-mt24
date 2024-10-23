#Implementation of a PD controller for the UUV

# control.py
class PDController:
    def __init__(self, kp=0.15, kd=0.6):  # Default gains
        self.kp = kp # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0     # Error at the previous time step

    def compute_control_action(self, reference, output, dt):  
        error = reference - output
        derivative = (error - self.previous_error) / dt
        control_action = self.kp * error + self.kd * derivative  
        self.previous_error = error
        return control_action