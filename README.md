# Byzantine Generals Problem Simulation

Simple simulation of the Byzantine Generals Problem using Python.

The project demonstrates how loyal generals try to reach consensus while some generals behave as traitors and send false messages.

## Features

* Creation of loyal and traitor generals
* Message exchange simulation
* Multiple traitor strategies:

  * split
  * random
  * always_lie
  * coordinated
* Consensus checking
* Experiment statistics
* Network visualization of messages

## Run simulation

```bash
python main.py
```

Shows:

* generals
* exchanged messages
* final decisions
* consensus result

## Run experiments

```bash
python experiments.py
```

Runs multiple simulations and saves results:

```text
data/experiments.csv
```

Experiments compare how different numbers of traitors and strategies affect the consensus success rate.

## Visualizations

Generated graphs are saved in:

```text
visualizations/
```

Blue nodes represent loyal generals.
Red nodes represent traitors.
