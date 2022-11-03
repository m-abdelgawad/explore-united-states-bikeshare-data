from .send_work_sms import send_work_sms


def send_wfp_sms(input_sheet_path):
    summary = send_work_sms(
        work_location='Premises',
        input_sheet_path=input_sheet_path)

    return summary