# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

# Use a supported base image (Debian Bullseye instead of old Buster)
FROM python:3.10-slim-bullseye

# Install required system packages
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Setup working directory
WORKDIR /VJ-FILTER-BOT
COPY . /VJ-FILTER-BOT

# Start the bot
CMD ["python", "bot.py"]
