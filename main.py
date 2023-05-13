import streamlit as st
import pandas as pd
st.set_page_config(page_title='Wealth Pilot',page_icon="logo.png",layout="wide",initial_sidebar_state='expanded')
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import pickle
from customer_segregation import *
from loan_inputs import *
import sklearn 
import altair
import bz2file as bz2


data = bz2.BZ2File('model.pbz2', 'rb')
rf_classifier = pickle.load(data)

clf_pickle = open('clf_model.pkl','rb')
clf_classifier = pickle.load(clf_pickle)

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.sidebar.image('Compunnel-Digital-Logo.png', width=125)
st.sidebar.title('''**Wealth Pilot**''')
st.markdown("""<style>[data-testid="stSidebar"][aria-expanded="true"] 
> div:first-child {width: 450px;}[data-testid="stSidebar"][aria-expanded="false"] 
> div:first-child {width: 450px;margin-left: -400px;}</style>""",
unsafe_allow_html=True)


def customer_classifier(children,age,occupation,partner_occupation,home,family_income,Average_Credit_Card_Transaction,Term_Deposit,Average_ac_Balance,Portfolio_Balance,investments,loan,Insurance):
     cat_children = children_encoding(children)
     cat_age= age_encoding(age)
     cat_occupation=occupation_encoding(occupation)
     cat_partner_occupation= partner_occupation_encoding(partner_occupation)
     cat_home=home_encoding(home)
     cat_family_income= family_encoding_encoding(family_income)
     
     
     result = rf_classifier.predict([[cat_children,cat_age,cat_occupation,cat_partner_occupation,cat_home,cat_family_income,Average_Credit_Card_Transaction,Term_Deposit,Average_ac_Balance,Portfolio_Balance,investments,loan,Insurance]])
     return result
    #  if result == 1:
    #      return " The customer has a High Net Worth"
    #  else:
    #      return "The Customer has Low Net Worth "

def loan_status_pred(gender,marriage_status,qualification,dependents,self_employed,income,loan_amount,loan_tenure,credit_history,area):
    gender = check_gender(gender)
    marriage_status = check_marriage_status(marriage_status)
    qualification = check_qualification(qualification)
    dependents = check_dependents(dependents)
    self_employed = check_self_employed(self_employed)
    credit_history= check_debt(credit_history)
    area = check_area(area)

    result = clf_classifier.predict([[gender,marriage_status,qualification,dependents,self_employed,loan_amount,loan_tenure,credit_history,area,income]])
    return result



