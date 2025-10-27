import os
from dotenv import load_dotenv

load_dotenv()

# --- Mock Alith SDK components for demonstration ---
class Agent:
    def __init__(self, name, description, capabilities):
        self.id = name.lower().replace(" ", "_")
        self.name = name
        self.description = description
        self.capabilities = capabilities

class PlotGeneratorAgent:
    def __init__(self):
        # Initialize the agent's identity within the mock Alith environment
        self.agent_info = Agent(
            name="PlotGenerator",
            description="Generates high-level story plots.",
            capabilities=["generate_plot_outline"]
        )

    def generate_plot_outline(self):
        """
        Generates a basic story outline with premise, conflict, and resolution.
        This structured data is the core output of this agent.
        """
        plot_outline = {
            "premise": "A young inventor discovers a time-travel device.",
            "conflict": "An evil corporation wants the device for nefarious purposes.",
            "resolution": "The inventor outsmarts the corporation and secures the device's future."
        }
        print(f"[{self.agent_info.name}] Generated plot outline: {plot_outline}")
        return plot_outline

if __name__ == "__main__":
    # Example execution when running the file directly
    generator = PlotGeneratorAgent()
    plot = generator.generate_plot_outline()
    print(plot)