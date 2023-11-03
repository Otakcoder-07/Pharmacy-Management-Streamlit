import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='your_mysql_host',  # Replace with your MySQL host address
    user='your_mysql_user',  # Replace with your MySQL username
    password='your_mysql_password',  # Replace with your MySQL password
    database='your_database_name'  # Replace with your database name
)
cursor = conn.cursor()

# Function to add a company
def add_company(name, address, phone):
    cursor.execute('INSERT INTO companies (name, address, phone) VALUES (%s, %s, %s)', (name, address, phone))
    conn.commit()

# Function to add a user
def add_user(name, email, role):
    cursor.execute('INSERT INTO users (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
    conn.commit()

# Function to add a drug
def add_drug(name, type, barcode, dose, code, cost_price, selling_price, expiry, company_name, production_date, expiration_date, place, quantity):
    cursor.execute('INSERT INTO drugs (name, type, barcode, dose, code, cost_price, selling_price, expiry, company_name, production_date, expiration_date, place, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (name, type, barcode, dose, code, cost_price, selling_price, expiry, company_name, production_date, expiration_date, place, quantity))
    conn.commit()

# Streamlit UI
st.title('Pharmacy Management System')

# Add Company Section
st.header('Add Company')
company_name = st.text_input('Company Name')
company_address = st.text_input('Company Address')
company_phone = st.text_input('Company Phone')

if st.button('Submit Company'):
    add_company(company_name, company_address, company_phone)
    st.success('Company added successfully!')

# Add User Section
st.header('Add User')
user_name = st.text_input('User Name')
user_email = st.text_input('User Email')
user_role = st.selectbox('User Role', ['admin', 'staff'])

if st.button('Submit User'):
    add_user(user_name, user_email, user_role)
    st.success('User added successfully!')

# Add Drug Section
st.header('Add Drug')
drug_name = st.text_input('Drug Name')
drug_type = st.text_input('Type')
drug_barcode = st.text_input('Barcode')
drug_dose = st.text_input('Dose')
drug_code = st.text_input('Code')
drug_cost_price = st.number_input('Cost Price', value=0.0, step=0.01)
drug_selling_price = st.number_input('Selling Price', value=0.0, step=0.01)
drug_expiry = st.text_input('Expiry')
drug_company_name = st.text_input('Company Name')
drug_production_date = st.date_input('Production Date')
drug_expiration_date = st.date_input('Expiration Date')
drug_place = st.text_input('Place')
drug_quantity = st.number_input('Quantity', value=0)

if st.button('Submit Drug'):
    add_drug(drug_name, drug_type, drug_barcode, drug_dose, drug_code, drug_cost_price, drug_selling_price, drug_expiry, drug_company_name, drug_production_date, drug_expiration_date, drug_place, drug_quantity)
    st.success('Drug added successfully!')

# Close the connection
cursor.close()
conn.close()
