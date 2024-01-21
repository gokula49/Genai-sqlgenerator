import streamlit as st;
import google.generativeai as gemini;


gemini.configure(api_key="your key")
model = gemini.GenerativeModel("gemini-pro")

def main():
    st.set_page_config(page_title="Generative AI Project" , page_icon=":robot:")
    st.markdown('''
                <h1 style="text-align: center;">Generative AI Project</h1>

                <h2 style="text-align: center;">Google Gemini -  Streamlet</h2>
               
                <h3 style="text-align: center;" > Generate SQL from normal text </h3>
                


                ''', unsafe_allow_html=True)
    
    textInput = st.text_input("Enter the text for which you want query")

    submit = st.button("Generate Query with Gen AI")

    
    if(submit) :
        with st.spinner("Generating Query") :
            template = """
               create a sql query for below snipet , just in response give query without explanation
               ```
               {textInput}
               ```
               i just want only query with no explanation
            """        

        formatted_template = template.format(textInput=textInput)
        query = model.generate_content(formatted_template)
        st.success(query.text)

main()