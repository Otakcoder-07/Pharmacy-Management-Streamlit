import streamlit as st
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',  
    user='root',  
    password='Shami@2003',  # Replace with your MySQL password
    database='project_pharma'
)
st.session_state.logged_in = False

cursor = conn.cursor()

# Function to add a company
def add_company(name, address, phone):
    cursor.execute('INSERT INTO company (name, address, phone) VALUES (%s, %s, %s)', (name, address, phone))
    conn.commit()

# Function to add a user
def add_user(name, email, role):
    cursor.execute('INSERT INTO users (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
    conn.commit()

# Function to add a drug
def add_drug(name, type, barcode, dose, code, cost_price, selling_price, expiry, company_name, production_date, expiration_date, place, quantity):
    cursor.execute('INSERT INTO drugs (name, type, barcode, dose, code, cost_price, selling_price, expiry, company_name, production_date, expiration_date, place, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (name, type, barcode, dose, code, cost_price, selling_price, expiry, company_name, production_date, expiration_date, place, quantity))
    conn.commit()

# Function to retrieve sales history for a given barcode
def view_sales_history(barcode):
    cursor.execute('SELECT * FROM sales WHERE drug_barcode = %s', (barcode,))
    sales_history = cursor.fetchall()
    return sales_history

# Function to authenticate user
def authenticate_user(name, password):
    cursor.execute('SELECT * FROM users WHERE name = %s AND password = %s', (name, password))
    user = cursor.fetchone()
    return user

# Function to retrieve drug and company information using a JOIN query
def get_drug_company_info():
    cursor.execute('''
        SELECT drugs.name, drugs.type, company.name 
        FROM drugs
        JOIN company ON drugs.company_name = company.name
    ''')
    info = cursor.fetchall()
    return info

# Function to retrieve drugs that are about to expire using a nested query
def get_expiring_drugs():
    cursor.execute('''
        SELECT name, expiration_date
        FROM drugs
        WHERE expiration_date < DATE_ADD(CURDATE(), INTERVAL 1 MONTH)
    ''')
    expiring_drugs = cursor.fetchall()
    return expiring_drugs

# Function to get the total sales for each drug using an aggregate query
def get_total_sales():
    cursor.execute('''
        SELECT name, SUM(quantity) 
        FROM sales 
        GROUP BY name
    ''')
    total_sales = cursor.fetchall()
    return total_sales

# Streamlit UI


# Streamlit UI
st.title('Pharmacy Management System')

# Login Section
st.header('Login')
user_name = st.text_input('User Name')
user_password = st.text_input('Password', type='password')

if st.button('Login'):
    user = authenticate_user(user_name, user_password)
    if user:
        st.success(f'Welcome, {user[1]}!')
        st.session_state.logged_in = True
        st.session_state.user_id = user[0]
    else:
        st.error('Invalid credentials. Please try again.')

# Logout Section
if st.session_state.logged_in:
    if st.button('Logout'):
        st.session_state.pop('logged_in')
        st.session_state.pop('user_id')
        st.success('You have been logged out.')

# Add Company Section
if st.session_state.logged_in:
    st.header('Add Company')
    company_name = st.text_input('Company Name')
    company_address = st.text_input('Company Address')
    company_phone = st.text_input('Company Phone')

    if st.button('Submit Company'):
        add_company(company_name, company_address, company_phone)
        st.success('Company added successfully!')
else:
    st.warning('You need to log in to access this feature.')

# Add User Section
if st.session_state.logged_in:
    st.header('Add User')
    user_name = st.text_input('User Name')
    user_email = st.text_input('User Email')
    user_role = st.selectbox('User Role', ['admin', 'staff'])

    if st.button('Submit User'):
        add_user(user_name, user_email, user_role)
        st.success('User added successfully!')
else:
    st.warning('You need to log in to access this feature.')

# Add Drug Section
if st.session_state.logged_in:
    st.header('Add Drug')
    drug_name = st.text_input('Drug Name')
    drug_type = st.text_input('Type')
    drug_barcode = st.text_input('Barcode')
    drug_dose = st.text_input('Dose')
    drug_code = st.text_input('Code')
    drug_cost_price = st.number_input('Cost Price', value=0.0, step=0.01)
    drug_selling_price = st.number_input('Selling Price', value=0.0, step=0.01)
    drug_expiry = st.text_input('Expiry')
    drug_company_name = st.text_input('Drug Company Name')
    drug_production_date = st.date_input('Production Date')
    drug_expiration_date = st.date_input('Expiration Date')
    drug_place = st.text_input('Place')
    drug_quantity = st.number_input('Quantity', value=0)

    if st.button('Submit Drug'):
        add_drug(drug_name, drug_type, drug_barcode, drug_dose, drug_code, drug_cost_price, drug_selling_price, drug_expiry, drug_company_name, drug_production_date, drug_expiration_date, drug_place, drug_quantity)
        st.success('Drug added successfully!')
else:
    st.warning('You need to log in to access this feature.')

# View Sales History Section
if st.session_state.logged_in:
    st.header('View Sales History')
    barcode = st.text_input('Enter Barcode to View Sales History')

    if st.button('View Sales History'):
        sales_history = view_sales_history(barcode)
        if sales_history:
            st.write('Sales History:')
            st.write(sales_history)
        else:
            st.warning('No sales history found for the given barcode.')
else:
    st.warning('You need to log in to access this feature.')

# View Drug and Company Info Section
if st.session_state.logged_in:
    st.header('View Drug and Company Info')
    if st.button('View Info'):
        info = get_drug_company_info()
        if info:
            st.write('Drug and Company Info:')
            st.write(info)
        else:
            st.warning('No information found.')
else:
    st.warning('You need to log in to access this feature.')

# View Expiring Drugs Section
if st.session_state.logged_in:
    st.header('View Expiring Drugs')
    if st.button('View Expiring Drugs'):
        expiring_drugs = get_expiring_drugs()
        if expiring_drugs:
            st.write('Expiring Drugs:')
            st.write(expiring_drugs)
        else:
            st.warning('No expiring drugs found.')
else:
    st.warning('You need to log in to access this feature.')

# View Total Sales Section
if st.session_state.logged_in:
    st.header('View Total Sales')
    if st.button('View Total Sales'):
        total_sales = get_total_sales()
        if total_sales:
            st.write('Total Sales:')
            st.write(total_sales)
        else:
            st.warning('No sales found.')
else:
    st.warning('You need to log in to access this feature.')

# Close the connection
cursor.close()
conn.close()
