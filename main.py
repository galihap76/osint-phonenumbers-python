# Import modules
import argparse, phonenumbers
from phonenumbers import timezone

# Adding an argument for the phone number
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', type=str, help='set the phone number')
args = parser.parse_args()

# Main function
def main():

    # Check if the user adds the argument in the terminal
    if args.number:
        target_number = phonenumbers.parse(args.number)  # Parsing the given phone number
        time_zone = timezone.time_zones_for_number(target_number)  # Getting the time zone

        # Displaying the time zone
        print("=====[OUTPUT]=====")
        print(f"Time zone : {time_zone}") 

# Run the code in terminal
if __name__ == "__main__":
    main()
