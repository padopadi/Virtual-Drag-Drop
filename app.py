import math
import av
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import streamlit as st
from streamlit_webrtc import RTCConfiguration, VideoTransformerBase, webrtc_streamer

st.set_page_config(page_title="Virtual Drag and Drop", layout="wide")
st.title("✋ Virtual Drag and Drop")
st.markdown("Bring your **Index** and **Middle** fingertips together inside any box to grab and drag it.")


class DragRect:
    def __init__(self, posCentre, size=[150, 150]):
        self.posCentre = list(posCentre)
        self.size = size
        self.color = (255, 0, 255)

    def update(self, cursor):
        cx, cy = self.posCentre
        w, h = self.size
        # Check if cursor is within rectangle boundaries
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCentre = [int(cursor[0]), int(cursor[1])]
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 255)


class HandProcessor(VideoTransformerBase):
    def __init__(self):
        self.detector = HandDetector(detectionCon=0.7, maxHands=1)
        self.rectList = [DragRect([x * 220 + 150, 150]) for x in range(3)]

    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        img = frame.to_ndarray(format="bgr24")
        img = cv2.flip(img, 1)

        # 1. Detect Hand
        hands, img = self.detector.findHands(img, flipType=False)

        if hands:
            lmList = hands[0]["lmList"]

            # Extract (x, y) coordinates for Index (8) and Middle (12) fingertips
            x1, y1 = lmList[8][0], lmList[8][1]
            x2, y2 = lmList[12][0], lmList[12][1]

            # Calculate distance directly without external function dependencies
            length = math.hypot(x2 - x1, y2 - y1)

            # When fingers are pinched together (drag state)
            if length < 45:
                cursor = (x1, y1)
                for rect in self.rectList:
                    rect.update(cursor)

        # 2. Draw all rectangles on every frame
        for rect in self.rectList:
            cx, cy = rect.posCentre
            w, h = rect.size
            cv2.rectangle(
                img,
                (cx - w // 2, cy - h // 2),
                (cx + w // 2, cy + h // 2),
                rect.color,
                cv2.FILLED,
            )
            cvzone.cornerRect(img, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


# STUN server configuration for stable WebRTC streaming
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

webrtc_streamer(
    key="hand-drag-drop",
    video_processor_factory=HandProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)