import streamlit as st
from patterns import PatternGenerator
from utils import format_pattern_name

def main():
    st.title("Pattern Generator")
    size = st.number_input("Enter size of pattern:", min_value=1, value=5, step=1)
    generator = PatternGenerator(size)
    patterns = generator.get_patterns()
    
    pattern_choice = st.selectbox("Choose a pattern:", list(patterns.keys()))
    
    if st.button("Generate Pattern"):
        st.code(patterns[pattern_choice](), language="plaintext")

if __name__ == "__main__":
    main()