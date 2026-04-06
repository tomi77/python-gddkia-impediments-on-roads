# Impediments on roads provided by GDDKiA

Simple wrapper for a data about impediments on roads provided by GDDKiA.

## Installation

```
pip install gddkia-impediments-on-roads
```

## Usage

```python
from impediments import get_impediments

impediments = get_impediments()
```

## Tips

Data about impediments are changed infrequently. To speed up operations use some cache mechanism and refresh the data every hour.
