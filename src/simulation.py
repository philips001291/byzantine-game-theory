import random

from src.general import General
from src.traitor_strategies import traitor_message


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


def collect_messages(generals, original_order, strategy="split"):
    messages = {}

    for receiver in generals:
        messages[receiver.general_id] = []

        for sender in generals:
            if sender.general_id != receiver.general_id:
                message = send_message(
                    sender,
                    receiver,
                    original_order,
                    strategy
                )

                messages[receiver.general_id].append(message)

    return messages


def majority_vote(messages):
    attack_count = messages.count("ATTACK")
    retreat_count = messages.count("RETREAT")

    if attack_count >= retreat_count:
        return "ATTACK"

    return "RETREAT"


def check_consensus(decisions):
    unique_decisions = set(decisions.values())
    return len(unique_decisions) == 1


def exchange_messages(
    generals,
    first_round_messages,
    original_order="ATTACK",
    strategy="split"
):
    second_round_messages = {}

    for receiver in generals:
        second_round_messages[receiver.general_id] = {}

        for sender in generals:
            if sender.general_id != receiver.general_id:
                if sender.is_traitor:
                    claimed_message = traitor_message(
                        strategy,
                        sender,
                        receiver,
                        original_order
                    )
                else:
                    sender_messages = first_round_messages[sender.general_id]
                    claimed_message = majority_vote(sender_messages)

                second_round_messages[receiver.general_id][sender.general_id] = claimed_message

    return second_round_messages


def make_final_decisions(
    generals,
    first_round_messages,
    second_round_messages
):
    final_decisions = {}

    for general in generals:
        if not general.is_traitor:
            all_messages = []

            all_messages.extend(first_round_messages[general.general_id])
            all_messages.extend(second_round_messages[general.general_id].values())

            final_decisions[general.general_id] = majority_vote(all_messages)

    return final_decisions


def run_single_experiment(
    number_of_generals,
    number_of_traitors,
    original_order="ATTACK",
    strategy="split"
):
    generals = create_generals(number_of_generals, number_of_traitors)

    first_round_messages = collect_messages(
        generals,
        original_order,
        strategy
    )

    second_round_messages = exchange_messages(
        generals,
        first_round_messages,
        original_order,
        strategy
    )

    final_decisions = make_final_decisions(
        generals,
        first_round_messages,
        second_round_messages
    )

    consensus = check_consensus(final_decisions)

    return {
        "generals": generals,
        "first_round_messages": first_round_messages,
        "second_round_messages": second_round_messages,
        "final_decisions": final_decisions,
        "consensus": consensus
    }


def run_experiments(
    number_of_runs,
    number_of_generals,
    number_of_traitors,
    original_order="ATTACK",
    strategy="split"
):
    successful_consensus = 0
    failed_consensus = 0

    for _ in range(number_of_runs):
        experiment = run_single_experiment(
            number_of_generals,
            number_of_traitors,
            original_order,
            strategy
        )

        if experiment["consensus"]:
            successful_consensus += 1
        else:
            failed_consensus += 1

    success_rate = (successful_consensus / number_of_runs) * 100

    return {
        "runs": number_of_runs,
        "generals": number_of_generals,
        "traitors": number_of_traitors,
        "strategy": strategy,
        "successful_consensus": successful_consensus,
        "failed_consensus": failed_consensus,
        "success_rate": success_rate
    }