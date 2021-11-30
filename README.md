# Spotify x CSE412 User Guide
User guide for the CSE 412 project. Follow the steps below to set up, run, and interact with the application.

## Prerequisites
* Python 3.9
* Pip
* PostgreSQL
* dos2unix
    * `sudo apt-get install dos2unix`
* System Requirements: WSL2, MacOS, Linux
* Visual Studio Code with Live Server Extension

## Steps to Run
1. Install  and enable the Live Server Extension from the Visual Studio Code Marketplace
<img src=images/liveserver.png>

2. Change directory to where you have cloned the repository
<img src=images/changeDirectory.png>

3. Since pulling files from GitHub can corrupt the file format, run `dos2unix setup.sh` from the project directory to remove any extraneous characters 
<img src=images/dos2unix.png>
 
4. After installing all the prerequisites run `./setup.sh` to start the backend for the application. You should see similar output to the following
<img src=images/setup.png>
All the http requests made by the webpage will be logged in this terminal window.
<img src=images/requests.png>

5. Open the directory containing <mark>index.html</mark> in Visual Studio Code and run the webpage using Live Server by right clicking on the file and selecting `Open with Live Server`
<img src=images/open1.png>
OR With the `index.html` file open in the editor, use the `Go Live` button in the bottom right corner to run the webpage using Live Server
<img src=images/open2.png>

6. A window with a web browser should open automatically, but if it doesn't, open any web browser and go to http://127.0.0.1:5500/ to access the website.
<img src=images/webpage.png>

## Functionality
1. Search using the provided metrics and provide an artist name for more specif results. Click search to load the results.
2. Hover over bars to see more detailed information about the artists, songs, or albums
3. Clicking on a bar will open a new tab which will search for the selected song, album, or artist on google