import multiprocessing
import time 
# from app import run_server
from WebEngine import run_webengine

def run_server():
    import os
    os.system('python app.py')

def print_process(process1,process2):
    while(process1.is_alive()):
        pass
    process2.terminate()
if __name__ == "__main__":
    onGoingProcess = []
    server_process = multiprocessing.Process(name='server',target=run_server)
    onGoingProcess.append(server_process)
    server_process.start()
    webengine_process = multiprocessing.Process(name='webengine',target=run_webengine)
    onGoingProcess.append(webengine_process)
    webengine_process.start()
    ps = multiprocessing.Process(name='ps',target=print_process(webengine_process,server_process))
    ps.start()

    

