import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

# def main():
st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
    # selected_box = st.sidebar.selectbox(
    # 'Choose one of the following',
    # ('Welcome', 'Image Processing', 'Video', 'Face Detection', 'Feature Detection', 'Object Detection') )
    #
    #
    # if selected_box == 'Welcome':
    #     # welcome()
    #     pass
    # if selected_box == 'Image Processing':
    #     # photo()
    #     pass
    # if selected_box == 'Video':
    #     # video()
    #     pass
    # if selected_box == 'Face Detection':
    #     # face_detection()
    #     pass
    # if selected_box == 'Feature Detection':
    #     # feature_detection()
    #     pass
    # if selected_box == 'Object Detection':
    #     # object_detection()
    #     pass
# if __name__ == "__main__":
#     main()