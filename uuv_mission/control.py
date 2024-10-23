#Implementation of a PD controller for the UUV

# control.py
class PDController:
    def __init__(self, kp, kd):  # Default gains
        self.kp = kp # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0     # Error at the previous time step

 
    
    def compute(self, error, dt) -> float:
        derivative = (error - self.previous_error) / dt
        # Compute control output by using the PD formula
        output = self.kp * error + self.kd * derivative
        # Update previous error for next iteration
        self.previous_error = error
        return output