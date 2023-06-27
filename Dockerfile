# Use the official Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /polyBot

# Copy the necessary files to the container
COPY . /polyBot

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install yt-dlp
RUN pip install yt-dlp

# Run the Bot application
CMD [ "python", "bot.py" ]
