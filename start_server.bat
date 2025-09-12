@echo off
echo ================================
echo   Starting Django Server
echo ================================
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.
echo Starting Django development server...
echo.
echo *** IMPORTANT INFORMATION ***
echo Your website will be available at:
echo   - http://127.0.0.1:8000/     (Main website)
echo   - http://localhost:8000/     (Alternative URL)
echo.
echo Your ADMIN PANEL will be available at:
echo   - http://127.0.0.1:8000/admin/
echo   - http://localhost:8000/admin/
echo.
echo Admin Login Credentials:
echo   - Username: admin
echo   - Password: [the password you set during setup]
echo.
echo To STOP the server: Press Ctrl+C
echo ================================
echo.
python manage.py runserver
pause
