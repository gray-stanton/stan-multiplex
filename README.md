# stan-multiplex
Easy distribution of stan models and data for evaluation on heterogenous remote machines

Goal:
Take compiled cmdstan model, either pre-exported standump data files or possibly pandas 
dataframes, and a configuration YAML file which contains the info necessary to 
connect to remote machines, manage jobs/datafiles locally, push out to remote machines
fully over SSH, get statuses and retrieve evaluated models. All that should be
required of remote machines is ability to evalutate C++ code and run a python 
overseer. Batch vs Stream tranfer of datafiles and resulting samples, redundancy.
Once all code has been executed, some sort of hook for recombining samples
