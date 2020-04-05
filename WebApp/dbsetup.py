import os
import argparse
import glob
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-f','--force', nargs='?', const=True, type=bool)



def init():
    if glob.glob("*.db"):
        print("Database already exists")
        return
        
    print("Initializing new db")
    os.system('flask db init')
    os.system('flask db migrate')
    os.system('flask db upgrade')

def force():
    print("Removing old db ")
    if os.path.exists('./migrations'):
        shutil.rmtree('./migrations')
    if os.path.exists('./app.db'):
        os.remove('./app.db')
    print("Initializing new db")
    os.system('flask db init')
    os.system('flask db migrate')
    os.system('flask db upgrade')

args = parser.parse_args()
if __name__ == "__main__":
    if args.force:
        print("Force created new db")
        force()
    else:
        print("Creating new db")
        init()
