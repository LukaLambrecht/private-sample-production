python3 check_disk.py \
    -d /Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX \
    -o ../../conditions/conditions-2022-preEE/pileup_files_on_disk.txt $@

python3 check_disk.py \
    -d /Neutrino_E-10_gun/Run3Summer21PrePremix-Summer22_124X_mcRun3_2022_realistic_v11-v2/PREMIX \
    -o ../../conditions/conditions-2022-postEE/pileup_files_on_disk.txt $@

python3 check_disk.py \
    -d /Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23_130X_mcRun3_2023_realistic_v13-v1/PREMIX \
    -o ../../conditions/conditions-2023-preBPIX/pileup_files_on_disk.txt $@

python3 check_disk.py \
    -d /Neutrino_E-10_gun/Run3Summer21PrePremix-Summer23BPix_130X_mcRun3_2023_realistic_postBPix_v1-v1/PREMIX \
    -o ../../conditions/conditions-2023-postBPIX/pileup_files_on_disk.txt $@
