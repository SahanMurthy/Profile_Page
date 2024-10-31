import streamlit as st
def main():
    st.header("Education")

    st.subheader("Electronics and Communication Engineering")
    st.write("PES College of Engineering, Mandya")
    st.write("December 2021 - June 2024 (Expected)")

    st.subheader("Electronics and Communication Engineering")
    st.write("Vidyavardhaka Polytechnic, Mysuru")
    st.write("August 2018 - November 2021")

    st.subheader("SSLC")
    st.write("Sri Sadguru Vidya Mandira, Basarikatte, Chikkamagalore District")
    st.write("March 2016")

    st.header("Courses")
    courses = [
        "Python from Besant Technologies",
        "Embedded System Design with Arm - NPTEL Online Certifications (January 2024 - March 2024)",
        "Artificial Intelligence from Mach It"
    ]
    for course in courses:
        st.write(f"- {course}")

    st.header("Certifications")
    st.write("- Embedded System Design with Arm - NPTEL Online Certification")
    st.write("- For soft copy of Certificates")
    st.write("[For Soft Copy link](https://drive.google.com/drive/folders/15uoedKnij6kU1kHVkLsjCr48_uoqNsF9?usp=drive_link)")

if __name__ == "__main__":
    main()