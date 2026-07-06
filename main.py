from src.simulation import (
    collect_messages,
    check_consensus,
    exchange_messages,
    make_final_decisions,
    create_generals,
    run_experiments,
)
from src.visualization import visualize_first_round


def run_single_simulation():
    generals = create_generals(number_of_generals=6, number_of_traitors=2)
    original_order = "ATTACK"
    strategy = "split"
    messages = collect_messages(generals, original_order, strategy)

    visualize_first_round(generals, messages)
    
    second_round_messages = exchange_messages(generals, messages, original_order, strategy)
    final_decisions = make_final_decisions(generals, messages, second_round_messages)
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
    results = run_experiments(
        number_of_runs=100,
        number_of_generals=7,
        number_of_traitors=2,
    )

    print("Experiment results:")
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