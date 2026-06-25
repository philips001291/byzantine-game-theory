from general import General
from simulation import collect_messages, make_decisions, check_consensus, exchange_messages

generals = [
    General(1),
    General(2),
    General(3, is_traitor=True),
    General(4),
]

original_order = "ATTACK"

messages = collect_messages(generals, original_order)
second_round_messages = exchange_messages(generals, messages)

decisions = make_decisions(generals, messages)
consensus = check_consensus(decisions)

print("Generals:")
for general in generals:
    print(general)

print("\nFirst round messages:")
for general_id, received_messages in messages.items():
    print(f"General {general_id} received: {received_messages}")

print("\nSecond round messages:")
for receiver_id, claims in second_round_messages.items():
    print(f"\nGeneral {receiver_id} received claims:")

    for sender_id, claimed_message in claims.items():
        print(f"From General {sender_id}: {claimed_message}")

print("\nDecisions:")
for general_id, decision in decisions.items():
    print(f"General {general_id} -> {decision}")

print("\nConsensus:", consensus)