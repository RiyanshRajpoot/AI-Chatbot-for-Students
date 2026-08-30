from chatbot import StudentChatbot

def run_chatbot():
    bot = StudentChatbot()
    print("=" * 60)
    print("      Welcome to AI Student Chatbot (CodSoft Project)      ")
    print("=" * 60)
    print("Bot: Hello! I'm your AI Assistant. Type 'exit' or 'bye' to leave.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                print("Bot: Please type something so I can help you.")
                continue

            response = bot.get_response(user_input)
            print(f"Bot: {response}\n")

            # Exit condition check
            cleaned_input = bot.clean_text(user_input)
            if cleaned_input in ["exit", "quit", "bye", "goodbye"]:
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Bot: An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_chatbot()
