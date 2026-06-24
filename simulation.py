def send_message(sender, receiver, original_order):
    if sender.is_traitor:
        if receiver.general_id % 2 == 0:
            return "ATTACK"
        return "RETREAT"

    return original_order


def collect_messages(generals, original_order):
    messages = {}

    for receiver in generals:
        messages[receiver.general_id] = []

        for sender in generals:
            if sender.general_id != receiver.general_id:
                message = send_message(sender, receiver, original_order)
                messages[receiver.general_id].append(message)

    return messages


def majority_vote(received_messages):
    attack_count = received_messages.count("ATTACK")
    retreat_count = received_messages.count("RETREAT")

    if attack_count >= retreat_count:
        return "ATTACK"

    return "RETREAT"


def make_decisions(generals, messages):
    decisions = {}

    for general in generals:
        if not general.is_traitor:
            decisions[general.general_id] = majority_vote(messages[general.general_id])

    return decisions


def check_consensus(decisions):
    unique_decisions = set(decisions.values())
    return len(unique_decisions) == 1