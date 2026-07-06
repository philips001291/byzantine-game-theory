import csv
import os
import matplotlib.pyplot as plt

from src.simulation import run_experiments


def save_results_to_csv(results, filename="data/experiments.csv"):
    os.makedirs("data", exist_ok=True)

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "runs",
                "generals",
                "traitors",
                "strategy",
                "successful_consensus",
                "failed_consensus",
                "success_rate"
            ]
        )

        writer.writeheader()
        writer.writerows(results)


def plot_success_rate(results, filename="visualizations/consensus_success_rate.png"):
    os.makedirs("visualizations", exist_ok=True)

    strategies = set()

    for result in results:
        strategies.add(result["strategy"])


    plt.figure(figsize=(8, 5))


    for strategy in strategies:

        strategy_results = []

        for result in results:
            if result["strategy"] == strategy:
                strategy_results.append(result)


        traitors = []
        success_rates = []


        for result in strategy_results:
            traitors.append(result["traitors"])
            success_rates.append(result["success_rate"])


        plt.plot(
            traitors,
            success_rates,
            marker="o",
            label=strategy
        )


    plt.xlabel("Number of traitors")
    plt.ylabel("Consensus success rate (%)")
    plt.title("Byzantine fault tolerance")

    plt.ylim(0, 105)

    plt.legend()
    plt.grid(True)

    plt.savefig(filename)
    plt.close()

def main():

    results = []
    
    strategies = ["split", "random", "always_lie", "coordinated"]

    for strategy in strategies:
        for traitors in range(0, 4):
            result = run_experiments(
                number_of_runs=100,
                number_of_generals=6,
                number_of_traitors=traitors,
                strategy=strategy
            )
            results.append(result)


    save_results_to_csv(results)
    plot_success_rate(results)

    print("Experiments finished.")
    print("Results saved to data/experiments.csv")
    print("Graph saved to visualizations/consensus_success_rate.png")


if __name__ == "__main__":
    main()