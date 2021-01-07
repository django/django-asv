## Django ASV


Benchmarks for Django using [asv](https://asv.readthedocs.io/en/stable/)

Currently, only a small sample of Djangobench benchmarks have been migrated to the asv format. 

Running the benchmarks should be as "simple" as cloning the repo, installing the requirements 
into a new virtual env, and running `asv run` from the command prompt.

CPU isolation is also imporant -- use the --cpu-affinity flag for this. 
