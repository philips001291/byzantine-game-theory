import random
from general import General
from traitor_strategies import traitor_message

def create_generals(number_of_generals, number_of_traitors):
    if number_of_traitors > number_of_generals:
        raise ValueError("Number of traitors cannot be greater than number of generals.")
    traitor_ids = random.sample(
        range(1, number_of_generals + 1),
        number_of_traitors
    )

    generals = []

    for general_id in range(1, number_of_generals + 1):
        is_traitor = general_id in traitor_ids
        generals.append(General(general_id, is_traitor))

    return generals

def send_message(sender, receiver, original_order, strategy="split"):
    if sender.is_traitor:
        return traitor_message(strategy, sender, receiver, original_order)

    return original_order

def collect_messages(generals, original_order, strategy = "split"):
    messages = {}

    for receiver in generals:
        messages[receiver.general_id] = []

        for sender in generals:
            if sender.general_id != receiver.general_id:
                message = send_message(sender, receiver, original_order, strategy)
                messages[receiver.general_id].append(message)

    return messages

def majority_vote(received_messages):
    attack_count = received_messages.count("ATTACK")
    retreat_count = received_messages.count("RETREAT")

    if attack_count >= retreat_count:
        return "ATTACK"

    return "RETREAT"

def check_consensus(decisions):
    unique_decisions = set(decisions.values())
    return len(unique_decisions) == 1

def exchange_messages(generals, first_round_messages, original_order="ATTACK", strategy="split"):
    second_round_messages = {}

    for receiver in generals:
        second_round_messages[receiver.general_id] = {}

        for sender in generals:
            if sender.general_id != receiver.general_id:
                if sender.is_traitor:
                    claimed_message = traitor_message(strategy, sender, receiver, original_order)
                else:
                    sender_messages = first_round_messages[sender.general_id]

                    attack_count = sender_messages.count("ATTACK")
                    retreat_count = sender_messages.count("RETREAT")

                    if attack_count >= retreat_count:
                        claimed_message = "ATTACK"
                    else:
                        claimed_message = "RETREAT"

                second_round_messages[receiver.general_id][sender.general_id] = claimed_message

    return second_round_messages

def make_final_decisions(generals, first_round_messages, second_round_messages):
    final_decisions = {}

    for general in generals:
        if not general.is_traitor:
            all_messages = []

            all_messages.extend(first_round_messages[general.general_id])
            all_messages.extend(second_round_messages[general.general_id].values())

            final_decisions[general.general_id] = majority_vote(all_messages)

    return final_decisions

def run_experiments(number_of_runs, number_of_generals, number_of_traitors):
    successful_consensus = 0
    failed_consensus = 0

    for run in range(number_of_runs):

        generals = create_generals(number_of_generals, number_of_traitors)
        first_round_messages = collect_messages(generals, "ATTACK")

        second_round_messages = exchange_messages(
            generals,
            first_round_messages
        )

        final_decisions = make_final_decisions(
            generals,
            first_round_messages,
            second_round_messages
        )
        
        consensus = check_consensus(final_decisions)

        if consensus:
            successful_consensus += 1
        else:
            failed_consensus += 1

    success_rate = (successful_consensus / number_of_runs) * 100

    return {
        "runs": number_of_runs,
        "generals": number_of_generals,
        "traitors": number_of_traitors,
        "successful_consensus": successful_consensus,
        "failed_consensus": failed_consensus,
        "success_rate": success_rate
    }
