import yaml
from packages.project import absolute_path
from packages.logger import logger
from packages.timestamp import timestamp


def main():

    # Initiate logger
    logs_file_path = logger.create_log_file(
        app_name='project-name', project_abs_path=absolute_path.get()
    )
    log = logger.setup_app_logger(logger_name='', log_file_path=logs_file_path)

    log.info('Start program execution')

    # Import configurations
    with open('./conf.yaml') as config_file:
        conf = yaml.safe_load(config_file)

    # Start testing logger
    log.info('Configuration Username: ' + conf['account']['username'])
    log.info('Configuration Password: ' + conf['account']['password'])
    current_timestamp = timestamp.get_current()
    log.info('Current Timestamp: ' + current_timestamp)
    # Finished testing logger

    log.info('Finished program execution')


if __name__ == '__main__':
    main()
