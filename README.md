This back-end app is running on port 80 and it mentioned inside "app.py" file.

You can build an image with the command below:
* docker build -t <name:tag> .

Then , running the container with the command below:
* docker run -d -p 80:80 <name:tag>
