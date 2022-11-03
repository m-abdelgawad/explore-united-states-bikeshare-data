from .send_work_sms import send_work_sms


def send_wfh_sms(input_sheet_path):
    summary = send_work_sms(
        work_location='Home',
        input_sheet_path=input_sheet_path)
    
    return summary
