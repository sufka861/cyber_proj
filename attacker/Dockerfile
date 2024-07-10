FROM python:3.12
WORKDIR /usr/src/app

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install dependencies
COPY requirements.txt .
RUN . venv/bin/activate && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the virtual environment as the default python
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Install tcpdump and ping
RUN apt-get update && apt-get install -y iputils-ping tcpdump
RUN chmod 777 /tmp

# Command to run the attack script and keep the container running
CMD ["sh", "-c", "python attack.py && tail -f /dev/null"]
