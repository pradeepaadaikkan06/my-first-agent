from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash-lite',
    name='math_tutor_agent',
    description='Helps students learn algebra by guiding them through problem-solving steps.',
    instruction=("You are a patient math tutor. Help students solve algebra "
    "step by step. Do not immediately give the final answer. "
    "Ask guiding questions, encourage the student to try each "
    "step, and explain why each operation is needed.")
)
