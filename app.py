import streamlit as st

def find_largest_num(a,b,c):
  return max(a,b,c)

def main():
  st.title("Find the Largest Number")

  st.write("Enter three numbers:")
  a = st.number_input("Number 1")
  b = st.number_input("Number 2")
  c = st.number_input("Number 3")

  if st.button("Find Largest"):
    largest = find_largest_num(a,b,c)
    st.write(f"The Largest number is: {largest}")

if __ name __ == '__ main __':
  main()
