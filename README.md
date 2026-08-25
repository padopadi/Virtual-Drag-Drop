# ✋ AI-Powered Virtual Drag & Drop Interface

A real-time, touchless Human-Computer Interaction (HCI) web application that enables users to grab, move, and organize virtual UI elements using natural hand gestures.

🔗 **[Live Demo](https://virtual-drag-drop-cct3iykspbczyisske46en.streamlit.app)**

---

## 🚀 Features

* **Real-Time Hand Tracking:** High-precision landmark tracking powered by MediaPipe and CVZone.
* **Pinch-to-Drag Gesture:** Intuitive interaction using index and middle fingertip proximity detection.
* **Low-Latency Streaming:** WebRTC integration for smooth browser-based video feed processing.
* **Cloud Deployed:** Fully hosted and running live on Streamlit Cloud.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11
* **Computer Vision:** OpenCV (`opencv-python-headless`), MediaPipe, CVZone
* **Frontend / Framework:** Streamlit, Streamlit-WebRTC, PyAV
* **Deployment:** Streamlit Community Cloud

---

## 🎮 How It Works

1. Open the live app and allow webcam permissions.
2. Position your hand in front of the camera.
3. Bring your **Index** and **Middle** fingertips together within any purple block.
4. Move your hand to drag the block across the canvas; release your pinch to drop it.

---

## 💻 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/padopadi/Virtual-Drag-Drop.git](https://github.com/padopadi/Virtual-Drag-Drop.git)
   cd Virtual-Drag-Drop