def main():

    with st.sidebar:
        selection = option_menu("Select the Application",["Customer Segmentation","Loan Approval"],
                                icons=['person-fill','cash-coin'],
                                # menu_icon=[]
                                styles={
                                "container": {"padding": "5!important", "background-color": "#fafafa"},
                                "icon": {"color": "black", "font-size": "20px"}, 
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "#ff6347"}
                                }

                                )
        

    if selection == "Customer Segmentation":
        option = option_menu(
        menu_title="",
        options=["Prediction","Vizualization"],
        icons=["toggles2","clipboard-data"],
        orientation="horizontal",
        styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "20px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#ff6347"}
                    }
        )

        if option == "Prediction":

            c1, c2 = st.columns(2)
            with c1:
                age = st.selectbox('Please specify the Age Category of the candidate',('18-21','22-25','26-30','31-35','36-40','41-45', '45-50','51-55','55-60', '61-65', '65-70', '71 and above', 'Unknown' ),key=1)

                children = st.selectbox('Please specify the number of children the candidate have',('0', '1', '2','3','4 or more than 4'),key=3)
 
                home = st.selectbox('Please specify the ownership of the house the candidate lives in',('Own Home','Rent Privately','Rent from Council/HA','Live in Parental Hom',
                    'Unclassified'),key=5)
                Average_Credit_Card_Transaction = st.number_input('Enter the average credit card transaction amount done by candidate',min_value=0,step=500,key=7)
                Term_Deposit = st.number_input('Enter the term deposit amount by the candidate',min_value=0,step=500,key=9) 
                investments = st.number_input("Enter the total investments amount(if any) by the candidate",min_value=0,step=500,key=13)


            with c2:
                occupation = st.selectbox('Please specify the Profession of the candidate',('Professional','Secretarial/Admin','Manual Worker','Housewife','Retired',
                                    'Other','Unknown','Business Manager','Student'),key=2) 
                partner_occupation = st.selectbox('Please specify the Profession of parner of the candidate(if applicable)',('Professional','Secretarial/Admin','Manual Worker','Housewife','Retired',
                                    'Other','NA','Business Manager','Student'),key=4)

                family_income = st.selectbox("Please select the family income category of the candidate",('>=35,000', '<22,500, >=20,000', '<25,000, >=22,500' ,'<30,000, >=27,500',
                                        '<20,000, >=17,500', '<27,500, >=25,000', '< 4,000', '<15,000, >=12,500',
                                        '<17,500, >=15,000', '< 8,000, >= 4,000', '<12,500, >=10,000', '<10,000, >= 8,000', 'Unknown'),key=6)
                
                Average_ac_Balance  = st.number_input("Enter the Average bank balance maintained by the candidate",min_value=0,step=1000,key=8)

                Insurance = st.number_input('Enter the Total Insuarance premium paid by the user',min_value=0,step=500,key=10)
                loan = st.number_input("Enter the total loan amount taken by (if any) by the candidate",min_value=0,step=1000,key=11) 

                      
            Portfolio_Balance = st.number_input("Enter the Portfolio balance of the candidate",min_value=0,step = 1000,key=12)

            col1, col2, col3,col4,col5 = st.columns(5)
            if col3.button('Check'):
                result = customer_classifier(children,age,occupation,partner_occupation,home,family_income,Average_Credit_Card_Transaction,Term_Deposit,Average_ac_Balance,Portfolio_Balance,investments,loan,Insurance)
                if result==1:
                    st.success('The Customer has high net worth')
                else:
                    st.error('The customer has low net worth')

        if option =='Vizualization':
            st.info('PowerBI Dashboard')
            st.markdown('<iframe title="Report Section" width="674" height="650" src="https://app.powerbi.com/view?r=eyJrIjoiZjRkM2Y1MDUtNGIyOC00ZGIyLTk5ODMtNTMxY2QzYzIxNjJlIiwidCI6ImE2MTdlYzYwLTBhYjMtNDBiZS05MjhmLWJmMzY1MzA4NDkxYSIsImMiOjF9" frameborder="0" allowFullScreen="true" ></iframe>',unsafe_allow_html=True)
            #st.markdown('<iframe title="Retail Dashboard 2.0" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=f2c5ba44-d7cc-41ee-9e9d-d37468f956ac&autoAuth=true&ctid=a617ec60-0ab3-40be-928f-bf365308491a" frameborder="0" allowFullScreen="true"></iframe>',unsafe_allow_html=True)


    if selection == "Loan Approval":
        option = option_menu(
        menu_title="",
        options=["Prediction","Vizualization"],
        icons=["toggles2","clipboard-data"],
        orientation="horizontal",
        styles={
                "container": {"padding": "5!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "20px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#ff6347"}
                    }
        )

        if option == "Prediction":
            
            gender = st.selectbox('Please specify the Gender of the applicant',('Male','Female'),key=1)
            c1, c2 = st.columns(2)
            with c1:
                marriage_status = st.radio('Is the applicant married',('Yes','No'),key=2) 
                qualification = st.radio("Select the education level of the applicant",('Graduate','Not Graduate'),key=3)
 
            with c2:

                dependents = st.radio('Are their any dependents on the applicant',('Yes','No'),key=4)
                self_employed = st.radio('Is the applicant self employed',('Yes','No'),key=5)

            income = st.number_input("Enter the salary of the applicant",step=5000,min_value=0,key=6)
            # co_applicant_income = st.number_input("Enter the salary of the co-applicant(if any)",key=6)

            c3,c4 = st.columns(2)

            with c3:
                loan_amount = st.number_input('Enter the loan amount',key=7)
            with c4: 
                loan_tenure = st.slider("Enter the loan tenure(in months)",6,600, step= 6)

            credit_history = st.radio("Is there any debt on the applicant",('Yes','No'))

            area = st.radio('Select the area type in which applicant resides',('Urban','Rural'))

            
            col1, col2, col3,col4,col5 = st.columns(5)
            if col3.button('Check'):
                result = loan_status_pred(gender,marriage_status,qualification,dependents,self_employed,income,loan_amount,loan_tenure,credit_history,area)
                if result=='Y':
                    st.success("The Loan is approved")
                else:
                    st.error(" The loan is not approved")


         



if __name__ == '__main__':
    main()


