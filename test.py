import streamlit as st
import pandas as pd
import sqlite3 as sq
conn=sq.connect('test.db')
cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT NOT NULL, position TEXT, salary REAL)')
z=st.text_input("Name")
y=st.text_input("position")
l=st.text_input("salary")
employees = (z, y, l)  
if st.button("submit"):
    cur.execute('INSERT INTO test (name, position, salary) VALUES (?, ?,?)', employees)
    conn.commit()

if st.button("show"):
    cur.execute('SELECT * from test')
    st.table(cur.fetchall())
cur.close()
