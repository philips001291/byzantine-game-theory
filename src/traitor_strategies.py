import random

def opposite(order):
    if order == "ATTACK":
        return "RETREAT"
    return "ATTACK"


def split_strategy(receiver):
    if receiver.general_id % 2 == 0:
        return "ATTACK"
    return "RETREAT"


def random_strategy():
    return random.choice(["ATTACK", "RETREAT"])


def always_lie_strategy(original_order):
    return opposite(original_order)


def coordinated_strategy(sender, receiver):
    if sender.general_id < receiver.general_id:
        return "ATTACK"
    return "RETREAT"


def traitor_message(strategy, sender, receiver, original_order):
    if strategy == "split":
        return split_strategy(receiver)

    if strategy == "random":
        return random_strategy()

    if strategy == "always_lie":
        return always_lie_strategy(original_order)

    if strategy == "coordinated":
        return coordinated_strategy(sender, receiver)

    return split_strategy(receiver)