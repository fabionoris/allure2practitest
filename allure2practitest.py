import csv
import datetime

# Filenames
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.csv"

# Test Automation Report
REPORT_TEST_STATUS = 0
REPORT_START_TIME = 1
REPORT_STOP_TIME = 2
REPORT_FEATURE_SET = 6
REPORT_TEST_CASE_NAME = 8

# Test Automation Prefix
PREFIX = ""

# PractiTest Fields
PRACTITEST_NAME = ""
PRACTITEST_DESCRIPTION = ""
PRACTITEST_STATUS = ""
PRACTITEST_AUTHOR = ""
PRACTITEST_TAGS = ""
PRACTITEST_PRECONDITIONS = ""
PRACTITEST_REQUIREMENTS = ""
PRACTITEST_DURATION = ""
PRACTITEST_FEATURE_SET = ""
PRACTITEST_FEATURES = ""
PRACTITEST_SPRINT = ""
PRACTITEST_SYSTEM = ""
PRACTITEST_ENVIRONMENT = ""
PRACTITEST_STEP_NAME = ""
PRACTITEST_STEP_DESCRIPTION = ""
PRACTITEST_EXPECTED_RESULT = ""
PRACTITEST_STEP_POSITION = ""
PRACTITEST_EXPECTED_RESPONSE_CODE = ""
PRACTITEST_TEST_RESULT = ""
PRACTITEST_TO_BE_AUTOMATED = ""
PRACTITEST_AUTOMATED = ""


def modify_csv(file_path):

  with open(file_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    with open(OUTPUT_FILENAME, "w", newline='') as new_csvfile:
      writer = csv.writer(new_csvfile)
      writer.writerow(["Name", "Description", "Status",
        "Author", "Tags", "Test Preconditions",
        "Linked Requirements","Estimated Duration", "Feature Set",
        "Features", "Sprint", "System",
        "Environment", "Step Name", "Step Description",
        "Step Expected Result", "Step Position", "Expected Response Code",
        "Test Result", "To Be Automated", "Automated"])

      for row in reader:

        name = row[REPORT_TEST_CASE_NAME]

        testclass = row[REPORT_FEATURE_SET]
        testclass = testclass.replace(PREFIX, "")
        testclass = testclass.replace(".", " ")
        package, testclass = split_string_at_first_uppercase_character(testclass)
        package = default_formatter(capitalize_first_letter(package))
        testclass = default_formatter(add_space_before_uppercase(testclass))

        esitmated_duration = difference_in_seconds(row[REPORT_START_TIME], row[REPORT_STOP_TIME])

        test_result = "OK" if row[REPORT_TEST_STATUS] == "passed" else "KO"

        writer.writerow([name, name + " in " + testclass, PRACTITEST_STATUS,
          PRACTITEST_AUTHOR, PRACTITEST_TAGS, "The user is in the " + package + " page",
          PRACTITEST_REQUIREMENTS, esitmated_duration, package,
          testclass, PRACTITEST_SPRINT, PRACTITEST_SYSTEM,
          PRACTITEST_ENVIRONMENT, name, PRACTITEST_STEP_DESCRIPTION,
          PRACTITEST_EXPECTED_RESULT, PRACTITEST_STEP_POSITION, PRACTITEST_EXPECTED_RESPONSE_CODE,
          test_result, PRACTITEST_TO_BE_AUTOMATED, PRACTITEST_AUTOMATED])


def add_space_before_uppercase(string):
  """
  Adds a space before each uppercase character in a string,
  except for the first letter.
  """
  first_character = string[0]
  string = string[1:]
  new_string = ""
  for c in string:
    if c.isupper():
      new_string += " "
    new_string += c
  return first_character + new_string


def capitalize_first_letter(string):
  """
  Capitalizes the first letter of each word in a string.
  """
  words = string.split()
  for i, word in enumerate(words):
    words[i] = word[0].upper() + word[1:]
  new_string = " ".join(words)
  return new_string


def split_string_at_first_uppercase_character(string):
  """
  Splits a string at the first occurrence of an uppercase character.
  """
  pos = string.find(next((c for c in string if c.isupper()), None))
  if pos == -1:
    return (string, "")
  else:
    return (string[:pos], string[pos:])


def difference_in_seconds(date_1, date_2):
  date_1 = datetime.datetime.strptime(date_1, '%a %b %d %H:%M:%S UTC %Y')
  date_2 = datetime.datetime.strptime(date_2, '%a %b %d %H:%M:%S UTC %Y')
  return (date_2 - date_1).total_seconds()


def default_formatter(string):
  string = string.replace(" Test", "")
  return string


if __name__ == "__main__":
  file_path = INPUT_FILENAME
  modify_csv(file_path)
