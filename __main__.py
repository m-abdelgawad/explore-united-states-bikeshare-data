from packages.project import absolute_path
from packages.logger import logger
from packages.timestamp import timestamp


# Get project absolute path
project_abs_path = absolute_path.get()
# Create log file
logs_file_path = logger.create_log_file(
    app_name='project-name', project_abs_path=project_abs_path
)
# Initiate logger
logger = logger.setup_app_logger(logger_name='', log_file_path=logs_file_path)


def main():

    logger.info('Start program...')

    current_timestamp = timestamp.get_current()

    logger.info('End program...')


if __name__ == '__main__':
    main()
