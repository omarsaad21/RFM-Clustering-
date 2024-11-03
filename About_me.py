import streamlit as st 

from forms.contact import contact_form


st.experimental_dialog('Contact Me')
def show_contact_form():
    contact_form()

# ---- Hero section ----
col1,col2 = st.columns(2,gap = 'small', vertical_alignment ='center')
with col1:
    st.image('D:\CDSP\Final_Project\Streamlit multipage App\Assets\IMG-20220824-WA0012.jpg',width=230)
with col2:
    st.title('Omar Saad',anchor=False)
    st.write(
        'I am Business analytics student seeking career in Data Science industry. I am eager to utilize my skills and passion to support the mission of the company. Technologically adept, offering latest academic knowledge with hands on office technology programs, advanced computer skills & analytical skills. Bringing forward a positive attitude with high willingness and motivation to learn and practice new Skills.'
             )
    if st.button ('Contact me'):
        show_contact_form()

st.write("\n")
st.subheader('Experience * Qualifications',anchor=False)
st.write(
    """
    - 2 Weeks  Hands on experinece Finance Internship in Petronefertiti Co. 2023
    - 6 months Digital Transformation Internship in attijirwafa Bank 2024 - Present
    - professional athlete with over 11 medals claimed in (Swimming & Gymnastics) 
    """
)       

st.write('\n')
st.subheader('Tehnical Skills',anchor=False)
st.write(
    """
    - Programming (python:(web scraping, Pandas, numpy, Sickit learn, Seaborn, Matplotlib), MySql)
    - Ms Office
    - PowerBi
    - Ideas system (oracle sub_system)
    - AP Accounts payable 
    """
)

st.write('\n')
st.subheader('Languages',anchor=False)
st.write(
    """
    - Arabic (mother tongue)
    - English C1
    - French (Delf B1)
    """
)

st.write('\n')
st.subheader('Soft skills',anchor=False)
st.write(
    """
    - Presentation
    - Negotiation skills
    - Innovative
    - Teamwork
    - Attention to detail
    - Complex problem solver
    """
)