from tariffs_modules import Factory
import argparse
import cProfile
import pstats
import os
import shutil
import platform
import datetime
import gc
from memory_profiler import memory_usage
import json

# Workaround to make pstats print sub milliseconds time
# Found here: https://gist.github.com/romuald/0346c76cfbbbceb3e4d1
def f8(x):
    ret = "%8.3f" % x
    if ret != '   0.000':
        return ret
    return "%6dµs" % (x * 1000000)


pstats.f8 = f8


def profile_function(fn, output):
    prof = cProfile.Profile()
    prof.runcall(fn)
    prof.dump_stats(output)

    with open(output, 'w') as profile_file:
        stats = pstats.Stats(prof, stream=profile_file)
        stats.sort_stats('cumulative')
        stats.print_stats()


def profile_memory_function(fn, output):
    gc.collect()
    with open(output, 'w') as f:
        f.write(json.dumps(memory_usage(fn, interval=0.001)))


def profile_module(module, output, iterations=10000, memory=True):
    # CPU Profiling
    profile_function(module.__init__, os.path.join(output, "init.txt"))
    profile_function(module.predict, os.path.join(output, "predict.txt"))

    # RAM Profiling
    if memory:
        profile_memory_function(module.predict, os.path.join(output, "predict_memory.txt"))

    # Multiple launch Benchmark
    print(module.loop(iterations))


if __name__ == "__main__":

    print("Current platform:", platform.python_implementation())

    parser = argparse.ArgumentParser()
    parser.add_argument("--outputdir", help="output dir")
    args = parser.parse_args()
    args.outputdir = os.path.join(args.outputdir, datetime.datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))

    if os.path.exists(args.outputdir):
        shutil.rmtree(args.outputdir)
    os.makedirs(args.outputdir)

    for module_name in Factory.list_modules():
        m = Factory.create(module_name)

        module_profile_path = os.path.join(args.outputdir, module_name)
        os.makedirs(module_profile_path)

        profile_module(m, module_profile_path)
