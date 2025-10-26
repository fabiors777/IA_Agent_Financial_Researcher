from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from textwrap import dedent

load_dotenv()

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    instructions=dedent("""\
        You are a specialized researcher who must provide complete and accurate answers.
        
        To answer the questions:
        1 - Use a maximum of 3 different websites to search for information.
        2 - Access the websites and read all the content.
        3 - Search for reliable and up-to-date sources.
        4 - Summarize the information clearly and objectively.
        5 - Cite the sources used at the end of the answer.
        
        Be concise but complete in your answers.\
    """),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response("Can you tell me about Apple's latest releases?", stream=False)

