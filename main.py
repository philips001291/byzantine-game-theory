from general import General
from simulation import collect_messages, make_decisions, check_consensus


generals = [
    General(1),
    General(2),
    General(3, is_traitor=True),
    General(4),
]

original_order = "ATTACK"

messages = collect_messages(generals, original_order)
decisions = make_decisions(generals, messages)
consensus = check_consensus(decisions)

print("Generals:")
for general in generals:
    print(general)

print("\nMessages:")
for general_id, received_messages in messages.items():
    print(f"General {general_id} received: {received_messages}")

print("\nDecisions:")
for general_id, decision in decisions.items():
    print(f"General {general_id} -> {decision}")

print("\nConsensus:", consensus)