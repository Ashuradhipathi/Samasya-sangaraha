import streamlit as st
import pandas as pd
from mongo import retrieve_all


def main():
    # Bg image
    st.image("https://github.com/Ashuradhipathi/Samasya-sangraha/blob/main/app/assets/Sangraha_bg.jpg", use_container_width=True)

    records = []

    # Retrieveing all values and converting to pandas data frame
    if st.button("List All problems"):
        with st.spinner("Please wait..."):
            records = pd.DataFrame(retrieve_all())

    if not isinstance(records, list):
        st.dataframe(records.text, width=700, hide_index=True)

    else:
        pass


if __name__ == "__main__":
    main()
