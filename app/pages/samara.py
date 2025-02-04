import streamlit as st
from rag import get_query_results


def main():
    # Flags
    query_given = False
    challenges = []

    # Bg image
    bg_image = st.container()
    bg_image.image("https://github.com/Ashuradhipathi/Samasya-sangraha/blob/main/app/assets/samara.png")

    # Query
    query = st.text_input("What do you want to solve?")

    if st.button("Query"):
        query_given = True

    

    if query_given:

        with st.spinner("Please wait..."):
            challenges = get_query_results(query)


        for challenge in challenges:
            st.markdown(f" ### {challenge['text']}")


if __name__ == "__main__":
    main()
