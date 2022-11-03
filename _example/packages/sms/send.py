# Import needed libraries
import cx_Oracle


def send_sms(sender, msisdn, message):

    # Database credentials
    hostname = "10.30.145.38"
    username = "SMPP1"
    password = "SMPP1"
    port = "1522"
    service_name = "HQSMPP2"

    # Connection string to connect to the database
    connection_string = "{}/{}@{}:{}/{}".format(username,
                                                password,
                                                hostname,
                                                port,
                                                service_name)

    # Establish the database connection
    connection = cx_Oracle.connect(connection_string)

    # Obtain a cursor
    cursor = connection.cursor()

    # Execute SEND SMS procedure
    cursor.callproc(
        'SENDSMS',
        ('TIBCO_Reg', sender, msisdn, message, '0', '2', '0')
    )


# Test the package
if __name__ == '__main__':
    send_sms(sender="SAS", msisdn="201069052620", message="Automation test")
