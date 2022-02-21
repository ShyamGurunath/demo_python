import streamlit as st


def get_userinputs():

    name = st.text_input("Name")

    if name.startswith("S"):
        st.write("Hey, Sir %s" % name)
    else:
        st.write("Hey, %s" % name)


def married_or_unnmarried():
    martial_staus = st.checkbox("Are you married?")
    if st.button("Click here"):
        if martial_staus == True:
            st.write("Life down")
        else:
            st.write("Life up")
            st.balloons()
            # show ironman image
            st.image("https://media.giphy.com/media/3o7btLwXy8Y9XxXzKU/giphy.gif")


if __name__ == "__main__":

    get_userinputs()
    married_or_unnmarried()
