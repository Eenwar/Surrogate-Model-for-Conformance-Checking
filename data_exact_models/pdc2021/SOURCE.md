# Where this corpus comes from

These archives are the Process Discovery Contest 2021 collection, mirrored here
unchanged so that the experiment is self-contained.

> Verbeek, H. M. W. (2021). *Process Discovery Contest 2021*.
> 4TU.ResearchData. https://doi.org/10.4121/16803232

**License: CC0 1.0 Universal** (public domain dedication),
https://creativecommons.org/publicdomain/zero/1.0/

CC0 places no condition on redistribution. The citation above is given because
it is the right thing to do, not because the license demands it.

| Archive | Contents | Format |
|---|---|---|
| `Models.zip` | 96 workflow nets | PNML |
| `TrainingLogs.zip` | 480 training logs | IEEE XES |
| `GroundTruthLogs.zip` | 96 ground-truth logs | IEEE XES |

`readme.txt` is the description shipped with the dataset. It explains the
six-digit configuration codes: each digit switches one construct on or off,
in the order dependent tasks, loops, OR constructs, routing constructs,
optional tasks, duplicate tasks.

The contest also publishes 96 test logs. The experiment does not use them, so
they are not mirrored here; they are in the 4TU record.

Run `prepare_data.py` from the repository root to unpack all three.
