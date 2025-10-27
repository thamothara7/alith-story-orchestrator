import os
from dotenv import load_dotenv
from agents.plot_generator import PlotGeneratorAgent, Agent as MockAgent
from agents.narrative_refiner import NarrativeRefinerAgent

load_dotenv()

# --- Mock Alith SDK Components ---
class MockTask:
    def __init__(self, sender_id, receiver_id, task_type, data):
        self.id = f"task-{os.urandom(4).hex()}"
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.task_type = task_type
        self.data = data

class MockDAT:
    def __init__(self, initiator_id, target_data_hash, action_type, validation_parameters, reward_amount):
        self.id = f"dat-{os.urandom(4).hex()}"
        self.initiator_id = initiator_id
        self.target_data_hash = target_data_hash
        self.action_type = action_type
        self.validation_parameters = validation_parameters
        self.reward_amount = reward_amount

class MockAlithClient:
    def __init__(self):
        self.api_key = os.getenv("ALITH_API_KEY")
        if not self.api_key:
            print("WARNING: ALITH_API_KEY not set in .env. This is a mock client, but real SDK would require it.")
        print("Mock Alith Client initialized.")

    def register_agent(self, agent_info):
        print(f"Mock Alith Client: Registering agent '{agent_info.name}' (ID: {agent_info.id})...")
        # In a real SDK, this would interact with the Alith network
        pass

    def send_task(self, task):
        print(f"Mock Alith Client: Sending task '{task.id}' from '{task.sender_id}' to '{task.receiver_id}'.")
        # In a real SDK, this would publish the task to the network
        pass

    def submit_dat(self, dat):
        print(f"Mock Alith Client: Submitting DAT '{dat.id}' for validation by '{dat.initiator_id}'.")
        print(f"  Validation parameters: {dat.validation_parameters}")
        print(f"  Reward if validated: {dat.reward_amount} tokens.")
        # In a real SDK, this would submit the DAT to the Alith ledger
        # for smart contract execution/validation.
        pass

# --- Orchestration Logic ---
def main():
    print("--- Starting Alith Story Orchestrator Demo ---")

    # Initialize mock Alith client
    alith_client = MockAlithClient()

    # Initialize agents
    plot_generator_instance = PlotGeneratorAgent()
    narrative_refiner_instance = NarrativeRefinerAgent()

    # (Conceptual) Register agents with Alith network
    alith_client.register_agent(plot_generator_instance.agent_info)
    alith_client.register_agent(narrative_refiner_instance.agent_info)

    # 1. Plot Generator creates a plot outline
    print("\n--- Step 1: Plot Generator at work ---")
    plot_outline_data = plot_generator_instance.generate_plot_outline()

    # 2. Plot Generator creates and sends a task to the Narrative Refiner
    print("\n--- Step 2: Plot Generator sends task to Narrative Refiner ---")
    plot_task = MockTask(
        sender_id=plot_generator_instance.agent_info.id,
        receiver_id=narrative_refiner_instance.agent_info.id,
        task_type="refine_story_plot",
        data=plot_outline_data
    )
    alith_client.send_task(plot_task)
    print(f"Task ID: {plot_task.id}")
    print(f"Data passed: {plot_task.data}")

    # 3. Narrative Refiner receives the task and refines the narrative
    print("\n--- Step 3: Narrative Refiner processes the task ---")
    # In a real system, the refiner would fetch the task. Here, we simulate direct passing.
    refined_story_output = narrative_refiner_instance.refine_narrative(plot_task.data)
    print("\nRefined Story:")
    print(refined_story_output)

    # 4. Narrative Refiner creates and submits a DAT for validation
    print("\n--- Step 4: Narrative Refiner submits DAT for validation ---")
    validation_criteria = {
        "min_word_count": 200,
        "keywords_present": ["temporal", "OmniCorp", "inventor"]
    }

    narrative_dat = MockDAT(
        initiator_id=narrative_refiner_instance.agent_info.id,
        target_data_hash=hash(refined_story_output), # A simple hash for integrity check
        action_type="story_refinement_validation",
        validation_parameters=validation_criteria,
        reward_amount=10 # Example reward in Alith tokens
    )
    alith_client.submit_dat(narrative_dat)

    print("\n--- Orchestration Demo Complete ---")
    print("Conceptual reward unlocked if DAT validation successful: 10 tokens for Narrative Refiner.")

if __name__ == "__main__":
    main()