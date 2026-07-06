import os
import networkx as nx
import matplotlib.pyplot as plt


def visualize_first_round(generals, messages, filename="first_round.png"):
    os.makedirs("visualizations", exist_ok=True)

    graph = nx.DiGraph()

    for general in generals:
        graph.add_node(general.general_id)

    for receiver in generals:
        receiver_id = receiver.general_id

        sender_index = 0

        for sender in generals:
            if sender.general_id != receiver_id:
                message = messages[receiver_id][sender_index]

                graph.add_edge(
                    sender.general_id,
                    receiver_id,
                    message=message
                )

                sender_index += 1

    node_colors = []

    for general in generals:
        if general.is_traitor:
            node_colors.append("red")
        else:
            node_colors.append("lightblue")

    positions = nx.spring_layout(graph, seed=42)

    plt.figure(figsize=(10, 7))

    nx.draw(
        graph,
        positions,
        with_labels=True,
        node_color=node_colors,
        node_size=1600,
        font_size=10,
        arrows=True
    )

    edge_labels = nx.get_edge_attributes(graph, "message")

    nx.draw_networkx_edge_labels(
        graph,
        positions,
        edge_labels=edge_labels,
        font_size=8
    )

    plt.title("First Round Messages")
    plt.savefig(f"visualizations/{filename}")
    plt.close()