import datetime
import psutil

def close_app():
    # Check if the time is 7:00pm and if it is a weekday (Monday to Friday)
    now = datetime.datetime.now()
    if now.hour != 19 or now.minute != 0 or now.weekday() >= 5:
        return
    
    # Check if MontavueGo.exe is running
    app_open = False
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'MontavueGo.exe':
            app_open = True
            # Terminate the app
            psutil.Process(process.info['pid']).terminate()
            break
    
    if not app_open:
        return


close_app()