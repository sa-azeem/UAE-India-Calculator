import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
EXCHANGE_RATE=23.44
st.title("Salary Calculator")


ind_salary = st.number_input("Enter your in-hand post tax monthly salary: ", min_value=0,step=10000)
ind_expanses = st.number_input("Enter your monthly expanses: ", min_value=0,step=10000)
ind_savings=ind_salary-ind_expanses
accomodation= st.selectbox("Select an option", ["1 BHK"])
savings_in_aed=ind_savings/EXCHANGE_RATE

# monthly expenses = 5500 aed
# utilities 800 aed 
# groceries 1000aed 

accomodation_table={
    '1 BHK':{
        'Rent': 5500,
        'Utilities': 800,
        'Groceries': 1000
    }
}

chosen_accomodation=accomodation_table[accomodation]
total_expenses=sum(chosen_accomodation.values())
salary_needed_aed=total_expenses+savings_in_aed



if ind_salary and ind_expanses:
    if ind_expanses>ind_salary:
        st.write("Really? Seriously?")
    else:
        st.write(f"To save same amount of money, you need to earn {round(salary_needed_aed)} AED per month in UAE.")
        st.write(f"Full breakdown: ")


        df=pd.DataFrame(chosen_accomodation.items(), columns=['Expenses', 'Amount (aed)'])
        df.loc[len(df)]=['Savings', round(savings_in_aed)]
        df.index = df.index + 1
        st.dataframe(df)

        fig1, ax1 = plt.subplots()
        ax1.pie(df['Amount (aed)'], labels=df['Expenses'], autopct='%1.1f%%')
        ax1.axis('equal') 
        for text in ax1.texts:
            text.set_color('grey')
        for text in ax1.texts[1::2]:
            text.set_color('black')
        fig1.patch.set_alpha(0)

        st.pyplot(fig1)







