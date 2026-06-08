import threading
import time

from app.services.sqs_service import (
    sqs_service
)


class VisibilityHeartbeat:

    def __init__(
        self,
        receipt_handle
    ):

        self.receipt_handle = receipt_handle

        self.running = True

    def start(self):

        thread = threading.Thread(
            target=self.run
        )

        thread.daemon = True

        thread.start()

    def run(self):

        while self.running:

            sqs_service.extend_visibility(
                self.receipt_handle,
                300
            )

            time.sleep(60)

    def stop(self):

        self.running = False