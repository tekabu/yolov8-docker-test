sudo docker build -t yolov8 .

export DISPLAY=:0

xhost +local:docker

sudo docker run -it \
	--device=/dev/video0 \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v ./src:/home/src \
    yolov8 \
    bash