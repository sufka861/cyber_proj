FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Set the virtual environment as the default python
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Install tcpdump and ping
RUN apt-get update && apt-get install -y iputils-ping tcpdump
RUN chmod 777 /tmp

# Command to run the attack script and keep the container running
CMD ["sh", "-c", "python ${SCRIPT_TO_RUN} && tail -f /dev/null"]
