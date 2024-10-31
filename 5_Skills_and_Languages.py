import streamlit as st
def main():
    st.header("Skills")
    skills = [
        "Python",
        "Arduino IDE (Embedded C Programming)",
        "PCB Designing",
        "C Programming",
        "Fast Learner"
    ]

    for skill in skills:
        st.write(f"- {skill}")

    st.subheader("Additional Skills")
    additional_skills = [
        "OpenCV",
        "Raspberry Pi",
        "Mentor Graphics Xpedition Enterprise",
        "Artificial Intelligence basics"
    ]

    for skill in additional_skills:
        st.write(f"- {skill}")

    st.header("Languages")
    languages = ["English", "Kannada", "Hindi"]
    st.write(", ".join(languages))

if __name__ == "__main__":
    main()