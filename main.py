import os
import streamlit as st
import cv2
import time
import requests
import numpy as np
from ai_agent import ask_agent
from text_to_speech import text_to_speech_with_elevenlabs
from speech_to_text import record_audio, transcribe_with_groq
import hashlib

# Page config
st.set_page_config(
    page_title="Dora - AI Assistant",
    page_icon="👧🏼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# IP Webcam URL
IP_WEBCAM_URL = "http://10.5.124.71:8080/shot.jpg"

def get_ip_camera_frame():
    """Fetch frame from IP webcam"""
    try:
        response = requests.get(IP_WEBCAM_URL, timeout=3)
        if response.status_code == 200:
            img_arr = np.array(bytearray(response.content), dtype=np.uint8)
            frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            if frame is not None:
                return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), None
            return None, "Failed to decode image"
        return None, f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        return None, "Connection timeout"
    except Exception as e:
        return None, str(e)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'camera_active' not in st.session_state:
    st.session_state.camera_active = True
if 'listening_active' not in st.session_state:
    st.session_state.listening_active = False
if 'last_audio_hash' not in st.session_state:
    st.session_state.last_audio_hash = None
if 'processing' not in st.session_state:
    st.session_state.processing = False
if 'last_frame' not in st.session_state:
    st.session_state.last_frame = None
if 'camera_error_count' not in st.session_state:
    st.session_state.camera_error_count = 0

AUDIO_FILEPATH = "audio_question.mp3"
FINAL_AUDIO_FILEPATH = "final.mp3"

# Title
st.markdown(
    "<h1 style='color: orange; text-align: center;'>👧🏼 Dora – Your Personal AI Assistant</h1>",
    unsafe_allow_html=True
)

# Create two columns
col1, col2 = st.columns(2)

# Left column - Webcam
with col1:
    st.markdown("## 📹 Live Webcam Feed")
    
    # Camera controls
    camera_col1, camera_col2 = st.columns(2)
    with camera_col1:
        if st.button("▶️ Start Camera", type="primary", disabled=st.session_state.camera_active):
            st.session_state.camera_active = True
            st.session_state.camera_error_count = 0
            st.rerun()
    with camera_col2:
        if st.button("⏸️ Pause Camera", disabled=not st.session_state.camera_active):
            st.session_state.camera_active = False
            st.rerun()
    
    # Webcam display
    webcam_placeholder = st.empty()
    
    if st.session_state.camera_active:
        frame, error = get_ip_camera_frame()
        
        if frame is not None:
            st.session_state.last_frame = frame
            st.session_state.camera_error_count = 0
            webcam_placeholder.image(frame, channels="RGB", use_container_width=True)
        else:
            st.session_state.camera_error_count += 1
            if st.session_state.camera_error_count > 10:
                webcam_placeholder.error(f"❌ Camera connection lost: {error}")
                st.session_state.camera_active = False
            else:
                if st.session_state.last_frame is not None:
                    webcam_placeholder.image(st.session_state.last_frame, channels="RGB", use_container_width=True)
                    st.info(f"⚠️ Retrying... ({st.session_state.camera_error_count}/10)")
                else:
                    webcam_placeholder.warning("⚠️ Waiting for camera feed...")
    else:
        webcam_placeholder.info("📷 Camera paused. Click 'Start Camera' to resume.")

