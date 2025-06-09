import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.grammar_utils import check_grammar
import streamlit as st

st.set_page_config(page_title="GrammarScope", page_icon="📝")
st.title("GrammarScope: Grammar Checker")

user_input = st.text_area("Enter a sentence or paragraph:")

if st.button("Check Grammar"):
    if user_input.strip():
        results = check_grammar(user_input)

        if not results:
            st.success("No grammatical errors found!")
        else:
            st.subheader("Errors Found:")
            for i, err in enumerate(results, start=1):
                st.markdown(f"""
                **{i}. Error**: `{err['error']}`  
                **Suggestion**: {', '.join(err['suggestion']) if err['suggestion'] else 'None'}  
                **Explanation**: {err['message']}  
                **Rule ID**: `{err['rule']}`  
                """)
    else:
        st.warning("Please enter some text to check.")
