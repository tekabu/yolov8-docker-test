FROM yolov8-gui-base

WORKDIR /home

COPY ./src/requirements.txt /home/requirements.txt

RUN pip install -r /home/requirements.txt

RUN echo 'alias py="python"' >> ~/.bashrc

RUN echo 'alias ll="ls -l"' >> ~/.bashrc
RUN echo 'alias la="ls -la"' >> ~/.bashrc

CMD ["bash"]
