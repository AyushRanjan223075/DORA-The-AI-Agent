import cv2
import base64
import requests
import numpy as np
from dotenv import load_dotenv

load_dotenv()

# IP Webcam URL (same as in main.py)
IP_WEBCAM_URL = "http://10.5.124.71:8080/shot.jpg"

def capture_image_from_ip_webcam() -> str:
    """
    Captures one frame from IP webcam and encodes it as Base64 JPEG.
    """
    try:
        # Fetch image from IP webcam
        response = requests.get(IP_WEBCAM_URL, timeout=5)
        
        if response.status_code != 200:
            raise RuntimeError(f"Failed to fetch image from IP webcam. Status: {response.status_code}")
        
        # Convert response content to numpy array
        img_arr = np.array(bytearray(response.content), dtype=np.uint8)
        
        # Decode image
        frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        
        if frame is None:
            raise RuntimeError("Failed to decode image from IP webcam")
        
        # Save for debugging (optional)
        cv2.imwrite("sample.jpg", frame)
        
        # Encode to base64
        ret, buf = cv2.imencode('.jpg', frame)
        if not ret:
            raise RuntimeError("Failed to encode image")
        
        return base64.b64encode(buf).decode('utf-8')
        
    except requests.exceptions.Timeout:
        raise RuntimeError("IP webcam connection timeout - check if IP camera is accessible")
    except requests.exceptions.ConnectionError:
        raise RuntimeError("Cannot connect to IP webcam - verify URL and network connection")
    except Exception as e:
        raise RuntimeError(f"Error capturing from IP webcam: {str(e)}")


from groq import Groq

def analyze_image_with_query(query: str) -> str:
    """
    Expects a string with 'query'.
    Captures the image from IP webcam and sends the query and the image
    to Groq's vision chat API and returns the analysis.
    """
    try:
        img_b64 = capture_image_from_ip_webcam()
    except RuntimeError as e:
        return f"Error capturing image: {str(e)}"
    
    model = "meta-llama/llama-4-maverick-17b-128e-instruct"
    
    if not query or not img_b64:
        return "Error: both 'query' and 'image' fields required."

    try:
        client = Groq()  
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_b64}",
                        },
                    },
                ],
            }
        ]
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model
        )

        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error analyzing image: {str(e)}"
