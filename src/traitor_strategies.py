import random

def opposite(order):
    if order == "ATTACK":
        return "RETREAT"
    return "ATTACK"


def split_strategy(sender, receiver, original_order):
    if receiver.general_id % 2 == 0:
        return "ATTACK"
    return "RETREAT"


def random_strategy(sender, receiver, original_order):
    return random.choice(["ATTACK", "RETREAT"])


def always_lie_strategy(sender, receiver, original_order):
    return opposite(original_order)


def coordinated_strategy(sender, receiver, original_order):
    if sender.general_id < receiver.general_id:
        return "ATTACK"
    return "RETREAT"


def traitor_message(strategy, sender, receiver, original_order):
    if strategy == "split":
        return split_strategy(sender, receiver, original_order)

    if strategy == "random":
        return random_strategy(sender, receiver, original_order)

    if strategy == "always_lie":
        return always_lie_strategy(sender, receiver, original_order)

    if strategy == "coordinated":
        return coordinated_strategy(sender, receiver, original_order)

    return split_strategy(sender, receiver, original_order)