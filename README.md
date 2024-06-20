# Tweaks - Extra!

### Why?

I recently moved to Linux as my daily driver, because I was tired of Microsoft invading every part of my computing life. Especially now that Recall is a thing. I also wanted to better support the FOSS community. I really like GNOME, however, there are a few settings that are very hard to
get to, let alone change, without downloading extensions that can break whenever the shell updates.

So, to get around that, I'm building a Python based GUI app that will expose the settings and provide the user with a simple interface for editing. 

### Features

- Edit the system-wide name of audio sinks and sources in the system. 

### Status

Finished the minimal interface design for the app. Visually it is styled like the Dracula - Official theme in VSCode.


### Installation

Obtaining Source Files

1. Clone the repository from <a href="https://github.com/jGDarkness/tweaks-extra/tree/branch_mvp_0.1.1">~here~</a>.
2a. Download the repository by right-clicking <a href="https://github.com/jGDarkness/tweaks-extra/archive/refs/heads/branch_mvp_0.1.1.zip">~here~></a> and selecting "Save As..." and saving to a directory of your choice.
2.b Extract the respository to a location of your choice.
3. Download with wget:

'''bash
wget https://github.com/jGDarkness/tweaks-extra/archive/refs/heads/branch_mvp_0.1.1.zip ~/Downloads/tweaks-extra.zip
'''

Building from Source

1. Navigate to the directory where you downloaded the source files, and start a new terminal session in that directory. 
2. Setup and activate a virtual environment:

'''python
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

# Placeholder for pyinstaller command line when implemented.
'''

Download Linux-ready Executable

<placeholder for downloadable bundle>


### Python Source Documentation

PyQt6 is used as the GUI framework. At the time of publication, PyQt6 version 6.7.0 was the newest version, and the version has been pinned in 'requirements.txt'.

pyinstaller is used to create the executable file for Linux. PyInstaller version 6.8.0 was the newest version, and the version has been pinned in 'requirements.txt'. It also requires pyinstaller-hooks-contrib to be pinned to a fixed version at the same time. The newest version, and the version that has been pinned in requirements.txt is 2024.7.
