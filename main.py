from agent import create_agent

def main():
    agent = create_agent()
    print("\nWelcome to the AI Product Advisor (Gemini)! Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.invoke(query)
        print(f"Advisor: {response}\n")

if __name__ == "__main__":
    main()
