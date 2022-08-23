# Constantine Quantum Technologies' RNG package

[![PyPi version](https://shields.io/pypi/v/cqt_rng)]()[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/CQTech-womanium-hackathon/Random-number-generation-using-boson-sampling---ORCA-Computing/blob/main/challenge/demo.ipynb)

This is `Constantine Quantum Technologies`'s solution to ORCA Computing's challenge `Random number generation using boson sampling`.

## Team

- Abdellah Tounsi
  [![](https://img.shields.io/badge/Abdellah-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/980795511927885844) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdellah.tounsi@umc.edu.dz) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abduhu)
- Amina Sadik
  [![](https://img.shields.io/badge/Amina-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/538380103722336283) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sadik.amina.mp@gmail.com) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Amouna133)
- Mohamed Messaoud Louamri
  [![](https://img.shields.io/badge/Mohamed-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/296402073262751744) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mm.louamri@gmail.com) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mmlouamri)
- Nacer eddine Belaloui
  [![](https://img.shields.io/badge/Nacer-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/980786019949490217) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:n.aityahia.belaloui@gmail.com) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Belaloui)
- Wafa Makhlouf
  [![](https://img.shields.io/badge/Wafa-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/996400056875876493) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:makhloufw98@gmail.com) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/wafamakhlouf)
- Zakaria Benhaddouche
  [![](https://img.shields.io/badge/Zakaria-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discordapp.com/users/1002915392601215016) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)]()

## Getting started

### Installation

To install the package, run:

```console
$ pip install cqt_rng
```

### Usage

To start generating random numbers, you need to pick an entropy source and a post-processor.
There are 3 simulated quantum entropy sources:

- `BosonSampler`
- `UniversalQCSampler`
- `ShiSFSampler`

And 2 real quantum entropy sources:

- `BorealisSampler`
- `IBMQSampler`

We also implemented two postprocessors:

- `VonNeumannPP`
- `CQTPP`

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

### More on RNG

An in-depth explanation of why we need RNG, the theory behind it, and what the package does can be found in the `challenge/demo.ipynb` notebook (which you can launch directly on google colab by clicking the button below).

<center markdown="1">

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/CQTech-womanium-hackathon/Random-number-generation-using-boson-sampling---ORCA-Computing/blob/main/challenge/demo.ipynb)

</center>
