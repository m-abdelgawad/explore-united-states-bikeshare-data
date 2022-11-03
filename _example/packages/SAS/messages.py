def get_schedule_message(work_location, work_schedule):
    """

    :param date:
    :type date:
    :param work_location: either 'Home' or 'Premises'
    :type work_location: str
    :param time:
    :type time:
    :return:
    :rtype:
    """
    message = "Our Hero,\nThis is your next week schedule from {},\
            \n{}Wishing you a cheerful week :)\nWF team".format(
        work_location, work_schedule
    )
    return message


def get_noshow_message(date):

    message = "Dear Colleague,\nHurry up and update the below NOSHOW days "\
        "to avoid Annual Leaves or Salary deduction. \n{}WF team".format(date)
    return message


if __name__ == "__main__":

    wfh_message = get_schedule_message(
        date='Tue 31-May',
        work_location='Home',
        time='19:15'
    )
    print("\nWFH Message:\n", wfh_message)

    premises_message = get_schedule_message(
        date='Tue 31-May',
        work_location='Premises',
        time='19:15'
    )
    print("\nPremises Message:\n", premises_message)

    noshow_message = get_noshow_message(
        date='16-May-2022'
    )
    print("\nNOSHOW Message:\n", noshow_message)
