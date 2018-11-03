FROM fnndsc/ubuntu-python3

# Steps to install YAJL
RUN apt-get -y install cmake
RUN apt-get install -y ruby
RUN apt-get install -y git
RUN git clone git://github.com/lloyd/yajl
RUN cd yajl && ./configure && make && make install

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
ENTRYPOINT ["python3"]
CMD ["app.py"]