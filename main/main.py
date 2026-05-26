from extract import extract
from transform import analyze_ticket
from load import load_ticket

tickets = extract()

for ticket in tickets:

    analysis = analyze_ticket(ticket['mensagem'])

    payload = {
        "ticket_id": ticket['id'],
        "mensagem": ticket['mensagem'],
        "analise": analysis
    }

    status = load_ticket(payload)

    print("=" * 50)
    print(f"Chamado: {ticket['mensagem']}")
    print(analysis)
    print(f"Status API: {status}")