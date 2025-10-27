# Alith Story Orchestrator: Multi-Agent Collaboration Demo

This repository contains a simple prototype demonstrating multi-agent collaboration using the Alith SDK. It showcases two agents – a `Plot Generator` and a `Narrative Refiner` – working together to create a story, with Decentralized Autonomous Transactions (DATs) used for validation and reward handling.

## Table of Contents
- [Project Overview](#project-overview)
- [How it Works](#how-it-works)
- [Agents Explained](#agents-explained)
- [Installation](#installation)
- [Usage](#usage)
- [Conceptual Alith Integration](#conceptual-alith-integration)
- [Screenshots & Demo](#screenshots--demo)
- [License](#license)

## Project Overview

The goal of this project is to illustrate:
1.  How two distinct AI agents can interact and pass tasks/data.
2.  The application of Alith's Decentralized Autonomous Transactions (DATs) for post-task validation and incentivization.

**Scenario:** A collaborative story writing process where one agent generates a basic plot outline, and another refines it into a detailed narrative.

## How it Works

1.  **Initialization:** The `orchestrator.py` script starts the process.
2.  **Plot Generation:** The `Plot Generator` agent creates a high-level story premise, conflict, and resolution.
3.  **Task Handover:** The plot outline is passed as data to the `Narrative Refiner`.
4.  **Narrative Refinement:** The `Narrative Refiner` agent takes the plot data and expands it into a richer, more descriptive story.
5.  **Validation & Reward (DAT):** Upon completion, a DAT is conceptually submitted to the Alith network. This DAT would include validation parameters (e.g., minimum word count, keyword presence) to ensure the refined narrative meets quality standards. If validation passes, a reward is conceptually triggered for the `Narrative Refiner`.

## Agents Explained

### 1. `Plot Generator` (`agents/plot_generator.py`)
-   **Role:** To conceive and outline the core elements of a story.
-   **Output:** A JSON-like dictionary containing `premise`, `conflict`, and `resolution`.
-   **Interaction:** Passes this structured data to the `Narrative Refiner`.

### 2. `Narrative Refiner` (`agents/narrative_refiner.py`)
-   **Role:** To elaborate on a given plot outline, transforming it into a compelling narrative.
-   **Input:** The plot outline from the `Plot Generator`.
-   **Output:** A detailed, multi-paragraph story.
-   **Interaction:** Submits a DAT to the Alith network for validation of its work.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/thamothara7/alith-story-orchestrator.git](https://github.com/thamothara7/alith-story-orchestrator.git)
    cd alith-story-orchestrator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Alith SDK Setup (Conceptual):**
    This demo assumes you have access to an Alith client and network. In a real-world scenario, you would configure your `ALITH_API_KEY` and other credentials in a `.env` file.
    Copy `.env.example` to `.env` and fill in your details:
    ```bash
    cp .env.example .env
    ```
    Then, open `.env` and add:
    ```
    ALITH_API_KEY="your_alith_api_key_here"
    # Other Alith configuration parameters if needed
    ```

## Usage

Run the main orchestrator script:

```bash
python orchestrator.py