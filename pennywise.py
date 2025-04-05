import random
import pandas as pd
from sklearn.linear_model import LinearRegression
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

# Step 1: Generate mock training data
categories = ["Food", "Transport", "Groceries", "Entertainment", "Shopping", "Utilities", "Health", "Education"]
mock_data = []

for user_id in range(1, 21):  # 20 users
    income = random.randint(20000, 80000)

    for category in categories:
        monthly_spending = round(random.uniform(0.05, 0.35) * income, 2)
        volatility = random.uniform(0.05, 0.20)
        suggested_budget = round(monthly_spending * (1 + volatility), 2)

        mock_data.append({
            "user_id": user_id,
            "category": category,
            "monthly_spending": monthly_spending,
            "monthly_income": income,
            "suggested_budget": suggested_budget
        })

df = pd.DataFrame(mock_data)
df.to_csv("mock_budget_dataset.csv", index=False)

# Step 2: Train the regression model
mock_df = pd.read_csv("mock_budget_dataset.csv")
X_train = mock_df[["monthly_spending", "monthly_income"]]
y_train = mock_df["suggested_budget"]

model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Sample user transactions
transactions = [
    {'amount': 100000, 'type': 'income', 'category': 'Salary', 'description': 'Monthly Salary', 'date': '2025-04-01'},
    {'amount': 2000, 'type': 'income', 'category': 'Interest', 'description': 'Savings Account Interest', 'date': '2025-04-10'},
    {'amount': 1000, 'type': 'income', 'category': 'Cashback', 'description': 'Credit Card Cashback', 'date': '2025-04-15'},
    {'amount': 500, 'type': 'expense', 'category': 'Food', 'description': 'Zomato Order', 'date': '2025-04-01'},
    {'amount': 1200, 'type': 'expense', 'category': 'Transport', 'description': 'Cab to work', 'date': '2025-04-02'},
    {'amount': 400, 'type': 'expense', 'category': 'Food', 'description': 'Grocery Shopping', 'date': '2025-04-03'},
    {'amount': 250, 'type': 'expense', 'category': 'Miscellaneous', 'description': 'Coffee Shop', 'date': '2025-04-04'},
    {'amount': 1800, 'type': 'expense', 'category': 'Utilities', 'description': 'Electricity Bill', 'date': '2025-04-05'},
    {'amount': 12000, 'type': 'expense', 'category': 'Rent/Bills', 'description': 'Monthly Rent', 'date': '2025-04-06'},
    {'amount': 5000, 'type': 'expense', 'category': 'EMI', 'description': 'Home Loan EMI', 'date': '2025-04-07'},
    {'amount': 600, 'type': 'expense', 'category': 'Entertainment', 'description': 'Netflix + Prime', 'date': '2025-04-08'},
    {'amount': 150, 'type': 'expense', 'category': 'Transport', 'description': 'Bus Fare', 'date': '2025-04-09'},
    {'amount': 200, 'type': 'expense', 'category': 'Food', 'description': 'Zomato Order', 'date': '2025-04-10'},
    {'amount': 300, 'type': 'expense', 'category': 'Food', 'description': 'Lunch Outside', 'date': '2025-04-11'},
    {'amount': 500, 'type': 'expense', 'category': 'Miscellaneous', 'description': 'Online Shopping', 'date': '2025-04-12'},
    {'amount': 1000, 'type': 'expense', 'category': 'Utilities', 'description': 'Internet Bill', 'date': '2025-04-13'},
    {'amount': 200, 'type': 'expense', 'category': 'Transport', 'description': 'Fuel', 'date': '2025-04-14'},
    {'amount': 400, 'type': 'expense', 'category': 'Food', 'description': 'Swiggy Order', 'date': '2025-04-15'},
    {'amount': 350, 'type': 'expense', 'category': 'Entertainment', 'description': 'Movie Night', 'date': '2025-04-16'},
    {'amount': 300, 'type': 'expense', 'category': 'Miscellaneous', 'description': 'Gift', 'date': '2025-04-17'},
    {'amount': 150, 'type': 'expense', 'category': 'Transport', 'description': 'Metro Recharge', 'date': '2025-04-18'},
    {'amount': 700, 'type': 'expense', 'category': 'Food', 'description': 'Restaurant Dinner', 'date': '2025-04-19'},
    {'amount': 200, 'type': 'expense', 'category': 'Food', 'description': 'Zomato Order', 'date': '2025-04-20'},
    {'amount': 1800, 'type': 'expense', 'category': 'Utilities', 'description': 'Gas Bill', 'date': '2025-04-21'},
    {'amount': 400, 'type': 'expense', 'category': 'Entertainment', 'description': 'Spotify Annual', 'date': '2025-04-22'},
    {'amount': 150, 'type': 'expense', 'category': 'Transport', 'description': 'Auto Fare', 'date': '2025-04-23'},
    {'amount': 500, 'type': 'expense', 'category': 'Food', 'description': 'Zomato Order', 'date': '2025-04-24'},
    {'amount': 200, 'type': 'expense', 'category': 'Miscellaneous', 'description': 'Snacks', 'date': '2025-04-25'},
    {'amount': 1000, 'type': 'expense', 'category': 'Entertainment', 'description': 'Concert Ticket', 'date': '2025-04-26'},
    {'amount': 500, 'type': 'expense', 'category': 'Utilities', 'description': 'Water Bill', 'date': '2025-04-27'},
    {'amount': 300, 'type': 'expense', 'category': 'Transport', 'description': 'Taxi', 'date': '2025-04-28'},
    {'amount': 250, 'type': 'expense', 'category': 'Food', 'description': 'Fast Food', 'date': '2025-04-29'},
    {'amount': 400, 'type': 'expense', 'category': 'Miscellaneous', 'description': 'Stationery', 'date': '2025-04-30'}
]
current_month = datetime.now().month
category_totals = defaultdict(float)

