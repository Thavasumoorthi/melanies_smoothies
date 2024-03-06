# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
from snowflake.snowpark.context import get_active_session

# # Write directly to the app
# st.title("Example Streamlit App :balloon:")
# st.write(
#     """Replace this example with your own code!
#     **And if you're new to Streamlit,** check
#     out our easy-to-follow guides at
#     [docs.streamlit.io](https://docs.streamlit.io).
#     """
# )

st.title(":cup_with_straw: **Customize your smoothie!** :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)


# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)


# option=st.selectbox(
#     'what is your favorite fruit?',
# ("Banana","Strawberies","Peaches")
# )
# st.write('You selected:', option)



name_on_order = st.text_input('Name on Smoothie', '')
st.write('The name on your smoothie will be', name_on_order)


session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))
st.dataframe(data=my_dataframe, use_container_width=True)

ingredient_list=st.multiselect(
    'Chose up to 5 ingredients:',
    my_dataframe ,
    max_selections=5
)

if ingredient_list:
    # st.write(ingredient_list)
    # st.text(ingredient_list)
    ingredient_string=''

    for fruit_chosen in ingredient_list:
        ingredient_string+=fruit_chosen+' '
    # st.write(ingredient_string)
    
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredient_string + """','"""+name_on_order+"""')"""
    st.write(my_insert_stmt)

    time_to_order=st.button("Submit Order")

    if time_to_order:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")




