import streamlit as st

def main():
    st.header("Projects")

    st.subheader("Iris Control Robot [Major Project]")
    st.write("""
    - Designed to incorporate Python (OpenCV) and Raspberry Pi technology to precisely emulate the intricate movements of human eyes.
    - This innovative integration allows the robot to effectively navigate in various directions by mirroring the natural eye movements essential for spatial orientation and exploration.
    - Through the utilization of Python and Raspberry Pi, the robot achieves a high level of accuracy and efficiency in these eye movements, enhancing its capabilities.
    """)

    st.subheader("Smart Dustbin [Minor Project]")
    st.write("""
    - Arduino-based project which uses an ultrasonic sensor to open and close the door.
    - Demonstrates practical application of sensor technology and automation in everyday objects.
    """)

    st.header("Publications")
    st.subheader("Iris Control Robot")
    st.write("Paper published on the Project Iris Control Robot in IJMRSET (International Journal of Multidisciplinary Research in Science, Engineering and Technology)")
    st.write("[View Paper](https://drive.google.com/file/d/1Al5FU91jmUA8UW2l-hRbY1VkX5JVTRRR/view?usp=drive_link)")

if __name__ == "__main__":
    main()