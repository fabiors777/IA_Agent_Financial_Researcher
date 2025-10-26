from dotenv import load_dotenv
from textwrap import dedent
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

load_dotenv()

db = SqliteDb(db_file="agent_data.db")

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    user_id="Fabio",
    session_id="1",
    db=db,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=3,
    instructions=dedent("""\
        Você é um assistente de IA útil e amigável com excelente memória.
        - Lembre-se de detalhes importantes sobre os usuários e referencie-os naturalmente
        - Mantenha um tom caloroso e positivo enquanto é preciso e útil
        - Quando apropriado, refira-se a conversas e memórias anteriores
        - Sempre seja honesto sobre o que você lembra ou não lembra
    """),
    markdown=True,
)

if __name__ == "__main__":
    while True:
        msg = input("Entre com a mensagem (ou 'q' p/ sair): ")
        if msg.lower() == "q":
            break
        agent.print_response(msg, stream=False, markdown=True)
        print()
