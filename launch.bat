@echo off

set mypath=%cd%
cd %mypath%/venv/Scripts/

cmd /k "activate & cd ../.. & python app.py & cd venv/Scripts & deactivate & exit"