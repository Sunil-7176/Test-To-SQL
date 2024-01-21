from dotenv import load_dotenv
load_dotenv() #load all the env variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load Gemini midel and provide sql query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro') #Loading Gemini pro model
    response = model.generate_content([prompt[0],question]) #We can give multiple prompts, since it is in list and we have only 1 prompt we use prompt[0]
    return response.text

#To retrieve query from SQL DB
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)

    return rows

#Define the prompt
prompt = [""" 
You are an expert in converting English questions to SQL query ! The SQl Database has the name STUDENT and has the following columns
          - NAMW, CLASS, SECTION and MArks \n\n Example-1 -How many entries of records are present?, the SQL command will be something 
          like this SELECT COUNT(*) FROM STUDENT ; \n Example-2 - Tell me all the students in Data Science class?, the SQL command 
          will be like this SELECT * FROM STUDENT where CLASS='DS' ;
          also the sql code should not have ```in beginning or end and sql word in the output 

"""
          ]

##StreamLit APP

st.set_page_config(page_title="Retrieve SQL QUery")
st.header("Retrieve SQL Data through GEMINI")

question = st.text_input("Input:", key='input')

submit = st.button("Ask the Question")

#Button clicked
if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    data = read_sql_query(response,"student.db")
    st.subheader("the Response is")
    for row in data:
        print(row)
        st.header(row)



