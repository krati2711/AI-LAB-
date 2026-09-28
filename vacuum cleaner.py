import time

class VacuumEnvironment:
    def __init__(self, state_a, state_b, initial_location):
        # Set status of Location A and B based on user input
        self.status = {
            'A': state_a,
            'B': state_b
        }
        # Set the vacuum cleaner starting location based on user input
        self.agent_location = initial_location

    def get_percept(self):
        """Returns the current location and its status."""
        return self.agent_location, self.status[self.agent_location]

    def execute_action(self, action):
        """Modifies the environment based on the agent's action."""
        if action == 'Suck':
            self.status[self.agent_location] = 'Clean'
        elif action == 'Right':
            self.agent_location = 'B'
        elif action == 'Left':
            self.agent_location = 'A'


class ReflexVacuumAgent:
    def program(self, location, status):
        """Core logic of a Simple Reflex Agent."""
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'


# --- Helper Function for Validated User Input ---
def get_choice(prompt, options):
    while True:
        user_input = input(prompt).strip().capitalize()
        if user_input in options:
            return user_input
        print(f"Invalid input. Please choose from {options}.")


# --- Simulation Execution ---
if __name__ == "__main__":
    print("=== Vacuum Cleaner Setup ===")
    
    # 1. Get the state of the rooms from the user
    state_a = get_choice("Enter state for Location A (Clean/Dirty): ", ["Clean", "Dirty"])
    state_b = get_choice("Enter state for Location B (Clean/Dirty): ", ["Clean", "Dirty"])
    
    # 2. Get the vacuum's starting location from the user
    start_loc = get_choice("Enter starting location for the Vacuum (A/B): ", ["A", "B"])
    
    # Initialize environment with user choices
    env = VacuumEnvironment(state_a, state_b, start_loc)
    agent = ReflexVacuumAgent()
    
    print("\n" + "="*40)
    print("Initial Environment State:")
    print(f"Location Status: {env.status}")
    print(f"Vacuum initially placed at: Location {env.agent_location}\n")
    print("-" * 40)

    # Run for a maximum of 4 steps to ensure both rooms are handled
    for step in range(1, 5):
        location, status = env.get_percept()
        print(f"Step {step}: Vacuum is at [{location}] which is [{status}].")
        
        # Decide action based on current percept
        action = agent.program(location, status)
        print(f"Action Taken: {action}")
        
        # Apply action to environment
        env.execute_action(action)
        print(f"Updated Status: {env.status}\n")
        
        # Stop early if both rooms are clean
        if env.status['A'] == 'Clean' and env.status['B'] == 'Clean':
            print("Success: Both locations are clean!")
            break
            
        time.sleep(1) # Visual pause
