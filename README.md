# Cryo PiCam

Fast speed imaging of moving Cryo-EM specimens with time resolution. This project is inspired by the [Vitrocam project](https://www.biorxiv.org/content/10.1101/2022.06.16.496351v1) and aims at using the lastest APIs for increased resolution and build an analysis toolbox for processing the images.

## Hardware

- ov9281 sensor
- Raspberri Pi 4
- *add info about the motion sensor*

## Setting up the Raspberri Pi

1. Flash an SD card with **RaspberriPi OS based on Debian Bullseye (32-bit)**

    Note: It should work with 64-bit but it has not been tested at this time.

2. Open `/boot/config.txt` and activate the kernel module for the ov9281 sensor.

    ```shell-session
    sudo vim /boot/config.txt

    #Add this line to the top of the file
    dtoverlay=ov9281,media-controller=1
    ```

3. Update the repository and the installed packages
    ```shell-session
    sudo apt update
    sudo apt upgrade
    ```

## Installation

### Dependencies

1. install the system dependencies
    ```shell-session
    sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev git -y
    ```
2. Other dependencies
    ```shell-session
    sudo pip3 install pydantic matplotlib

    ## This one will take a while to build
    sudo pip3 install opencv-python
    ```

3. Download CryoPiCam
    ```shell-session
    git clone 
    cd cryopicam
    ```

4.  Edit your settings (more options soon)
    ```shell-session
    vim settings.env

    ##Edit the values to your needs
    dataDir=/home/pi/picam_data/
    sensorPin=7
    ```
    - `dataDir`: Where you want the data to be saved
    - `sensorPin`: GPIO pin number where the motion sensor is connected on the pi.

## Testing the installation

*Coming soon*

## Usage

`python run.py name_of_grid`

It will create a grid_directory under the `datadir` and will save the raw stream as `all_frames.raw` of frames, the indiviual frames in `frames/??.png`, the timestamps with the frames as `meta.json` the timestamped movie as `movie.mp4`

The timestamps are relative to the sensor trigger timestamp. Negative number are frame prior to sensor activate and the positive numbers are from after.