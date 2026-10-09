import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class PlannerAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        self.client = genai.Client(api_key=api_key)

    def create_plan(self, requirement):
        prompt = f"""
You are the Planner Agent of MultiDev AI.

Your job is to analyse a software requirement and create
a clear development plan for other software engineering agents.

Do not write the actual code.

Requirement:
{requirement}

Create a plan containing:

1. Project understanding
2. Functional requirements
3. Main modules
4. Development tasks
5. Testing requirements
6. Important considerations

Keep the plan clear and structured.
"""

        interaction = self.client.interactions.create(
            model="gemini-3.7-flash",
            input=prompt
        )

        return interaction.output_text