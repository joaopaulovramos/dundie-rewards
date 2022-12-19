import os


TEST_PATH = os.path.dirname(__file__)
print(TEST_PATH)
PEOPLE_FILE = os.path.join(TEST_PATH.replace("\\", "/"), "assets/people.csv")
