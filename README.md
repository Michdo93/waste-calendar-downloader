# waste-calendar-downloader
A waste calendar downloader written in Python with Selenium to download the waste calender for Furtwangen University.

The code can be customized, of course. It is just an example of how to navigate through such a page to generate the waste calendar. Change the URL and the XPaths accordingly.

Note: I use Mozilla Firefox in headless mode. Unfortunately Chrome did not work because the website detects that automation software is being used.

# Installation

At first you have to install Selenium:

```
python3 -m pip install selenium
```

Then you have to download the code and make it executable:

```
wget https://raw.githubusercontent.com/Michdo93/waste-calendar-downloader/main/waste_calendar_downloader.py
sudo chmod +x waste_calendar_downloader.py
```

At least you have to run the code and wait:

```
python3 waste_calendar_downloader.py
```
