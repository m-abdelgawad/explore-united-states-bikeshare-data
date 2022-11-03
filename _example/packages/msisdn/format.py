def prepare_msisdn_format(mobile_number):
    if mobile_number[0] == '1':
        mobile_number = '20' + mobile_number
    elif mobile_number[0] == '0':
        mobile_number = '2' + mobile_number

    return mobile_number
