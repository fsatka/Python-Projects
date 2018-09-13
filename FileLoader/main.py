from FileLoader import FTPLoader
import parse_json as jp
import os
import time
from logging import Log
from multiprocessing import cpu_count, Queue, Process


def start_processes(parse_res, count_cpu_param=1):
    user = [parse_res.user["host"],
            parse_res.user["name"],
            parse_res.user["password"]]
    processes = []
    log = Log(os.path.dirname(os.path.abspath(__file__)))
    queue_of_paths = Queue()

    if not FTPLoader.check_login(*user, log):
        return

    for path in parse_res.paths:
        queue_of_paths.put(path)

    if queue_of_paths.qsize() < count_cpu_param:
        loader = FTPLoader(*user, log)
        loader.start_load(queue_of_paths)
    else:
        for i in range(count_cpu_param - 1):
            another_loader = FTPLoader(*user, log)

            # you can change Process to Thread and it will be work(don't forget import threading)
            process = Process(target=another_loader.start_load, args=(queue_of_paths, ))
            process.start()
            processes.append(process)

        loader = FTPLoader(*user, log)
        loader.start_load(queue_of_paths)


if __name__ == "__main__":
    parsing_res = jp.ParseJson("conf.json")
    if parsing_res.parsing_complete:
        count_cpu = cpu_count()
        start = time.time()
        start_processes(parsing_res, count_cpu)
        end = time.time()
        print(end - start)

