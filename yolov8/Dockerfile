FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y \
	libgl1-mesa-glx \
	libglib2.0-0 \
	wget
    
RUN python -m pip install --upgrade pip

RUN pip install ultralytics==8.0.20

RUN wget -O /home/yolov8n.pt https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt