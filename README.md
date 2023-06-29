# PyNegEx

PyNegEx is a PyPI modular package based on Chapman's NegEx implementation. NegEx is a rule-based algorithm to detect assertion in clinical texts.

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

pynegex.run(text="patient hat kein Fieber",
            ent_tag="Fieber",
            triggerset_name="cotik-de",
            )
# ['negated', 'patient [PREN]hat kein[PREN] [NEGATED]Fieber[NEGATED]']
```

Supported languages are specificed with `triggerset_name`:

- `'en'` or `'chapman-en'` for English
- `'de'` or `'cotik-de'` for German

Speculation is enabled by default, but you can change it by passing `speculation=False`.

## Modifications

PyNegex uses the original implementation by Chapman with support for German (triggerset by Cotik etal 2016). PyNegEx includes hotfixes for known issues with the original implementation (for more details see [CHANGELOG](CHANGELOG))

## Credits & License

PyNegEx contains code parts that are released in compliance with their original license.
These code parts are anything originated from original distirbuted negex repo.

Furthermore, credits for the other languages support:

- German: Cotik et al 2016.

## CONTRIBUTIONS

Feel free to support this package by adding support for other languages.
