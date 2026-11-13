"""Unpack the PDC 2021 corpus into the layout the notebook expects.

The three archives ship as distributed by 4TU.ResearchData. They are flat:
the files sit at the root of each archive, with no enclosing folder. This
script gives each one its own folder, so that the notebook finds:

    data_exact_models/pdc2021/Models/pdc2021_<cfg>.pnml
    data_exact_models/pdc2021/TrainingLogs/pdc2021_<cfg>0.xes
    data_exact_models/pdc2021/GroundTruthLogs/pdc2021_<cfg>.xes

Run it once, from the repository root:

    python prepare_data.py

It is safe to run again: an archive whose folder already holds the expected
number of files is skipped rather than re-extracted.
"""

import os
import sys
import zipfile

PDC = os.path.join("data_exact_models", "pdc2021")

# archive -> (folder it fills, how many files that folder should end up with)
ARCHIVES = {
    "Models.zip": ("Models", 96),
    "TrainingLogs.zip": ("TrainingLogs", 480),
    "GroundTruthLogs.zip": ("GroundTruthLogs", 96),
}


def count(folder):
    if not os.path.isdir(folder):
        return 0
    return sum(len(files) for _, _, files in os.walk(folder))


def main():
    if not os.path.isdir(PDC):
        sys.exit("%s not found. Run this from the repository root." % PDC)

    for name, (folder, expected) in ARCHIVES.items():
        archive = os.path.join(PDC, name)
        target = os.path.join(PDC, folder)
        if not os.path.isfile(archive):
            sys.exit("missing archive: %s" % archive)

        have = count(target)
        if have == expected:
            print("%-20s already unpacked, %d files" % (folder, have))
            continue
        if have:
            print("%-20s has %d files, expected %d: re-extracting"
                  % (folder, have, expected))

        print("%-20s extracting %s ..." % (folder, name))
        with zipfile.ZipFile(archive) as z:
            # into target, not into PDC: the archives carry no folder of
            # their own and would otherwise land side by side in pdc2021/.
            z.extractall(target)

        have = count(target)
        if have != expected:
            sys.exit("%s holds %d files after extraction, expected %d"
                     % (target, have, expected))
        print("%-20s %d files" % (folder, have))

    print("\nCorpus ready. Open poisson_conformance_bench.ipynb from here.")


if __name__ == "__main__":
    main()
