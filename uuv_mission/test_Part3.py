from dynamic import Mission

# Test the from_csv method with the test CSV file
#mission = Mission.from_csv(
#    "/Users/jaihyunkim/Eng/B1_Repos/b1-coding-practical-mt24/data/mission.csv"
#)

# For use on other machines:
import os
abs_dir = os.path.dirname(os.path.abspath(__file__))
abs_dir2 = os.path.dirname(abs_dir)
csv_dir = abs_dir2 + "/data/mission.csv"
mission = Mission.from_csv(csv_dir)

# Print the contents to check if they are correctly loaded
print("Reference:", mission.reference)
print("Cave Height:", mission.cave_height)
print("Cave Depth:", mission.cave_depth)
