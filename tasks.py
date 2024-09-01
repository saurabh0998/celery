from celery import Celery

app = Celery('tasks', 
        broker='redis://localhost:6379/0', 
        backend='redis://localhost:6379/0'
)        

@app.task
def calculate_power_to_weight_ratio(weight, horsepower):
    if horsepower == 0:  # Avoid division by zero
        return None
    return weight / horsepower
