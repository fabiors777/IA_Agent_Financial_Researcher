from agno.models.openai import OpenAIChat
from agno.team.team import Team
from financial_researcher import researcher
from financial_analyst import finance_agent
import asyncio
from dotenv import load_dotenv

load_dotenv()

agent_team = Team(
    name="Financial Team",
    model=OpenAIChat(id="gpt-5-mini"),
    members=[
        finance_agent,
        researcher,
    ],
    instructions=[
        "Você é o coordenador de uma equipe de análise financeira.",
        "Você deve parar a discussão quando a equipe chegar a um consenso sobre a analise.",
        "Certifique-se de que tanto a pesquisa quanto a análise técnica sejam abordadas.",
        "O relatório final deve ser abrangente e bem estruturado.",
    ],
    markdown=True,
    show_members_responses=True,
)

if __name__ == "__main__":
    asyncio.run(
    agent_team.aprint_response("Iniciem a análise sobre o tema: 'Análise completa das ações do Banco do Brasil SA (BBAS3.SA)'", stream=True)
)
