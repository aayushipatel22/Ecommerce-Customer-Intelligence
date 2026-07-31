from langgraph_ai.graph import graph


def chat():

    print("=" * 60)
    print("AI Customer Intelligence Assistant")
    print("=" * 60)

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        result = graph.invoke(
            {
                "question": question,
                "context": "",
                "answer": "",
            }
        )

        print("\nAnswer:\n")

        print(result["answer"])


if __name__ == "__main__":
    chat()

# cmd--> D:\Data\Documents\Ecomm_Cust_intelligence_Project\venv\Scripts\python.exe -m langgraph_ai.run_chatbot