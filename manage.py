from multiprocessing import Manager
from app import create_app



app = create_app("development")








if __name__ == "__main__":
    Manager.run()