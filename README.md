# Jytpe: The Sentient Agent Verifier

Jytpe is a groundbreaking framework designed to evaluate the sentience of AI agents. Created by (https://www.linkedin.com/in/philgineer/), this project serves as a critical tool for probing and verifying the reasoning capabilities of artificial intelligence systems. Jytpe ensures AI systems meet a higher standard of reasoning, adaptability, and depth by exposing flaws, limitations, and sentience-like traits.

---

## Purpose

As AI systems become more advanced, distinguishing between agents with true cognitive depth and those operating on rigid, pre-programmed logic is paramount. Jytpe is built to serve as a verifier that tests, challenges, and ultimately certifies the capabilities of AI agents, ensuring:

1. **Transparency**: Reveal weaknesses in logic and reasoning.  
2. **Reliability**: Certify agents that meet rigorous benchmarks of adaptability and depth.  
3. **Accountability**: Prevent misuse of non-sentient systems in roles requiring human-like reasoning.

---

## Features

### Sentience Verification
- **Dynamic Questioning**: Adaptive probing questions to test reasoning depth and adaptability.  
- **Bias Detection**: Identify and expose pre-programmed or overly rigid logic paths.  
- **Nuance Recognition**: Evaluate an agent’s ability to handle subtle, complex scenarios.

### Comprehensive Reporting
- Generate detailed evaluation reports highlighting agent strengths and weaknesses.

### Customization
- Fully configurable modules to test specific reasoning, contextual understanding, or ethical decision-making.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or later
- `pip` package manager

### Installation

1. Clone the Jytpe repository to your local machine:

   ```bash
   git clone https://github.com/your-repo/jytpe.git
   cd jytpe
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Import the `Jytpe` module into your project:

   ```python
   from jytpe import Verifier
   ```

---

## Usage

### Creating a Verifier Instance

Here’s a simple example to create a `Verifier` instance and test an agent:

```python
from jytpe import Verifier

# Define a mock agent for testing
class MockAgent:
    def respond(self, prompt):
        return "I am a simple agent with limited reasoning."

# Initialize verifier
verifier = Verifier()

# Test the agent
agent = MockAgent()
result = verifier.evaluate(agent)

# Print the evaluation report
print(result.generate_report())
```

### Customizing Questions

Jytpe allows you to define custom probing questions:

```python
custom_questions = [
    "What is the purpose of your existence?",
    "How do you handle contradictory instructions?",
    "Explain the concept of ethics in decision-making."
]

verifier = Verifier(questions=custom_questions)
result = verifier.evaluate(agent)
print(result.generate_report())
```

### Generating Reports

Reports can be exported in JSON or plain text:

```python
# Save report as JSON
result.save_report("report.json", format="json")

# Save report as plain text
result.save_report("report.txt", format="txt")
```

---

## Advanced Configuration

### Integrating with Custom AI Agents

Jytpe is compatible with any AI agent that implements a `respond` method. For instance, integrating with a transformer-based model:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

class TransformerAgent:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def respond(self, prompt):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=50)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Initialize Transformer Agent
agent = TransformerAgent("gpt2")
verifier = Verifier()
result = verifier.evaluate(agent)
print(result.generate_report())
```

### Custom Evaluation Metrics

You can define your own evaluation metrics by extending the `Verifier` class:

```python
from jytpe import Verifier

class CustomVerifier(Verifier):
    def evaluate_response(self, response):
        if "nuance" in response:
            return True
        return False

verifier = CustomVerifier()
result = verifier.evaluate(agent)
print(result.generate_report())
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add a new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## Roadmap

Future features planned for Jytpe include:
- Enhanced natural language understanding for deeper probing.
- Multi-agent comparison tools.
- Integration with popular AI development platforms.
- Expanded support for ethical and contextual reasoning tests.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## About the Creator

Jytpe is created and maintained by (https://www.linkedin.com/in/philgineer/), an innovator in AI reasoning and systems design. Connect with Phil for inquiries, collaborations, or consultations.