# Right column - Chat
with col2:
    st.markdown("## 💬 Chat Interface")
    
    # Listening mode controls
    listen_col1, listen_col2 = st.columns(2)
    with listen_col1:
        if st.button("🎤 Start Listening", type="primary", disabled=st.session_state.listening_active):
            st.session_state.listening_active = True
            st.rerun()
    
    with listen_col2:
        if st.button("⏹️ Stop Listening", disabled=not st.session_state.listening_active):
            st.session_state.listening_active = False
            st.rerun()
    
    # Status indicator
    if st.session_state.listening_active:
        st.success("🔴 **Listening Mode Active** - Listening for your voice...")
        
        try:
            with st.spinner("🎙️ Recording audio..."):
                record_audio(file_path=AUDIO_FILEPATH)
            
            with st.spinner("📝 Transcribing..."):
                user_input = transcribe_with_groq(AUDIO_FILEPATH)
            
            if user_input and user_input.strip():
                # Add user message
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": user_input
                })
                
                # Check for goodbye
                if "goodbye" in user_input.lower():
                    response = "Goodbye! Have a great day! 👋"
                    st.session_state.listening_active = False
                else:
                    with st.spinner("🤖 Dora is thinking..."):
                        response = ask_agent(user_query=user_input)
                
                # Add assistant message
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response
                })
                
                # Convert to speech (FIXED: was 'elevanlabs')
                with st.spinner("🔊 Generating voice response..."):
                    text_to_speech_with_elevenlabs(
                        input_text=response,
                        output_filepath=FINAL_AUDIO_FILEPATH
                    )
                
                # Clean up audio files
                for audio_file in [AUDIO_FILEPATH, "recorded_audio.wav"]:
                    if os.path.exists(audio_file):
                        try:
                            os.remove(audio_file)
                        except:
                            pass
        
        except Exception as e:
            st.error(f"❌ Error in listening mode: {str(e)}")
            st.session_state.listening_active = False
    
    # Chat container
    chat_container = st.container(height=350)
    
    # Display chat history
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.chat_message("user").write(f"🗣️ {message['content']}")
            else:
                st.chat_message("assistant").write(f"🤖 {message['content']}")
    
    # Play final response if exists
    if os.path.exists(FINAL_AUDIO_FILEPATH):
        with open(FINAL_AUDIO_FILEPATH, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3", autoplay=False)
    
    st.divider()
    
    # Manual audio input
    st.markdown("*Or record a single message:*")
    
    audio_value = st.audio_input(
        "Record a voice message",
        disabled=st.session_state.listening_active or st.session_state.processing
    )
    
    # Process single audio message
    if audio_value and not st.session_state.processing and not st.session_state.listening_active:
        audio_bytes = audio_value.getvalue()
        audio_hash = hashlib.md5(audio_bytes).hexdigest()
        
        if audio_hash != st.session_state.last_audio_hash:
            st.session_state.processing = True
            st.session_state.last_audio_hash = audio_hash
            
            with st.spinner("🎙️ Processing your voice..."):
                try:
                    with open("recorded_audio.wav", "wb") as f:
                        f.write(audio_bytes)
                    
                    user_input = transcribe_with_groq("recorded_audio.wav")
                    
                    if user_input and user_input.strip():
                        st.session_state.chat_history.append({
                            "role": "user",
                            "content": user_input
                        })
                        
                        if "goodbye" in user_input.lower():
                            response = "Goodbye! Have a great day! 👋"
                        else:
                            with st.spinner("🤖 Dora is thinking..."):
                                response = ask_agent(user_query=user_input)
                        
                        st.session_state.chat_history.append({
                            "role": "assistant",
                            "content": response
                        })
                        
                        with st.spinner("🔊 Generating voice response..."):
                            text_to_speech_with_elevenlabs(  # ✅ FIXED: was 'elevanlabs'
                                input_text=response,
                                output_filepath="final.mp3"
                            )
                        
                        if os.path.exists("recorded_audio.wav"):
                            os.remove("recorded_audio.wav")
                        
                        st.session_state.processing = False
                        st.rerun()
                        
                except Exception as e:
                    st.error(f"❌ Error processing audio: {str(e)}")
                    st.session_state.processing = False
    
    # Clear chat button
    col_clear1, col_clear2 = st.columns([3, 1])
    with col_clear2:
        if st.button("🗑️ Clear Chat", type="secondary", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.last_audio_hash = None
            st.session_state.listening_active = False
            st.rerun()

# Controlled camera refresh
if st.session_state.camera_active and not st.session_state.listening_active:
   # Increased delay to reduce strain
    st.rerun()
