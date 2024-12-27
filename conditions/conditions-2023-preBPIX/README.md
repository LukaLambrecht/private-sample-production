# Processing sequence with 2023-preBPIX conditions

The recommended processing sequence, correct global tags, etc., can be retrieved from [this PdmV TWiki](https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun3Analysis#Recipes_for_Run3Summer23_and_Run)

The sequence here corresponds to MiniAOD v4 and NanoAOD v12.

Customizations:
- Monitoring in the form of `--customise Configuration/DataProcessing/Utils.addMonitoring` was added to every step.
- The random number seed is set as follows (in the LHE/GEN-SIM step): `--customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${SEED})"\\nprocess.source.firstLuminosityBlock="cms.untracked.uint32(${JOBNUM})"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(${EVENTS})"`
