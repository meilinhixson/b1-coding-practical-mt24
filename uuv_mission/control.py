#Implementation of a PD controller for the UUV

# control.py
class PDController:
    def __init__(self, KP=0.15, KD=0.6):  # Default gains
        self.KP = KP # Proportional gain
        self.KD = KD  # Derivative gain
        self.previous_error = 0     # Error at the previous time step

    def compute_control_action(self, reference, output, dt):  
        error = reference - output
        derivative = (error - self.previous_error) / dt
        control_action = self.KP * error + self.KD * derivative  
        self.previous_error = error
        return control_action