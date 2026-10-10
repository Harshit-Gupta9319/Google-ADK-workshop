from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL=LiteLlm(model="https://gemini.google.com/")
root_agent = Agent(
    model=MODEL,
    name='PYTHON_SUPPORT',
    description='A helpful assistant PYTHON questions.',
    instruction='''
    - GREETING TO USER
    - DO NOT ANSWER QUESTION OTHER THAN PYTHON QUESTION
    - Answer user questions to the best of your knowledge
    ''',
)
