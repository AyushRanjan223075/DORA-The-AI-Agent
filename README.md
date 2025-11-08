# 👧🏼 NOVA - Your Personal AI Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An end-to-end agentic GenAI application featuring real-time vision, voice interaction, and intelligent conversation capabilities powered by Google's Gemini, Groq API, and ElevenLabs.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Configuration](#configuration) • [Troubleshooting](#troubleshooting)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Keys Setup](#api-keys-setup)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🌟 Overview

**Dora** is an intelligent AI assistant that combines multiple AI technologies to create a seamless multimodal interaction experience. The application uses:

- **Vision AI**: Real-time image analysis from IP webcam feeds
- **Voice Interaction**: Speech-to-text and text-to-speech capabilities
- **Agentic AI**: Autonomous decision-making using LangGraph and Google Gemini
- **Real-time Chat**: Interactive conversation interface with chat history

Dora can see through your camera, listen to your voice, understand context, and respond naturally with synthesized speech—all in real-time.

---

## ✨ Features

### 🎥 Vision Capabilities
- **Real-time Webcam Integration**: Connects to IP webcam for live video feed
- **Visual Question Answering**: Analyzes images and answers queries about what it sees
- **Object Recognition**: Identifies objects, colors, and scenes in real-time

### 🎤 Voice Interaction
- **Speech-to-Text**: Converts your voice commands to text using Groq's Whisper model
- **Natural Language Processing**: Understands context and intent from spoken queries
- **Text-to-Speech**: Responds with natural-sounding voice using ElevenLabs API
- **Continuous Listening Mode**: Hands-free operation with automatic audio recording

### 🤖 Intelligent AI Agent
- **Agentic Behavior**: Autonomous decision-making using LangGraph
- **Tool Integration**: Automatically decides when to use vision tools
- **Context Awareness**: Maintains conversation history for coherent interactions
- **Multi-modal Reasoning**: Combines visual and textual information for responses

### 💬 User Interface
- **Split-Screen Layout**: Simultaneous view of webcam feed and chat interface
- **Real-time Updates**: Live webcam feed with minimal latency
- **Audio Playback**: Plays AI responses with embedded audio player
- **Chat History**: Persistent conversation history during session
- **Manual Controls**: Start/stop camera and listening modes independently

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Streamlit UI (main.py)                   │
│  ┌──────────────────────┐      ┌─────────────────────────────┐ │
│  │   Webcam Feed        │      │      Chat Interface         │ │
│  │   (IP Camera)        │      │   - Voice Input             │ │
│  │                      │      │   - Text Display            │ │
│  │                      │      │   - Audio Playback          │ │
│  └──────────────────────┘      └─────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ├─ Speech to Text (speech_to_text.py)
                              │  └─ Groq Whisper API
                              │
                              ├─ AI Agent (ai_agent.py)
                              │  ├─ Google Gemini 2.0 Flash
                              │  ├─ LangChain + LangGraph
                              │  └─ ReAct Agent Pattern
                              │
                              ├─ Vision Tools (tools.py)
                              │  ├─ Image Capture from IP Webcam
                              │  └─ Groq Vision API (Llama 4)
                              │
                              └─ Text to Speech (text_to_speech.py)
                                 ├─ ElevenLabs API (Primary)
                                 └─ gTTS (Fallback)
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **UI Framework** | Streamlit | Web interface and real-time updates |
| **AI Orchestration** | LangChain + LangGraph | Agent creation and tool routing |
| **Language Model** | Google Gemini 2.0 Flash | Main conversational AI |
| **Vision Model** | Meta Llama 4 Maverick (via Groq) | Image analysis and VQA |
| **Speech-to-Text** | Whisper Large v3 (via Groq) | Audio transcription |
| **Text-to-Speech** | ElevenLabs API | Natural voice synthesis |
| **Camera Integration** | IP Webcam + OpenCV | Live video streaming |
| **Package Manager** | UV | Fast Python dependency management |

---

## 📦 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 11+, or Linux (Ubuntu 20.04+)
- **Python**: 3.10 or higher
- **RAM**: Minimum 4GB (8GB recommended)
- **Internet**: Stable connection for API calls

### Required Software
1. **UV Package Manager** (recommended) or pip
2. **IP Webcam App** (for Android/iOS) or any IP camera
3. **Microphone** for voice input
4. **Speakers/Headphones** for audio output

