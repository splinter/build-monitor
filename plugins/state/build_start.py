import logging
import time

MAX_BUILD_DURATION=60*5
WAIT_TIME=5

def is_event_build_start(event):
    return True
def record_new_build_start(event):
    return True
def record_current_build_end(event):
    return True
def record_current_build_failure(event):
    return True
def has_build_max_duration_expired(event):
    return True
def get_expired_builds():
    return []
def build_success_event():
    return {}
def build_failed_event():
    return {}

class BuildStartPlugin:
    def init(self,plugin_services):
        self.plugin_services = plugin_services
        return
    def inspect(self,event):
        return

    def loop(self):
        queue_service = self.plugin_services.get_queue_service()

        while True:
            logging.info("Checking if a build time out has expired")
            expired_builds = get_expired_builds()
            if len(expired_builds) > 0:
                logging.info("Recording build completed")
                for build in expired_builds:
                    queue_service.push_input_event(build_failed_event())
            time.sleep(WAIT_TIME)
        return