# PyNegEx

PyNegEx is a PIPY modular package based on Chapman's NegEx implementation. NegEx is a rule-based algorithm to detect assertion in clinical texts.

Motivation behind PyNegEx is to provide the community with a modern python packaing for the algorithm to guarantee easy usage and a space for better maintainability, e.g. add support for other languages.

## Requirements

Tested so far on:

- Python 3.8+

## Install

```sh
pip install pynegex
```

## Usage

```python
import pynegex

pynegex.run("patient hat kein Fieber", "Fieber", "cotik-de")
# ['negated', 'patient [PREN]hat kein[PREN] [NEGATED]Fieber[NEGATED]']
```

## Modifications

PyNegex uses the original implementation by Chapman with support for German (triggerset by Cotik etal 2016). PyNegEx includes hotfixes for known issues with the original implementation (for more details see [CHANGELOG](CHANGELOG))

## Credits & License

PyNegEx is released in compliance with the original licese of NegEx which is Python 2.5.4.

Furthermore, credits for the other languages support:

- German: Cotik et al 2016.

## CONTRIBUTIONS

Feel free to support this package by adding support for other languages.
