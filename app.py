# financial_chatbot.py

# Static data from analysis
data_2023 = {
    "Total Revenue": 220000,
    "Net Income": 72000,
    "Total Assets": 470000,
    "Total Liabilities": 180000
}

data_2024 = {
    "Total Revenue": 232000,
    "Net Income": 83000,
    "Total Assets": 490000,
    "Total Liabilities": 185000
}

def simple_chatbot(user_query):
    user_query = user_query.lower()

    if "total revenue" in user_query:
        return f"The total revenue in 2024 was ${data_2024['Total Revenue']:,} million."

    elif "net income changed" in user_query or "net income difference" in user_query:
        diff = data_2024["Net Income"] - data_2023["Net Income"]
        if diff > 0:
            return f"The net income has increased by ${diff:,} million from 2023 to 2024."
        elif diff < 0:
            return f"The net income has decreased by ${abs(diff):,} million from 2023 to 2024."
        else:
            return "The net income remained the same from 2023 to 2024."

    elif "total assets" in user_query:
        return f"The total assets in 2024 were valued at ${data_2024['Total Assets']:,} million."

    elif "total liabilities" in user_query:
        return f"The total liabilities in 2024 were ${data_2024['Total Liabilities']:,} million."

    elif "company perform" in user_query or "performance" in user_query:
        rev_change = data_2024["Total Revenue"] - data_2023["Total Revenue"]
        net_change = data_2024["Net Income"] - data_2023["Net Income"]
        return (f"From 2023 to 2024, total revenue increased by ${rev_change:,} million "
                f"and net income changed by ${net_change:,} million.")

    else:
        return "Sorry, I can only provide information on predefined financial queries."

def main():
    print("Welcome to the Financial Chatbot! Ask about Microsoft's financials.")
    print("Try questions like 'What is the total revenue?' or 'How has net income changed over the last year?'")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
