import streamlit as st

def main():
    st.title("© Simple Calculator")
    st.write("Enter two numbers and choose an operation")


    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter First number", value=0.0)

    with col2:
        num2 = st.number_input("Enter Second number", value=0.0)

    operation = st.selectbox("Choose an Operation", ["Addition (+)", "Subtraction (-)", "Multiplication (x)", "Division (/)"])

    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (x)":
                result = num1 * num2
                symbol = "x"
            else:
                if num2 == 0:
                    st.error("Error: Division by Zero!")
                    return
                result = num1 / num2
                symbol = "/"
                
            st.success(f"{num1} {symbol} {num2} = {result}")

        except Exception as e:
            st.error(f"An error occured: {str(e)}")

if __name__ == "__main__":
    main()


# Build by: AbdulWahid😎

