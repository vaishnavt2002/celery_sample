from celery import shared_task
import time


@shared_task
def generate_sub_tasks():
    """
    This task waits 100 minutes then generates 200 sub-tasks.
    """
    print("Parent task started. Waiting 100 minutes...")
    time.sleep(100)  # 100 mins

    print("Generating 1000 child tasks...")
    for i in range(1000):
        child_task.delay(i)

    return "Created 1000 tasks successfully"


@shared_task
def child_task(task_no):
    """
    Each child task takes 2 minutes.
    """
    print(f"Child task {task_no} started...")
    time.sleep(2 * 60)  # 2 mins
    print(f"Child task {task_no} completed!")

    return f"Task {task_no} done"
