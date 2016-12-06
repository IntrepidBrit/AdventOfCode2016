import cProfile
import d5p2
from intrepid_calendar import read_input_data

if __name__ == "__main__":
    cProfile.run("d5p2.naive_hashthrash_me_a_password(read_input_data(5))")