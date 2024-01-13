# gen-Run3Summer23
Scripts for CRAB private production of Run2Summer23 samples

- Use `CMSSW_13_0_14`
- Put the fragments in the `step1/fragments/` in `$CMSSW_BASE/src/Configuration/GenProduction/python/`.
- Do `scram b; scram b python` from `$CMSSW_BASE/src` to compile the fragments
- Use `step1/cmsDriver.py`, together with the lines in `cmsDriver.txt`, to generate the config file for step1
- Use `step1/crabConfig.py` to submit CRAB jobs for that config file. The script tries to be a bit smart about file naming, but it may fail; fix it if it happens.
- Use`step2/crabConfig.py` to submit CRAB jobs for the `DIGIRAWHLT.py` config file, running over the dataset produced in step1. Again, the script tries to be a bit smart about file naming, but it may fail; fix it if it happens. In particular, notice that there is my surname hardcoded in this CRAB config -- this is because private datasets have the username of their producer encoded in their names!
- For step2, `config.JobType.maxMemoryMB = 5000` is important. The job will fail with less memory.
