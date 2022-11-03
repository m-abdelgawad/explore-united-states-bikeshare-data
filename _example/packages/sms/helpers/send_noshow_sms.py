import logging
logger = logging.getLogger('')


import datetime
import traceback

from packages.SAS.messages import get_noshow_message
from packages.dataframe.helpers.clean_df import clean_df
from packages.msisdn.format import prepare_msisdn_format
from packages.sms.send import send_sms


def send_noshow_sms(input_sheet_path):
    logger = logging.getLogger('')

    sender_name = 'NoShow'

    df = clean_df(sheet_path=input_sheet_path,
                  cols_types_dict={'Shift Date': datetime.datetime,
                                   'Mobile Number': str})

    # Rename Shift Date column
    df.rename(columns={'Shift Date': 'Date'}, inplace=True)

    # Convert date to the format of "Sat 30-Jul".
    df['Date'] = df['Date'].dt.strftime('%a %d-%b')

    # Get unique mobile numbers
    mobile_numbers_list = df['Mobile Number'].unique()
    msisdns_count = len(mobile_numbers_list)

    # Define counters for success and failed numbers
    success_counter = 0
    fail_counter = 0

    logger.info("Start processing MSISDNs...\n")

    # Loop over unique mobile numbers
    for idx, mobile_number in enumerate(mobile_numbers_list):

        logger.info("processing: {0} (#{1} out of {2})".format(
            mobile_number, idx + 1, msisdns_count))

        try:

            # Initiate work schedule
            noshow_dates = ''

            # Loop over the rows of the same mobile number
            filtered_df = df[df['Mobile Number'] == mobile_number]

            for index, row in filtered_df.iterrows():
                row_date = row['Date']
                noshow_dates += '{0}\n'.format(row_date)

            # Prepare mobile number format
            formatted_msisdn = prepare_msisdn_format \
                (mobile_number=mobile_number)

            no_show_message = get_noshow_message(
                date=noshow_dates
            )

            # Send the message
            send_sms(
                sender=sender_name,
                msisdn=formatted_msisdn,
                message=no_show_message
            )
            
            success_counter += 1

        except Exception as e:
            fail_counter += 1
            logger.error("Error Message: {0}".format(e))
            logger.error(
                "Error Traceback: \n{0}".format(traceback.format_exc()))

    logger.info("Finished processing all MSISDNs.\n")
    logger.info(
        "Total success = {0} out of {1}".format(success_counter, msisdns_count))
    logger.info(
        "Total fails = {0} out of {1}".format(fail_counter, msisdns_count))

    return {'total': msisdns_count, 'success': success_counter,
            'fails': fail_counter}