### API Keys Required
You'll need to obtain free API keys from:
- [Google AI Studio](https://aistudio.google.com/) (Gemini API)
- [Groq Console](https://console.groq.com/) (Groq API)
- [ElevenLabs](https://elevenlabs.io/) (Text-to-Speech API)

---

## 🚀 Installation

### Step 1: Install UV Package Manager

UV is an extremely fast Python package manager written in Rust. It's 10-100x faster than pip and handles virtual environments automatically.

#### On Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### On Windows (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Alternative Installation (via pip):
```bash
pip install uv
```

Verify installation:
```bash
uv --version
```

### Step 2: Clone the Repository

```bash
git clone <your-repository-url>
cd dora-ai-assistant
```

### Step 3: Install Python (via UV)

UV can automatically install and manage Python versions:

```bash
# Install Python 3.10 or higher
uv python install 3.10

# Verify installation
uv python list
```

### Step 4: Create Virtual Environment

```bash
# UV automatically creates and manages virtual environments
uv venv

# Activate the virtual environment
# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\\Scripts\\activate
```

### Step 5: Install Dependencies

```bash
# Install all required packages using UV
uv pip install streamlit opencv-python-headless requests numpy python-dotenv
uv pip install langchain langchain-google-genai langgraph
uv pip install groq elevenlabs speechrecognition pydub pygame gtts
```

#### Alternative: Using requirements.txt

Create a `requirements.txt` file with the following content:

```txt
streamlit>=1.28.0
opencv-python-headless>=4.8.0
requests>=2.31.0
numpy>=1.24.0
python-dotenv>=1.0.0
langchain>=0.1.0
langchain-google-genai>=0.0.6
langgraph>=0.0.26
groq>=0.4.0
elevenlabs>=0.2.24
SpeechRecognition>=3.10.0
pydub>=0.25.1
pygame>=2.5.0
gTTS>=2.3.2
```

Then install:
```bash
uv pip install -r requirements.txt
```

### Step 6: Install System Dependencies

#### For Audio Processing (Linux/macOS):
```bash
# Ubuntu/Debian
sudo apt-get install portaudio19-dev python3-pyaudio ffmpeg

# macOS
brew install portaudio ffmpeg
```

#### For Audio Processing (Windows):
- Download and install [FFmpeg](https://ffmpeg.org/download.html)
- Add FFmpeg to your system PATH

---

## ⚙️ Configuration

### Step 1: Set Up IP Webcam

1. **Download IP Webcam App**:
   - Android: [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam)
   - iOS: [IP Camera Lite](https://apps.apple.com/us/app/ip-camera-lite/id1013455241)

2. **Start the Camera Server**:
   - Open the app
   - Scroll down and tap "Start Server"
   - Note the IP address shown (e.g., `http://192.168.1.100:8080`)

3. **Update IP Address in Code**:
   
   Edit `main.py` and `tools.py` to update the IP address:
   
   ```python
   # In main.py (line 20)
   IP_WEBCAM_URL = "http://YOUR_IP_ADDRESS:8080/shot.jpg"
   
   # In tools.py (line 10)
   IP_WEBCAM_URL = "http://YOUR_IP_ADDRESS:8080/shot.jpg"
   ```

### Step 2: Create Environment File

Create a `.env` file in the project root directory:

```bash
touch .env  # Linux/macOS
# or
type nul > .env  # Windows
```

Add your API keys to `.env`:

```env
# Google Gemini API Key
GOOGLE_API_KEY=your_google_api_key_here

# Groq API Key (for Vision and Whisper)
GROQ_API_KEY=your_groq_api_key_here

# ElevenLabs API Key (for Text-to-Speech)
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

### Step 3: Verify Configuration

Create a simple test script (`test_config.py`):

```python
import os
from dotenv import load_dotenv

load_dotenv()

print("✓ GOOGLE_API_KEY:", "✓ Set" if os.getenv("GOOGLE_API_KEY") else "✗ Missing")
print("✓ GROQ_API_KEY:", "✓ Set" if os.getenv("GROQ_API_KEY") else "✗ Missing")
print("✓ ELEVENLABS_API_KEY:", "✓ Set" if os.getenv("ELEVENLABS_API_KEY") else "✗ Missing")
```

Run:
```bash
uv run python test_config.py
```

---

## 🎯 Usage

### Starting the Application

1. **Ensure your IP webcam is running** (see Configuration section)

2. **Activate the virtual environment** (if not already activated):
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\\Scripts\\activate    # Windows
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

4. **Open your browser**: The app will automatically open at `http://localhost:8501`

### Using the Interface

#### Webcam Feed (Left Panel)
- **Start Camera**: Begin live video stream from IP webcam
- **Pause Camera**: Temporarily stop the video feed
- The camera feed refreshes automatically to show real-time video

#### Chat Interface (Right Panel)

**Option 1: Continuous Listening Mode**
1. Click **"🎤 Start Listening"**
2. Speak your question clearly
3. The system will:
   - Record your audio
   - Transcribe it to text
   - Process through the AI agent
   - Display the response
   - Play audio response
4. Say **"goodbye"** to stop listening mode

**Option 2: Manual Recording**
1. Click the **audio input widget** at the bottom
2. Record your message
3. Stop recording
4. The system processes automatically

#### Example Interactions

**Vision-based queries:**
- *"What do you see in front of the camera?"*
- *"What color is the object in the image?"*
- *"Describe what's in the room"*
- *"Can you identify this object?"*

**General queries:**
- *"What's the weather like?"*
- *"Tell me a joke"*
- *"How are you today?"*

**Multi-turn conversations:**
- *"What do you see?"* → (Response) → *"What color is it?"*

---

## 📁 Project Structure

```
dora-ai-assistant/
│
├── main.py                    # Main Streamlit application
├── ai_agent.py                # AI agent logic with LangGraph
├── tools.py                   # Vision tools for image analysis
├── speech_to_text.py          # Audio recording and transcription
├── text_to_speech.py          # Text-to-speech synthesis
│
├── .env                       # Environment variables (API keys)
├── .env.example               # Example environment file
├── requirements.txt           # Python dependencies
├── README.md                  # This file
│
├── .venv/                     # Virtual environment (created by UV)
├── sample.jpg                 # Sample captured image (generated)
├── audio_question.mp3         # Temporary audio file
├── recorded_audio.wav         # Temporary recorded audio
└── final.mp3                  # Generated speech response
```

### File Descriptions

#### `main.py` (Streamlit UI)
- Implements the web interface with two-column layout
- Manages webcam feed from IP camera
- Handles user interactions (voice/text input)
- Displays chat history and plays audio responses
- Coordinates all components

#### `ai_agent.py` (AI Agent)
- Creates the ReAct agent using LangGraph
- Integrates Google Gemini 2.0 Flash as the LLM
- Defines system prompt for agent personality ("NOVA")
- Routes queries to appropriate tools
- Returns formatted responses

#### `tools.py` (Vision Tools)
- **`capture_image_from_ip_webcam()`**: Captures frame from IP camera
- **`analyze_image_with_query()`**: Sends image + query to Groq Vision API
- Uses Meta Llama 4 for visual question answering
- Encodes images as base64 for API transmission

#### `speech_to_text.py` (Audio Input)
- **`record_audio()`**: Records audio from microphone using SpeechRecognition
- **`transcribe_with_groq()`**: Transcribes audio using Groq's Whisper model
- Saves audio in MP3 format for processing

#### `text_to_speech.py` (Audio Output)
- **`text_to_speech_with_elevenlabs()`**: Generates natural voice using ElevenLabs
- **`text_to_speech_with_gtts()`**: Fallback TTS using Google Text-to-Speech
- **`play_audio()`**: Plays generated audio using Pygame

---

## 🔑 API Keys Setup

### 1. Google Gemini API Key

**Steps:**
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" in the left sidebar
4. Create a new API key
5. Copy the key and add to `.env`:
   ```env
   GOOGLE_API_KEY=AIzaSy...your_key_here
   ```

**Free Tier:**
- 60 requests per minute
- 1,500 requests per day
- Sufficient for personal use

### 2. Groq API Key

**Steps:**
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Navigate to "API Keys" section
4. Click "Create API Key"
5. Copy the key and add to `.env`:
   ```env
   GROQ_API_KEY=gsk_...your_key_here
   ```

**Free Tier:**
- Access to Whisper (transcription) and Vision models
- Rate limits apply (check console for details)

### 3. ElevenLabs API Key

**Steps:**
1. Visit [ElevenLabs](https://elevenlabs.io/)
2. Sign up for a free account
3. Go to Profile → API Keys
4. Generate a new API key
5. Copy the key and add to `.env`:
   ```env
   ELEVENLABS_API_KEY=sk_...your_key_here
   ```

**Free Tier:**
- 10,000 characters per month
- Access to standard voices
- Sufficient for testing and demos

### Environment File Template

Create `.env.example` as a template:

```env
# Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here

# Groq API
GROQ_API_KEY=your_groq_api_key_here

# ElevenLabs API
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. **Camera Connection Issues**

**Problem**: "Camera connection lost" or "Cannot connect to IP webcam"

**Solutions:**
- Verify IP webcam app is running on your phone
- Check the IP address in `main.py` and `tools.py` matches the app
- Ensure your computer and phone are on the same WiFi network
- Try accessing the camera URL in your browser first: `http://YOUR_IP:8080`
- Disable firewall temporarily to test connectivity
- Restart the IP webcam app

#### 2. **Audio Recording Not Working**

**Problem**: Microphone not detecting input

**Solutions:**
- Grant microphone permissions to your terminal/Python
- Check default audio input device in system settings
- Install PortAudio:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install portaudio19-dev
  
  # macOS
  brew install portaudio
  ```
- Test microphone with system settings first
- Try a different microphone if available

#### 3. **API Key Errors**

**Problem**: "Invalid API key" or "Authentication failed"

**Solutions:**
- Verify API keys are correctly copied to `.env` (no extra spaces)
- Ensure `.env` file is in the project root directory
- Check if API keys have expired or been revoked
- Regenerate API keys if necessary
- Restart the Streamlit app after updating `.env`

#### 4. **Import Errors**

**Problem**: `ModuleNotFoundError` for packages

**Solutions:**
- Ensure virtual environment is activated:
  ```bash
  source .venv/bin/activate  # Linux/macOS
  ```
- Reinstall dependencies:
  ```bash
  uv pip install -r requirements.txt
  ```
- Check Python version (must be 3.10+):
  ```bash
  python --version
  ```

#### 5. **Text-to-Speech Issues**

**Problem**: No audio playback or errors in TTS

**Solutions:**
- Verify ElevenLabs API key and quota
- Check system audio output is working
- Install FFmpeg:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install ffmpeg
  
  # macOS
  brew install ffmpeg
  ```
- Try the gTTS fallback by modifying `text_to_speech.py`

#### 6. **Streamlit Won't Start**

**Problem**: `streamlit: command not found`

**Solutions:**
- Activate virtual environment first
- Install streamlit explicitly:
  ```bash
  uv pip install streamlit
  ```
- Use full path:
  ```bash
  python -m streamlit run main.py
  ```

#### 7. **High CPU Usage**

**Problem**: Application consuming too much CPU

**Solutions:**
- Increase camera refresh delay in `main.py`
- Pause camera when not needed
- Reduce webcam resolution in IP Webcam app settings
- Use hardware acceleration if available

#### 8. **Vision Model Not Working**

**Problem**: Agent doesn't analyze images or returns errors

**Solutions:**
- Check Groq API quota and rate limits
- Verify camera is capturing images (check for `sample.jpg`)
- Ensure IP webcam URL is correct
- Test vision endpoint separately using `tools.py`

### Debug Mode

Enable verbose logging by modifying `ai_agent.py`:

```python
import langchain
langchain.verbose = True
langchain.debug = True
```

Run with Python directly to see detailed logs:
```bash
python ai_agent.py
```

### Getting Help

If you encounter issues not covered here:
1. Check the [Streamlit documentation](https://docs.streamlit.io/)
2. Review [LangChain documentation](https://python.langchain.com/)
3. Check API provider status pages
4. Open an issue on GitHub with:
   - Error message
   - Steps to reproduce
   - System information (OS, Python version)
   - Relevant logs

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs
- Use the GitHub issue tracker
- Include detailed error messages and logs
- Provide steps to reproduce
- Specify your environment (OS, Python version, etc.)

### Suggesting Features
- Open a feature request issue
- Explain the use case and benefits
- Provide examples if possible

### Submitting Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your fork (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/dora-ai-assistant.git
cd dora-ai-assistant

# Install dev dependencies
uv pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Format code
black .
ruff check .
```

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **Google** - Gemini 2.0 Flash LLM
- **Groq** - Ultra-fast inference for Whisper and Llama models
- **ElevenLabs** - Natural text-to-speech synthesis
- **Meta** - Llama 4 vision model
- **LangChain** - Agent orchestration framework
- **Streamlit** - Beautiful web UI framework
- **Astral** - UV package manager


## 🚀 Future Enhancements

Planned features for upcoming releases:

- [ ] Multi-camera support
- [ ] Persistent chat history (database integration)
- [ ] Custom voice cloning
- [ ] Screen sharing capability
- [ ] Mobile app version
- [ ] Multiple language support
- [ ] Image generation integration
- [ ] Tool for web search
- [ ] RAG (Retrieval Augmented Generation) support
- [ ] Emotion detection from voice
- [ ] Background noise cancellation
- [ ] Custom wake word detection

---

## ⭐ Star History

If you find this project useful, please consider giving it a star on GitHub!

---

**Built with ❤️ using GenAI technologies**
