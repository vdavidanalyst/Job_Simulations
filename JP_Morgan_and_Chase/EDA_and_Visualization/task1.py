import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_csv(r'C:\Users\vik\Desktop\Forage Projects\JP_Morgan_and_Chase\transactions.csv')
    df

def exercise_1(df):
    column_names = df.columns.tolist()
    print(column_names)

def exercise_2(df, k):
    k_rows = df.head()
    print(k_rows)

def exercise_3(df, k):
    k = 3
    random_sample = df.sample(n=k)
    print(random_sample)

def exercise_4(df):
    unique_transaction_types = df['type'].unique().tolist()
    print(unique_transaction_types)
def exercise_5(df):
    top_10_destinations = df['nameDest'].value_counts().head()
    print(top_10_destinations)

def exercise_6(df):
    fraud_was_detected = df[df['isFlaggedFraud'] == 1]

    print(fraud_was_detected)

def exercise_7(df):
    distinct_destinations = df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False).reset_index()
    distinct_destinations.columns = ['nameOrig','Distinct_Dest_Count']
    print(distinct_destinations)
def visual_1(df):
    def transaction_counts(df):
        return df['type'].value_counts()

    def transaction_counts_split_by_fraud(df):
        return df.groupby(['type', 'isFraud']).size().unstack()

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar', color='skyblue')
    axs[0].set_title('Transaction Types Bar Chart')
    axs[0].set_xlabel('Transaction Types')
    axs[0].set_ylabel('Count')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar', stacked=True, color=['skyblue', 'salmon'])
    axs[1].set_title('Transaction Types Split by Fraud Bar Chart')
    axs[1].set_xlabel('Transaction Types')
    axs[1].set_ylabel('Count')
    fig.suptitle('Transaction Types Visualization')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
        for p in ax.patches:
            ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()))
    return 'The visualizations provide insights into the distribution of transaction types and the prevalence of fraud across these types.'
# Call the function to create the graphs and get the description
result_desc = visual_1(df)
print(result_desc)

def visual_2(df):
    def query(df):
        cash_out_df = df[df['type'] == 'CASH_OUT']
        return cash_out_df

    plot = query(df).plot.scatter(x='oldbalanceOrg', y='oldbalanceDest', color='purple', alpha=0.5)
    plot.set_title('Balance Delta Scatter Plot for Cash Out Transactions')
    plot.set_xlabel('Origin Account Balance Delta')
    plot.set_ylabel('Destination Account Balance Delta')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'The scatter plot showcases the relationship between the change in origin account balance and the change in destination account balance for Cash Out transactions.'

    # Call the function to create the scatter plot and get the description
    result_desc = visual_2(df)
    print(result_desc)

def exercise_custom(df):
     # TODO: Perform the custom exercise on the DataFrame
    custom_result = df.groupby('type')['amount'].sum()
    return custom_result
    
def visual_custom(df):
    custom_data = exercise_custom(df)
    custom_plot = custom_data.plot(kind='bar', figsize=(8, 6), color='green')
    custom_plot.set_title('Custom Exercise: Total Amount by Transaction Type')
    custom_plot.set_xlabel('Transaction Types')
    custom_plot.set_ylabel('Total Amount')
    for p in custom_plot.patches:
        custom_plot.annotate(str(p.get_height()), (p.get_x(), p.get_height()))
    return 'The bar chart demonstrates the total transaction amount for each transaction type, providing insights into the distribution of monetary values across different transaction types.'


    # Call the function to perform the custom exercise and create the visualization, and get the description
    result_custom = exercise_custom(df)
    desc_custom = visual_custom(df)
    print(result_custom)
    print(desc_custom)
s
