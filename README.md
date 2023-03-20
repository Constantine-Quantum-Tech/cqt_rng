<img align="right" width="70" src="https://raw.githubusercontent.com/Constantine-Quantum-Tech/tqsim/main/images/cqtech_logo.png" alt="CQTech">

# cqt_rng

[![Version](https://img.shields.io/pypi/v/cqt_rng?style=flat-square)](https://pypi.org/project/cqt_rng/) [![License](https://img.shields.io/pypi/dm/cqt_rng?style=flat-square)](https://pypi.org/project/cqt_rng/) [![License](https://img.shields.io/github/license/Constantine-Quantum-Tech/cqt_rng?style=flat-square)](LICENSE)

cqt_rng is an open-source package designed to generate random numbers using quantum entropy sources. This library leverages the principles of quantum mechanics to generate truly random numbers, which are fundamental to many areas of science and technology, including cryptography, simulation, and modeling.

## Installation

You can install cqt_rng from pip using

```bash
pip install --upgrade cqt_rng
```

## Usage

To start generating random numbers, you need to pick an entropy source and a post-processor.
There are 3 simulated quantum entropy sources:

- `BosonSampler`
- `UniversalQCSampler`
- `ShiSFSampler`

And 2 real quantum entropy sources:

- `BorealisSampler`
- `IBMQSampler`

We also implemented three postprocessors:

- `VonNeumannPP`
- `CQTPP`
- `NoPostProcess`

Once you have chosen you entropy source and post-processor, you just need 2 lines of code (without counting the imports 😅) to generate random numbers:

```python
from cqt_rng import RNG
from cqt_rng.post_processors import VonNeumannPP
from cqt_rng.entropy_sources import BosonSampler

rng = RNG(BosonSampler(), VonNeumannPP())
rng.generate(length = 1024)
```

You can also use your custom entropy sources by implementing them as subclasses of the abstract class `EntropySource`, and also implement your own postprocessors as subclasses of the abstract class `PostProcessor`.

_For more example, please refer to the [documentation]()._

## License

Copyright © 2022-2023, [Constantine Quantum Technologies](https://cqtech.org). Released under the [Apache License 2.0](LICENSE).
