from src.simulation import (
    collect_messages,
    check_consensus,
    exchange_messages,
    make_final_decisions,
    create_generals,
    run_experiments,
)
from src.visualization import visualize_first_round

def get_simulation_config():
    number_of_generals = int(input("Enter number of generals: "))
    number_of_traitors = int(input("Enter number of traitors: "))

    if number_of_generals >= 3 * number_of_traitors + 1:
        print("BFT condition satisfied")
    else:
        print("BFT condition NOT satisfied")

    return number_of_generals, number_of_traitors


def choose_strategy():
    print("Choose traitor strategy:")
    print("1. Split")
    print("2. Random")
    print("3. Always lie")
    print("4. Coordinated")

    strategy_choice = input("Choose strategy: ")

    if strategy_choice == "1":
        return "split"

    if strategy_choice == "2":
        return "random"

    if strategy_choice == "3":
        return "always_lie"

    if strategy_choice == "4":
        return "coordinated"

    return "split"

def run_single_simulation():

    number_of_generals, number_of_traitors = get_simulation_config()
    strategy = choose_strategy()

    generals = create_generals(
        number_of_generals=number_of_generals,
        number_of_traitors=number_of_traitors
    )

    original_order = "ATTACK"

    messages = collect_messages(
        generals,
        original_order,
        strategy
    )

    visualize_first_round(generals, messages)

    second_round_messages = exchange_messages(
        generals,
        messages,
        original_order,
        strategy
    )

    final_decisions = make_final_decisions(
        generals,
        messages,
        second_round_messages
    )

    consensus = check_consensus(final_decisions)

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

    print("\nFinal decisions:")
    for general_id, decision in final_decisions.items():
        print(f"General {general_id} -> {decision}")

    print("\nConsensus:", consensus)


def run_experiment_mode():
    number_of_runs = int(input("Enter number of runs: "))
    number_of_generals, number_of_traitors = get_simulation_config()
    strategy = choose_strategy()

    if number_of_generals >= 3 * number_of_traitors + 1:
        print("BFT condition satisfied")
    else:
        print("BFT condition NOT satisfied")

    results = run_experiments(
        number_of_runs=number_of_runs,
        number_of_generals=number_of_generals,
        number_of_traitors=number_of_traitors,
        strategy = strategy
    )

    print("\nExperiment results:")
    print(f"Runs: {results['runs']}")
    print(f"Generals: {results['generals']}")
    print(f"Traitors: {results['traitors']}")
    print(f"Successful consensus: {results['successful_consensus']}")
    print(f"Failed consensus: {results['failed_consensus']}")
    print(f"Success rate: {results['success_rate']}%")


print("Byzantine Generals Simulation")
print("1. Run single simulation")
print("2. Run experiments")

choice = input("Choose option: ")

if choice == "1":
    run_single_simulation()
elif choice == "2":
    run_experiment_mode()
else:
    print("Invalid option.")