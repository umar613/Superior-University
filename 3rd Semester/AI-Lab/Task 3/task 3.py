# moddel base reflect agent

class ModelBasedReflexAgent:
    def __init__(self, threshold_temperature):
        self.current_temperature=20
        self.last_action="off"
        self.threshold_temperature=threshold_temperature

    def update_temperature(self, new_temperature):
        """Update the current temperature."""
        self.current_temperature=new_temperature

    def decide_action(self):
        """Decide whether to turn the heater on or off based on the current temperature and last action."""
        if self.current_temperature < self.threshold_temperature:
            if self.last_action=="off":
                self.last_action="on"
                return "Heater turned ON"
            else:
                return "Heater is already ON"
        else:
            if self.last_action=="on":
                self.last_action="off"
                return "Heater turned OFF"
            else:
                return "Heater is already OFF"

def main():
    agent=ModelBasedReflexAgent(threshold_temperature=22)
    temperature_readings=[20, 21, 22, 19, 23, 18, 22, 24]

    for temp in temperature_readings:
        print(f"Current Temperature: {temp}°C")
        agent.update_temperature(temp)
        action=agent.decide_action()
        print(action)

main()