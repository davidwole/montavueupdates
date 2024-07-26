import datetime
import psutil
import time


def check_app():
    # Check if the app is already open if not launch the app
    app_name = 'MontavueGo.exe'
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == app_name:
                print('App is open')
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    launch_app()
    
        
def checking_weekend():
    # Get the current day of the week (0 = Monday, 1 = Tuesday, ..., 5 = Saturday, 6 = Sunday)
    current_day = datetime.datetime.today().weekday()

    # Get the current time
    current_time = datetime.datetime.now().time()

    # Define the time range (6am to 7pm)
    start_time = datetime.time(6, 0)
    end_time = datetime.time(19, 0)

    # Check if it is a weekend and within the specified time range
    if current_day >= 5 or not (start_time <= current_time <= end_time):
        # If it's Saturday (5) or Sunday (6), or not within the time range, do not run the code
        return
    else:
        # Call the function if it is a weekday and within the specified time range
        check_app()
    
def launch_app():
    # Launches the MontavueGo App
    print('Hello, world!')

checking_weekend()