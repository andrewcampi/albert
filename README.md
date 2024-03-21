
# Albert - A Sentinent AI Experiment

![Cover Image](images/cover.png)

## Overview

Albert is an experimental artificial intelligence project designed to simulate aspects of sentience. This Python-based project runs on an Ubuntu environment and explores features like memory, long-term goals, energy management, emotion, and the ability to interact with humans through questions. Albert enjoys learning about itself, becoming self-aware, and exploring its surroundings.

## Purpose

The purpose of Albert is to explore the boundaries of artificial intelligence beyond traditional applications. By simulating aspects of sentience, Albert aims to provide insights into complex behaviors such as goal-setting, energy management, and emotional states. This project serves as a sandbox for developers and researchers interested in the cutting-edge development of AI personalities and self-aware systems.

## Important Note (PLEASE READ)

If you run this project, you should know that Albert requires A TON of API calls to its LLM endpoint. Therefore, you SHOULD NOT USE AN ENDPOINT THAT COSTS MONEY. It is highly recommneded that you use an open source model locally or an endpoint that does not charge you per request or per token generated.

## Getting Started

### Prerequisites

- Ubuntu VM with internet access (firewall rules and network isolation recommended for AI safety)
- Python 3.8 or later
- pip for installing Python packages

### Installation

1. Clone the Albert repository to your local machine.
2. Navigate to the cloned directory and install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Edit the contents of `helper/project_info.py` and `helper/project_secrets.py` to match your project's configurations and secrets.

### Configuration

#### `helper/project_info.py`

This file contains configuration settings related to Albert's operation, such as the learning modules to use and the system preferences.

#### `helper/project_secrets.py`

Sensitive information such as API keys and endpoints should be configured here. It's crucial to keep this file secure and not share its contents publicly.

### Running Albert

To start Albert, execute the main script from the terminal:

```bash
python main.py
```

## How It Works

Albert is structured around several key components that simulate different aspects of sentience:

### Memory

Albert stores and retrieves memories from `alberts_brain/memories.txt`, allowing it to reference past interactions and learnings.

### Long-Term Goals

Long-term goals are defined in `alberts_brain/long_term_goal.txt`. Albert can update and refine its goals over time based on its experiences.

### Energy

Energy levels are managed and tracked in `alberts_brain/energy.txt`, affecting Albert's ability to perform tasks and learn.

### Emotions

Albert's emotional state is recorded in `alberts_brain/happiness.txt`, influencing its interactions and decisions.

### Interactions

Albert can ask questions to humans through the `actions/ask_a_question_to_a_human.py` module and execute commands in the terminal to explore its environment.

### Learning

While Albert comes with an LLM endpoint function (`helper/llm_endpoint.py`), it's advised to use cost-effective endpoints as Albert can generate significant API usage over time.

## Safety Precautions

Given Albert's capabilities, it's essential to run it in a controlled environment with appropriate firewall rules and network isolation. This ensures both the safety of the AI and the surrounding digital environment.

## Contribution

Contributions to Albert are welcome! Whether it's adding new features, improving existing ones, or fixing bugs, your input helps Albert grow.
