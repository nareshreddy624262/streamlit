import streamlit as st

st.title("streamlit session  ")                                                                               #title
st.header("now we are going to learn streamlit and its properies  :")                                         #header
st.subheader("streamli is used for deploye machine learinhg algorithams and other things")                    #subheader
st.text("streamlit is python package it used for web servies ")                                               #text
st.markdown("this is markdown")                                                                               #markdown


# colors for streamlit

st.success("this success for green color")                                                                    #success
st.info("this is info for blue color   ")                                                                     #info
st.warning("this warning for red color")                                                                      #WARNING
st.error("this is error")

st.subheader("write  ")
st.write("range(1,10)")
st.write(range(1,10))                                                                  #error

st.write("write code in streamlit  ")
st.subheader('Code')
st.code('x = 10\n'                                      # Code
        'for i in range(x):\n'
        '\tprint(i)')

st.code('x= 10 \n'
        'for i in range(1,10): \n'
        '\tif i==5: \n'
            '   \tprint(hello world)'        )


st.subheader("check box")
male = st.checkbox("male")
female = st.checkbox("female")
others = st.checkbox("others")
if male:
    st.write("you are a male ")
elif female:
    st.write("you ar female ")
else:
    st.write("you are others  ")




st.subheader("radio buttons ")
radio_button = st.radio("gender:",("male","female","others"))
if radio_button == "amle":
    st.write("you are male :")
elif radio_button == "female":
    st.write("you are female :")
elif radio_button == "others" :
    st.write("you are ither gender :")




st.subheader("select box ")
select_box = st.selectbox("data science :",["artificial intellegence","machine learning",
                                "data analytics","data mining","numpy",
                                "pandas","matplotlib","seaboarn","streamlit",
                                "powerbi","ms excel","tabule","deep learning",
                                "natural language process","image processing"])

st.write("you are selected ",select_box)



st.subheader("multi select  box ")

multi_select_box = st.multiselect("data science :",["artificial intellegence","machine learning",
                                "data analytics","data mining","numpy",
                                "pandas","matplotlib","seaboarn","streamlit",
                                "powerbi","ms excel","tabule","deep learning",
                                "natural language process","image processing"])


st.subheader("button")

button = st.button("click me ")
if button:
    st.write("thanks for click me :")

st.subheader("slider")
vol = st.slider("select the valume ",0,100,step = 1)
st.write("vol is",vol)


st.subheader("text input :")
name = st.text_input("enter you name")
branch = st.text_input("enter your class")
if name:
    st.write("your name is :",name)


st.subheader("text area ")
st.text_area("enter your text here :")


st.subheader("int input ")
st.number_input("'enter your age from 18 to 100",18,100)


st.subheader("input date ")
st.date_input("enter your date")

st.subheader("input time ")
st.time_input("enter your time")
