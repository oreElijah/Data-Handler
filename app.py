import streamlit as st
import pandas as pd

st.title("Data Handler")
file_upload = st.file_uploader("Choose a csv file", type='csv')
n=file_upload
if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.subheader("Data preview")
    st.write(df.head())
    st.subheader("Filter Data")   
    columns = df.columns.tolist()
    selected_column =st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox("Select values", unique_values)

    filtered_df = df[df[selected_column]==selected_values]
    st.write(filtered_df)
    st.subheader("Data management") 
    null = df.isnull()
    # new_df = pd.read_csv(file_upload)

    rows = st.text_input("How many rows do you want to see in your dataset?")
    if rows:
        st.write("To check for null values")
        null =  st.write(df.head(int(rows)))
    else:
        st.write(df.head(10))

    arr = ['Drop null values', 'Fill null values with mode', "None of the above"]
    null_val = st.text_input("Are there null values present ?")
    null_val = null_val.lower()
    if null_val == "yes":
        func = st.selectbox("Select what you would like to do with the null values", arr)
        if func== arr[0]:
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode("utf-8")
            new_df = df.dropna()
            csv = convert_df(new_df)
            st.subheader("New preprocessed data")
            st.write(new_df)
            st.download_button(label="Download", data=csv, file_name='NEW_CSV_FILE.csv')
            st.subheader("Plot Data")
            x_column = st.selectbox("Select X-axis column",columns)
            y_column = st.selectbox("Select Y-axis column",columns)
            if st.button("Generate Plot"):
                st.line_chart(new_df.set_index(x_column)[y_column])            
            st.subheader('Rate us')
            sentiment_mapping = ["one", "two", "three", "four", "five"]
            selected = st.feedback("stars")
            
            if selected is not None:
                st.markdown(f"Thanks for the rating")
                ratings = []
        elif func==arr[1]:
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode("utf-8")
            columns = df.columns.tolist()
            mode_of_i = df.mode().iloc[0]
            df=df.fillna(mode_of_i)
              
            csv = convert_df(df)
            st.subheader("New preprocessed data")
            st.write(df)
            st.download_button(label="Download", data=csv, file_name='NEW_CSV_FILE.csv')
            st.subheader("Plot Data")
            x_column = st.selectbox("Select X-axis column",columns)
            y_column = st.selectbox("Select Y-axis column",columns)
            if st.button("Generate Plot"):
                st.line_chart(df.set_index(x_column)[y_column])
            st.subheader('Rate us')
            sentiment_mapping = ["one", "two", "three", "four", "five"]
            selected = st.feedback("stars")
            
            if selected is not None:
                st.markdown(f"Thanks for the rating")
                ratings = []
        else:
            st.write("No action taken")
            st.subheader('Rate us')
            sentiment_mapping = ["one", "two", "three", "four", "five"]
            selected = st.feedback("stars")
            
            if selected is not None:
                st.markdown(f"Thanks for the rating")
                ratings = []
                for i in sentiment_mapping:
                    ratings.append(sentiment_mapping[selected])
                    st.write("This are our ratings")
                    st.write(ratings)
    elif null_val == 'no':
            st.header("No null value present")
            st.subheader('Rate us')
            sentiment_mapping = ["one", "two", "three", "four", "five"]
            selected = st.feedback("stars")
            
            if selected is not None:
                st.markdown(f"Thanks for the rating")
                ratings = []
                
    else:
        st.write("Answer with Yes or No")
else:
   st.write("Waiting on file upload........")