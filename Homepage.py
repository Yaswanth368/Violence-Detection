import streamlit as st
import base64
from pathlib import Path

def add_bg_from_local(image_file):
    """
    Function to read and encode the background image
    """
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{data}");
        background-size: cover;
        background-repeat: no-repeat;
    }}
    </style>
    '''
def create_sidebar():
    """
    Create a sidebar with navigation and project information
    """
    with st.sidebar:
        
                
        # Navigation buttons with custom styling
        st.markdown("""
            <style>
            .sidebar-button {
                background-color: #1E88E5;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin: 5px 0;
                text-align: center;
                cursor: pointer;
            }
            .sidebar-button:hover {
                background-color: #1565C0;
            }
            </style>
        """, unsafe_allow_html=True)
        
        
        # Project Information
        st.markdown("### ℹ️ Project Info")
        with st.expander("About"):
            st.write("""
                This system uses advanced AI and computer vision 
                techniques to detect crowds and violent activities 
                in real-time video streams.
            """)
            
        with st.expander("Features"):
            st.write("""
                - Real-time video processing
                - Crowd density estimation
                - Violence detection alerts
                - Historical data analysis
                - Export capabilities
            """)
            
        with st.expander("Help"):
            st.write("""
                **Quick Start:**
                1. Select detection mode
                2. Upload video or connect to camera
                3. View real-time analysis
                
                For support, contact: support@example.com
            """)
        
        st.divider()
        
        # System Status
        st.markdown("### 🔄 System Status")
        status = st.empty()  # Placeholder for dynamic status updates
        status.success("System Online")
        
        # Optional: Add system metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("CPU", "40%")
        with col2:
            st.metric("Memory", "60%")
        
        # Footer
        st.divider()
        st.markdown("""
            <div style='text-align: center; color: #666;'>
                <small>Version 1.0.0</small>
            </div>
        """, unsafe_allow_html=True)
def main():
    # Set page configuration
    st.set_page_config(
        page_title="Crowd and Violence Detection System",
        page_icon="👁️",
        layout="wide"
    )
    create_sidebar()
    # Add custom CSS for better styling
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            padding: 20px;
            color: #FFFFFF;
            background-color: rgba(0, 0, 0, 0.7);
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .feature-card {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 18px;
            border-radius: 10px;
            margin: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .feature-header {
            color: #FFFFFF;
            text-align: center;
            margin-bottom: 15px;
        }
        .feature-text {
            color: #FFFFFF;
            text-align: justify;
        }
        </style>
    """, unsafe_allow_html=True)

    # Try to set background image if available
    try:
        bg_image = Path("")  # Update path as needed
        if bg_image.exists():
            st.markdown(add_bg_from_local(str(bg_image)), unsafe_allow_html=True)
    except Exception:
        pass  # Continue without background image if not available

    # Main Header
    st.markdown("""
        <div class="main-header">
            <h1>Welcome to Crowd and Violence Detection System</h1>
            <p>An advanced AI-powered surveillance solution for public safety</p>
        </div>
    """, unsafe_allow_html=True)

    # Create three columns for features
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div class="feature-card">
                <h2 class="feature-header">🎯 Crowd Detection</h2>
                <p class="feature-text">
                    Our advanced crowd detection system uses state-of-the-art computer vision 
                    algorithms to accurately monitor and analyze crowd dynamics in real-time. 
                    Perfect for managing public spaces, events, and ensuring safety protocols.
                </p>
                <ul class="feature-text">
                    <li>Real-time crowd density estimation</li>
                    <li>Occupancy monitoring</li>
                    <li>Crowd flow analysis</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Go to Crowd Detection", key="crowd_btn",use_container_width=True):
            st.switch_page("Pages/Crowd_Detection.py")

    with col2:
        st.markdown("""
            <div class="feature-card">
                <h2 class="feature-header">⚠️ Violence Detection</h2>
                <p class="feature-text">
                    Our violence detection module employs sophisticated AI models to identify 
                    and alert potential violent situations in real-time. Essential for 
                    security personnel and law enforcement agencies.
                </p>
                <ul class="feature-text">
                    <li>Real-time violence detection</li>
                    <li>Instant alerting system</li>
                    <li>Video analysis capabilities</li>
                    <p>.</p>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Go to Violence Detection", key="violence_btn",use_container_width=True):
            st.switch_page("Pages/Violence_Detection.py")

    # Footer
    st.markdown("""
        <div style="position: fixed; bottom: 0; left: 0; right: 0; background-color: rgba(0, 0, 0, 0.7); padding: 10px; text-align: center; color: white;">
            <p>© 2025 Crowd and Violence Detection System. All rights reserved.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()