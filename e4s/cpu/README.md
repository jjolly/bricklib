# Creating a Docker image for the E4S project from ECP

## Building the Docker image
To build a Docker image from these files for the CPU based E4S image, type the following command in this directory:

```
docker build -t <your-image-name> .
```

You can use almost anything for an image name, but traditionally the image name is formatted like:

```
<docker-hub-username>/<docker-hub-repository-name>:latest
```

This is necessary only if you expect to push your image build to Docker Hub. If you don't expect to push this image, pick a name that make sense.

## Using the Docker image
You can start a Docker container using your new image with this command:

```
docker run -it --name=<your-container-name> <your-image-name>
```

This will put you at a command prompt where you may begin using the Bricks library as built by Spack!

Have fun!
