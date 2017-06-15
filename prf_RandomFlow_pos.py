"""import profile
import re

def RandomFlower():
    
    
if __name__ == '__main__':
    profile.run('RandomFlower')
"""
def RandomFlower():
    import RandomFlow_pos

if __name__ == '__main__':
    import profile, pstats
    profile.run("RandomFlower()", "{}.profile".format(__file__))
    s = pstats.Stats("{}.profile".format(__file__))
    s.strip_dirs()
    s.sort_stats("time").print_stats(10)
