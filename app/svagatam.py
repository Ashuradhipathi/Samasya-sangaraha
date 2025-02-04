import streamlit as st
from rag import insert_problem


# Home Page
def main():
    st.title("Samsya-sangraha!")

    # Authors message
    st.markdown(
        "_I have always been in Tutorial Hell and when I finally wanted to build something for actual people, I had no ideas. This website is the outcome of my problem, let yours join in the never ending list inspiring those in love with solutions to **Build**_"
    )
    st.markdown("----")

    # Directions
    st.markdown(
        "The contents below explains the website! You can drop your ideas/problems for our fellow devs(I would prefer ideas for ml domain 😉) below."
        ""
    )

    # Columns for pages
    samara, sangraha = st.columns(2)

    samara.image("assets/svagatam_samara.jpg")

    samara.markdown(
        "_Samara_ meaning battle contains a search box that lets you put in a topic such as students, challenged etc and retrieves problems, use cases"
    )

    sangraha.markdown(
        "_Sangraha_ meaning collection conatins all the problems entered through the application depicted as a table."
    )
    sangraha.image("assets/svagatam_sangraha.jpg")

    # Page links
    sangraha.page_link("pages/sangraha.py", label="Catalogue Page", icon="🚨")

    samara.page_link("pages/samara.py", label="Query Page", icon="🔥")
    st.markdown("----")

    # Button to add probelms/ideas
    if st.button("Add ?"):
        add()

    st.markdown("## Thank You!!")


# streamlit function to create dialog box on clicking add
@st.dialog("Cast your vote")
def add():
    st.write("Add Your Problem")
    problem = st.text_input("Tell Us")

    if st.button("Submit"):
        # function to insert problem into mongoDB
        insert_problem(problem)
        st.rerun()


if __name__ == "__main__":
    main()
