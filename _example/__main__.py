# Setup logger
from packages.logger.setup import setup_app_logger, create_log_file
from packages.project.absolute_path import get_abs_path
# Get project absolute path
project_abs_path = get_abs_path()
# Create log file
logs_file_path = create_log_file(
    app_name='SAS', project_abs_path=project_abs_path
)
# Initiate logger
logger = setup_app_logger(logger_name='', log_file_path=logs_file_path)


import os
import shutil
import traceback


from packages.arguments.get import get_input_args
from packages.sms.helpers.send_wfh_sms import send_wfh_sms
from packages.sms.helpers.send_wfp_sms import send_wfp_sms
from packages.sms.helpers.send_noshow_sms import send_noshow_sms
from packages.timestamp.current import get_current_timestamp
from packages.mail import mail


def main():

    logger.info('Start executing SAS project')

    # get current timestamp
    current_timestamp = get_current_timestamp()

    # Get running arguments
    args = get_input_args()

    # Message type
    message_type = args.message_type
    logger.info('Message Type: {0}'.format(message_type))

    # Sheet path
    sheet_path = args.sheet_path
    logger.info('Sheet Path: {0}'.format(sheet_path))
    logger.info('Sheet Name: {0}'.format(sheet_path.split('/')[-1]))

    if message_type == 'WFH':
        # Send work from home messages
        summary = send_wfh_sms(input_sheet_path=sheet_path)
        archive_folder_path = os.path.join(project_abs_path,
                                           'data/input/from_home/archive')

    elif message_type == 'Premises':
        # Send work from premises messages
        summary = send_wfp_sms(input_sheet_path=sheet_path)
        archive_folder_path = os.path.join(project_abs_path,
                                           'data/input/from_premises/archive')

    elif message_type == 'Noshow':
        # Send No-Show messages
        summary = send_noshow_sms(input_sheet_path=sheet_path)
        archive_folder_path = os.path.join(project_abs_path,
                                           'data/input/no_show/archive')

    else:
        print("Please try again and enter valid arguments")
        exit()

    # rename the input sheet with current timestamp
    archive_file_name = message_type + '_' + current_timestamp + '.xlsx'

    # Archived file path
    archived_file_path = os.path.join(archive_folder_path, archive_file_name)

    # Move input file to archive folder
    shutil.move(sheet_path, archived_file_path)

    # Construct mail subject
    mail_subject = "SAS | {0} | {1} Fails | {2} Success | {3} Total".format(
        message_type, summary['fails'], summary['success'], summary['total']
    )

    # Send execution info mail
    mail.send(
        sender_mail='ITAutomation@vodafone.com.eg',
        receivers_list=[
            'mohamed.aboatta@vodafone.com.eg',
            'mohamed.salemmahmoud1@vodafone.com.eg',
        ],
        subject=mail_subject,
        body='Kindly find attached the logs of execution.',
        attachs_list=[logs_file_path],
    )

    logger.info('Finished executing SAS project')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error("Error Message: {0}".format(e))
        logger.error("Error Traceback: \n{0}".format(traceback.format_exc()))
