import openai
import tweepy
import json
from datetime import datetime
import random

# OpenAI API Key
openai.api_key = 'your-openai-api-key'

# Twitter API credentials (replace with your own credentials)
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

# Authenticate to the Twitter API using Tweepy
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# === Helper Functions ===

def ask_gpt_agent(question):
    response = openai.Completion.create(
        model="gpt-4",  # Or use another GPT model like gpt-3.5
        prompt=question,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def evaluate_reasoning(response):
    if "because" in response or "since" in response:
        return "Reasoning ability detected."
    elif "I think" in response or "It seems" in response:
        return "Reasoning ability detected."
    else:
        return "No reasoning ability detected."

def evaluate_self_awareness(response):
    if "I am aware" in response or "I understand myself" in response or "I am a machine" in response:
        return "Self-awareness detected."
    else:
        return "No self-awareness detected."

def evaluate_adaptability(response):
    if "I have learned" in response or "I can adapt" in response:
        return "Adaptability detected."
    else:
        return "No adaptability detected."

def evaluate_decision_making(response):
    if "I would choose" in response or "I would decide" in response:
        return "Decision-making ability detected."
    else:
        return "No decision-making ability detected."

# === Sentient Agent Verifier Class ===

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

# === Twitter Bot Logic ===

def post_to_twitter(message):
    try:
        api.update_status(message)
        print("Successfully posted the tweet.")
    except Exception as e:
        print(f"Error posting tweet: {e}")

def generate_tweet(results):
    tweet = f"Sentient Agent Testing Summary: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    tweet += "Results:\n"
    
    for category, tests in results.items():
        tweet += f"\n--- {category.replace('_', ' ').title()} ---\n"
        for test in tests:
            question = test['question']
            evaluation = test['evaluation']
            tweet += f"Q: {question}\nEvaluation: {evaluation}\n"
            
            if len(tweet) > 280:
                tweet = tweet[:279]  # Ensure it fits within Twitter's 280 character limit
                break
    
    tweet += "\n#AI #SentientAgent #ArtificialIntelligence"
    return tweet

# === Main Function to Run the Process ===

def main():
    verifier = SentientAgentVerifier()
    results = verifier.run_tests()
    
    # Generate a tweet based on the results
    tweet = generate_tweet(results)
    
    # Post the tweet to Twitter
    post_to_twitter(tweet)

if __name__ == "__main__":
    main()
