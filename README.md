# Meeting Availability

This module allows you to know available time blocks for two people to meet.

## Installation

```
$ pip install meeting_availability
```

## Usage

```python
from meeting_availability import get_available_time_blocks

calendar1 = {
  'meetings': [
    ['09:00', '10:30'],
    ['10:30', '11:30'],
    ['12:00', '13:00'],
    ['16:00', '18:00']
  ],
  'bounds': ['8:00', '20:00']
}

calendar2 = {
  'meetings': [
    ['10:00', '11:30'],
    ['12:30', '14:30'],
    ['14:30', '15:00'],
    ['16:00', '17:00']
  ],
  'bounds': ['8:30', '19:30']
} 

meeting_duration = 35

available_time_blocks = get_available_time_blocks(
    calendar1,
    calendar2,
    meeting_duration
)

print(available_time_blocks)

# prints
# [['15:00', '16:00'], ['18:00', '19:30']]
```

## Testing locally

Clone the repository:

```
$ git clone https://github.com/adriwicked/meeting-availability.git
```

Run the tests from inside the project:

```
$ cd meeting-availability
$ python -m unittest discover -s . -p "*_test.py"
```