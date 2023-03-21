# telco_classification_report

Welcome to the Telco Classification Report. Thank you for taking some time to read this documentation as it may provide some information necessary when 
reading the final report. 

Project Description:
This project encompasses the steps of the Data Science pipeline using the Classification methodology in order to
provide some explanation as to why some customers churn from using Telco services and to develop a model which 
can be used to predict which accounts will churn. This is important because the climate for telecommunications
companies is competitive, and the rate of churn at Teclo has raised concern. This is important for any company 
which provides a service in an industry which is saturated with providers. Finding the aspects by which a company
is failing to satisfy its customers is good for both the copmany and its customers. 

Modules needed to run this report:
1. Your personal env.py file saved into the same directory as all the files contained in this repository.
2. acquire.py
3. prepare.py
4. evaluation.py

Goal: The purpose of this project ultimately is to provide insight, indictators, and a model which will help Telco understand
why some customers are churning and what specfic features about the customer experience with the company may be 
contributing to their desicion to churn. The Data Science methodology used in this project is Classification. 

Planning:
My planning, question development, and exploratory analysis comes from a few realizations developed upon first glance 
to the dataset. Please refer to 'Dashboard 1' =, which can be found in this repository for the report to which I am 
refering. Upon initial exploration, I wanted to know if those who were paying for movie and tv streaming were customers
who had dependents. My assumption was that these customers had families, perhaps with small children. I also assumed 
that these customers who had dependenst would make up the majority of the customers who paid for multiple lines. Both
of these assumptions in mind, I then hypothesized that the customers with dependents would have the larger monthly and
total costs and that this demographic would be less likely to churn. 

The questions that are then formally expored include:
1. What is the the relationship between having dependents and the rate of churn?
2. If those with dependents do not make up the majority of churn, is there a group of people where the churn is greater
than the those who stayed with the company? The answer to this was that senior citizens churn more than not. So the 
question then became is there a relationship between being a senior citizen and churn?
3. Is the mean total charges of those who pay for internet, phone, and streaming services more than those who do not?
4. Do those who pay for internet, phone, and streaming services have greater tenures than those who do not?

Data Dictionary:

 0   customer_id                           7043 non-null   object        unique account number 
 1   gender                                7043 non-null   object        gender of the account holder
 2   senior_citizen                        7043 non-null   int64         binary yes (1) or no (0)
 3   partner                               7043 non-null   int64         binary yes (1) or no (0)
 4   dependents                            7043 non-null   int64         binary yes (1) or no (0) 
 5   tenure                                7043 non-null   int64         binary yes (1) or no (0) 
 6   phone_service                         7043 non-null   int64         binary yes (1) or no (0) 
 7   multiple_lines                        7043 non-null   int64         binary yes (1) or no (0) 
 8   online_security                       7043 non-null   int64         binary yes (1) or no (0) 
 9   online_backup                         7043 non-null   int64         binary yes (1) or no (0) 
 10  device_protection                     7043 non-null   int64         binary yes (1) or no (0) 
 11  tech_support                          7043 non-null   int64         binary yes (1) or no (0) 
 12  streaming_tv                          7043 non-null   int64         binary yes (1) or no (0) 
 13  streaming_movies                      7043 non-null   int64         binary yes (1) or no (0) 
 14  paperless_billing                     7043 non-null   int64         binary yes (1) or no (0) 
 15  monthly_charges                       7043 non-null   float64       average monthly bill (USD)
 16  total_charges                         7043 non-null   float64       total charges over tenure (USD) 
 17  churn                                 7043 non-null   int64         binary yes (1) or no (0) 
 18  contract_type                         7043 non-null   object        (Month-to-month, One year, two year) 
 19  internet_service_type                 7043 non-null   object        (None, DSL, Fiber optic)
 20  payment_type                          7043 non-null   object        (Electronic check, Mailed check, Bank               transfer, Credit card)
 21  churn_month                           7043 non-null   object        datetime of when the customer churned 
 22  signup_date                           7043 non-null   datetime64[ns]datetime of when the customer signed
 23  gender_Male                           7043 non-null   uint8          hot-code 
 24  contract_type_One year                7043 non-null   uint8          hot-code
 25  contract_type_Two year                7043 non-null   uint8          hot-code
 26  internet_service_type_Fiber optic     7043 non-null   uint8          hot-code
 27  internet_service_type_None            7043 non-null   uint8          hot-code
 28  payment_type_Credit card (automatic)  7043 non-null   uint8          hot-code
 29  payment_type_Electronic check         7043 non-null   uint8          hot-code
 30  payment_type_Mailed check             7043 non-null   uint8          hot-code
 31  time_with_telco                       1869 non-null   timedelta64[ns]days difference between churn date and signup date (only applies to customers who have churned)
