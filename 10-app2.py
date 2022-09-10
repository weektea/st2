import streamlit as st


# title
st.title("My favorites")

# 3 columns that display your favorite songs from youtube
colu1, colu2, colu3 = st.columns(3)

with colu1:
    st.write("My first favorite song")
    st.video("https://www.youtube.com/watch?v=jBVsgYJKkyE")
    
with colu2:
    st.write("My second favorite song")
    st.video("https://www.youtube.com/watch?v=3jfI-z__GY0")
    
with colu3:
    st.write("My third favorite song")
    st.video("https://www.youtube.com/watch?v=vvmUvtYsarA")    

# 3 columns that display your photo of favorite foods.
col1, col2, col3 = st.columns(3)

with col1:
    st.write("My first favorite food")
    st.image("https://img.freepik.com/free-photo/top-view-pepperoni-pizza-with-mushroom-sausages-bell-pepper-olive-corn-black-wooden_141793-2158.jpg?w=2000", caption="This image is from google search")  
    
with col2:
    st.write("My second favorite food")
    st.image("https://image.shutterstock.com/z/stock-photo-assorted-sushi-nigiri-and-maki-big-set-on-slate-a-variety-of-japanese-sushi-with-tuna-crab-1937661397.jpg", caption="This image is from google search")  
    
with col3:
    st.write("My third favorite food")
    st.image("https://i.ytimg.com/vi/dh6GgbgQ5j0/maxresdefault.jpg", caption="This image is from google search")  

# balloon or snowflake
st.balloons()


# caption by your name
st.caption("Developed by XingYee")