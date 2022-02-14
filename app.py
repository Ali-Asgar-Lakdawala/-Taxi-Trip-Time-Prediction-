import pickle
import streamlit as st 
import datetime
from geopy.distance import geodesic 
import numpy as np
import joblib

taxi= open('finalized_model_rfr.sav','rb')
taxi_regressor=joblib.load(taxi)

  

def main ():


    activiteis = ["Home","Contack Us"]
    choice = st.sidebar.selectbox("Select Activity", activiteis)

    if choice == "Home":
        st.title("Wellcome aliens")   
        html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Bike sharing demand prediction.</h4>
                                            </div>
                                            </br>"""

        st.header('Taxi trip time prediction')

        pickup_longitude=st.number_input("pickup_longitude",value =-73.95104218,min_value=-122.0,max_value=-62.0)
        pickup_latitude=st.number_input("pickup_latitude",value =40.78575897,min_value=34.0,max_value=52.0)
        dropoff_longitude=st.number_input("dropoff_longitude",value =-73.96601868,min_value=-122.0,max_value=-62.0)
        dropoff_latitude=st.number_input("dropoff_latitude",value =40.75396729,min_value=34.0,max_value=44.0)
        distance=geodesic((pickup_latitude, pickup_longitude),(dropoff_latitude, dropoff_longitude)).km

        date = st.date_input("Date for demand prediction",datetime.date(2021, 4, 3))

        month=date.month
        pickup_months=['pickup_month_1', 'pickup_month_2','pickup_month_3', 'pickup_month_4', 'pickup_month_5', 'pickup_month_6']
        pickup_month_1= 0
        pickup_month_2= 0
        pickup_month_3= 0
        pickup_month_4= 0
        pickup_month_5= 0
        pickup_month_6= 0

        for month in pickup_months:
            if month[-1]==str(month):
                globals()[month] = 1
            else:
                globals()[month] = 0

        weekday=date.weekday()
        pickup_days=['pickup_day_0','pickup_day_1', 'pickup_day_2', 'pickup_day_3', 'pickup_day_4', 'pickup_day_5', 'pickup_day_6']
        pickup_day_0=0
        pickup_day_1=0
        pickup_day_2=0
        pickup_day_3=0
        pickup_day_4=0
        pickup_day_5=0
        pickup_day_6=0

        for day in pickup_days:
            if day[-1]==str(weekday):
                globals()[day] = 1
            else:
                globals()[day] = 0

        vendor_id=st.selectbox("vendor_id",[1,2],index=1)
        if vendor_id==1:
            vendor_id_1=1
            vendor_id_2=0
        else:
            vendor_id_1=0
            vendor_id_2=1 

        store_and_fwd_flag=st.selectbox("store_and_fwd_flag",['yes','no'],index=1)
        if store_and_fwd_flag=='yes':
            store_and_fwd_flag_Y=1
            store_and_fwd_flag_N=0
        else:
            store_and_fwd_flag_Y=0
            store_and_fwd_flag_N=1


        passenger_count=st.selectbox("passenger_count",[1,2,3,4,5,6],index=1)
        passengers_conts=['passenger_count_1', 'passenger_count_2', 'passenger_count_3',
       'passenger_count_4', 'passenger_count_5', 'passenger_count_6',]
        passenger_count_1=0
        passenger_count_2=0
        passenger_count_3=0
        passenger_count_4=0
        passenger_count_5=0
        passenger_count_6=0
        for num in passengers_conts:
            if num[-1]==str(passenger_count):
                globals()[num] = 1
            else:
                globals()[num] = 0

        pickup_period=st.slider("Hour",value =20,max_value=23,min_value=0)
        if pickup_period in range(6,12):
            pickup_period_Morning=1
            pickup_period_Afternoon=0
            pickup_period_Evening=0
            pickup_period_Night=0
        if pickup_period in range(12,17):
            pickup_period_Morning=0
            pickup_period_Afternoon=1
            pickup_period_Evening=0
            pickup_period_Night=0
        if pickup_period in range(17,24):
            pickup_period_Morning=0
            pickup_period_Afternoon=0
            pickup_period_Evening=1
            pickup_period_Night=0
        else:
            pickup_period_Morning=0
            pickup_period_Afternoon=0
            pickup_period_Evening=0
            pickup_period_Night=1



        result= taxi_regressor.predict([[pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,distance,vendor_id_1,vendor_id_2,passenger_count_1,
                                    passenger_count_2,passenger_count_3,passenger_count_4,passenger_count_5,passenger_count_6,
                                    pickup_day_0,pickup_day_1,pickup_day_2,pickup_day_3,pickup_day_4,pickup_day_5,pickup_day_6,pickup_month_1,pickup_month_2,
                                    pickup_month_3,pickup_month_4,pickup_month_5,pickup_month_6,pickup_period_Afternoon,pickup_period_Evening,pickup_period_Morning,
                                    pickup_period_Night]])
        
        if st.button("Predict count"):
            st.success('The Trip will take {} minutes'.format(round(int(result/60))))

    if choice == "About":
        pass




    elif choice == "Contack Us":
        st.header("Contact Details")
        st.write(""" LinkedIn profile Link""")
        st.write(""" >* [Ali Asgar Lakadwala] (https://www.linkedin.com/in/ali-asgar-lakdawala/)""")
        st.write("""Email Id""")
        st.write(""">* Ali Asgar Lakadwala : aliasgarlakdawala0209@gmail.com""")

if __name__ == '__main__':
    main()