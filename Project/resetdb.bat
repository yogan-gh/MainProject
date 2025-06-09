@echo off
call ".venv\Scripts\activate"
python "main\manage.py" flush
pause