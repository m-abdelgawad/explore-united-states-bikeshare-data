import argparse


def get_input_args():
    """
        Retrieves and parses the 2 command line arguments provided by the user
        when they run the program from a terminal window.
        Command Line Arguments:
          1. Message type as --type
          2. Contacts list file path as --path
        This function returns these arguments as an ArgumentParser object.
        """

    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 2 command line arguments
    parser.add_argument('--type', type=str, dest='message_type',
                        help='Message type: "WFH", "Premises", or "Noshow".')

    parser.add_argument('--path', type=str, dest='sheet_path',
                        help='The path to contacts list sheet.')

    # Replace None with parser.parse_args() parsed argument collection that
    # you created with this function
    return parser.parse_args()
