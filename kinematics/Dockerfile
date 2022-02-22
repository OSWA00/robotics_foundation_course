FROM python:3.9-slim

# Create container user and workspace
RUN useradd --create-home --shell /bin/bash user
WORKDIR /home/user

# Update and install dependencies
COPY requirements.txt ./
RUN apt-get -y update
RUN pip install --no-cache-dir -r requirements.txt

USER user

CMD ["bash"]