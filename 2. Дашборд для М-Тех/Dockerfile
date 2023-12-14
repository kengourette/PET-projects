# Base image is Python 3.9
FROM python:3.9-slim

# Set the working directory
WORKDIR /MTech_test

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the model and application code into the container
COPY streamlit_dash.py .

# Define the port on which the Streamlit application will runStreamlit
ENV PORT 8501

# The command that will be run when the Docker container starts
CMD streamlit run --server.port $PORT streamlit_dash.py
