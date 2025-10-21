import streamlit as st
import plotly.express as px 
from backend import get_data


st.title("wheater forecast for next days")

place =st.text_input("place:")

days=st.slider("Forecast Days",min_value=1,max_value=5,
               help="select the number of days for forecast")
option=st.selectbox("select data view",("Temperature","sky"))

st.subheader(f"{option} for the next {days} in {place}")



if place:
    try:
        filter_data = get_data(place,days)

        if option =="Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filter_data]
            dates = [dict["dt_txt"] for dict in filter_data]

            figure = px.line(x=dates,y=temperatures, labels={"x":"Date", "y":"Temperature (c)"})
            st.plotly_chart(figure)

        if option == "sky":
            images = {"Clear":"image/clear.png","Clouds":"image/cloud.png",
                    "Rain":"image/rain.png","Snow": "image/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths,width=115)
    except KeyError:
        st.write("you had enterd wrong place")






