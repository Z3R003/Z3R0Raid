@echo off
echo Installing requirements...
pip install -r requirements.txt
echo Requirements installed successfully!
echo Launching the tool...

cls

python main.py
