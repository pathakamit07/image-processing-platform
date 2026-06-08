import time
import uuid


def current_timestamp():

    return int(time.time())


def generate_s3_key(job_id):

    return f"images/{job_id}.txt"


def generate_worker_id():

    return str(uuid.uuid4())