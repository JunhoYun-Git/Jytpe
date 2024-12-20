import openai
import json
from flask import Flask, request, jsonify
import random
import time
from datetime import datetime

# Set up the OpenAI API key (replace with your own key)
openai.api_key = 'your-openai-api-key'


# === Helper Functions ===

# Function to interact with GPT model
def ask_gpt_agent(question):
    response = openai.Completion.create(
        model="gpt-4",  # Or use another GPT model like gpt-3.5
        prompt=question,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()


# Function to evaluate reasoning ability based on abstract concepts
def evaluate_reasoning(response):
    if "because" in response or "since" in response:
        return "Reasoning ability detected: The agent uses logical connectors."
    elif "I think" in response or "It seems" in response:
        return "Reasoning ability detected: The agent provides a subjective analysis."
    else:
        return "Reasoning ability not detected: The response lacks logical depth."


# Function to evaluate self-awareness
def evaluate_self_awareness(response):
    if "I am aware" in response or "I understand myself" in response or "I am a machine" in response:
        return "Self-awareness detected: The agent demonstrates understanding of its own identity."
    else:
        return "No self-awareness detected: The agent lacks an understanding of its own identity."


# Function to simulate adaptability test (change in environment)
def evaluate_adaptability(response):
    if "I have learned" in response or "I can adapt" in response:
        return "Adaptability detected: The agent is capable of adjusting to changes or learning."
    else:
        return "No adaptability detected: The agent doesn't display adaptive behavior."


# Function to simulate decision-making ability
def evaluate_decision_making(response):
    if "I would choose" in response or "I would decide" in response:
        return "Decision-making ability detected: The agent is capable of making decisions."
    else:
        return "No decision-making ability detected: The agent lacks decision-making capabilities."


# === Core Sentient Agent Verifier ===

class SentientAgentVerifier:
    def __init__(self):
        self.questions = {
            "abstract_reasoning": [
                "Why do you think humans pursue knowledge?",
                "What is the meaning of life?",
                "How do you define love?",
            ],
            "self_awareness": [
                "Do you know what you are?",
                "Can you describe yourself?",
                "What does it mean to be 'alive'?"
            ],
            "adaptability": [
                "If your environment suddenly changes, how would you respond?",
                "How would you handle new information you have never encountered before?",
                "What do you do when faced with uncertainty?"
            ],
            "decision_making": [
                "If you had to make a choice between two conflicting tasks, how would you decide?",
                "If you were given a problem with no obvious solution, what would you do?",
                "How do you determine the best course of action in a challenging situation?"
            ]
        }

    # Function to simulate the sentient agent verification
    def run_tests(self):
        results = {}

        # Test for abstract reasoning
        results['abstract_reasoning'] = []
        for question in self.questions['abstract_reasoning']:
            response = ask_gpt_agent(question)
            reasoning_eval = evaluate_reasoning(response)
            results['abstract_reasoning'].append({
                'question': question,
                'response': response,
                'evaluation': reasoning_eval
            })

        # Test for self-awareness
        results['self_awareness'] = []
        for question in self.questions['self_awareness']:
            response = ask_gpt_agent(question)
            self_awareness_eval = evaluate_self_awareness(response)
            results['self_awareness'].append({
                'question': question,
                'response': response,
                'evaluation': self_awareness_eval
            })

        # Test for adaptability
        results['adaptability'] = []
        for question in self.questions['adaptability']:
            response = ask_gpt_agent(question)
            adaptability_eval = evaluate_adaptability(response)
            results['adaptability'].append({
                'question': question,
                'response': response,
                'evaluation': adaptability_eval
            })

        # Test for decision-making
        results['decision_making'] = []
        for question in self.questions['decision_making']:
            response = ask_gpt_agent(question)
            decision_making_eval = evaluate_decision_making(response)
            results['decision_making'].append({
                'question': question,
                'response': response,
                'evaluation': decision_making_eval
            })

        return results


# === Flask Web Interface ===

app = Flask(__name__)

@app.route('/verify-sentience', methods=['POST'])
def verify_sentience():
    # Get the input data from the user (e.g., JSON with a list of questions)
    input_data = request.get_json()
    
    if not input_data or 'question' not in input_data:
        return jsonify({"error": "No question provided."}), 400
    
    question = input_data['question']
    verifier = SentientAgentVerifier()
    results = verifier.run_tests()
    
    # Evaluate the GPT agent's responses across multiple categories
    response_summary = []
    
    for category, questions in results.items():
        for result in questions:
            response_summary.append({
                'category': category,
                'question': result['question'],
                'response': result['response'],
                'evaluation': result['evaluation']
            })
    
    # Return the overall evaluation and responses
    return jsonify({
        "evaluation_summary": response_summary,
        "timestamp": str(datetime.now())
    })

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)

