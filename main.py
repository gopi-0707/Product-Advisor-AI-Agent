# Entry point for interacting with the AI Product Advisor Agent via CLI

from agent import create_agent

def main():
    # Initialize the agent
    agent = create_agent()
    print("\nWelcome to the AI Product Advisor (Gemini)! Type 'exit' to quit.\n")
    while True:
        # Take user query as input
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break

        # Invoke the agent and print its response
        response = agent.invoke(query)
        print(f"Advisor: {response}\n")

# Run the CLI if this file is executed directly
if __name__ == "__main__":
    main()