for tx in transactions:
    try:
        date_obj = datetime.strptime(tx.get('date', ''), '%Y-%m-%d')
    except ValueError:
        continue
    if tx['type'] == 'expense' and date_obj.month == current_month:
        category_totals[tx['category']] += tx['amount']

# Step 2: Prepare data for pie chart
labels = list(category_totals.keys())
sizes = list(category_totals.values())

# Step 3: Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Expense Distribution by Category (This Month)', fontsize=14)
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.
plt.show()

# Step 4: Budget suggestion + savings goal forec
def suggest_budget(transactions, savings_goal=10000):
    expenses = defaultdict(list)
    total_income = 0
    current_month = datetime.now().month

    # Aggregate transactions
    for tx in transactions:
        try:
            date_obj = datetime.strptime(tx.get('date', '2025-04-01'), '%Y-%m-%d')
        except ValueError:
            continue

        if date_obj.month == current_month:
            if tx['type'] == 'expense':
                expenses[tx['category']].append(tx['amount'])
            elif tx['type'] == 'income':
                total_income += tx['amount']

    print("🤖 AI-Powered Budget Suggestions:")

    total_suggested_budget = 0
    suggested_budgets = {}

    for category, amounts in expenses.items():
        monthly_spending = sum(amounts)
        input_df = pd.DataFrame([[monthly_spending, total_income]], columns=["monthly_spending", "monthly_income"])
        predicted_budget = model.predict(input_df)[0]
        suggested_budgets[category] = predicted_budget
        total_suggested_budget += predicted_budget
        print(f"{category}: ₹{predicted_budget:.2f} (based on your habits)")

    # Calculate savings forecast
    remaining_after_budget = total_income - total_suggested_budget
    if remaining_after_budget > 0:
        months_to_goal = savings_goal / remaining_after_budget
        print(f"\n📈 Savings Goal Forecast:")
        print(f"You can reach your ₹{savings_goal} goal in approximately {months_to_goal:.1f} months if you follow the suggested budget.")
    else:
        print("\n⚠️ Warning: Your budget exceeds your income. Consider adjusting expenses to achieve savings.")

    print(f"\n💰 Total Income this month: ₹{total_income:.2f}")
    print(f"📊 Total Suggested Budget: ₹{total_suggested_budget:.2f}")
    print(f"💵 Potential Savings: ₹{remaining_after_budget:.2f}")

#main
goal=int(input("enter savings goal: "))
suggest_budget(transactions, savings_goal=goal)


