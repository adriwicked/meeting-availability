import unittest
from meeting_availability import (
    time_to_minutes,
    compare_times,
    merge_bounds,
    is_block_long_enough,    
    is_meeting_inside_bounds,
    get_available_time,
    clamp_meetings_by_bounds,
    get_available_time_blocks
)


class TestMeetingAvailability(unittest.TestCase):
    def test_string_time_is_correctly_parsed_to_minutes(self):
        self.assertEqual(time_to_minutes('08:30'), 510)

    def test_if_time_is_not_a_string_return_none(self):
        self.assertEqual(time_to_minutes(600), None)

    def test_if_compare_times_works_properly(self):
        self.assertEqual(compare_times('08:00', '09:30'), -90)
        self.assertEqual(compare_times('09:00', '08:45'), 15)
        self.assertEqual(compare_times('09:00', '09:00'), 0)

    def test_if_merge_bounds_works_properly(self):
        bounds1 = ['7:00', '20:00']
        bounds2 = ['9:30', '19:00']
        bounds3 = ['8:00', '18:00']

        self.assertEqual(merge_bounds(bounds1, bounds2), ['9:30', '19:00'])
        self.assertEqual(merge_bounds(bounds2, bounds3), ['9:30', '18:00'])

    def test_if_non_overlapping_bounds_returns_none(self):
        bounds4 = ['8:00', '13:00']
        bounds5 = ['14:00', '18:00']

        self.assertEqual(merge_bounds(bounds4, bounds5), None)

    def test_if_is_block_long_enough_works_properly(self):
        self.assertEqual(is_block_long_enough(['9:30', '10:00'], 30), True)
        self.assertEqual(is_block_long_enough(['10:00', '10:45'], 60), False)    

    def test_if_is_meeting_inside_bounds_works_properly(self):
        self.assertEqual(is_meeting_inside_bounds(['10:00', '11:00'], ['8:00', '12:00']), True)
        self.assertEqual(is_meeting_inside_bounds(['11:30', '12:30'], ['8:00', '12:00']), True)
        self.assertEqual(is_meeting_inside_bounds(['7:30', '9:00'], ['8:00', '12:00']), True)
        self.assertEqual(is_meeting_inside_bounds(['13:00', '14:00'], ['8:00', '12:00']), False)        

    def test_if_clamp_meetings_by_bounds_works_properly(self):
        meetings = [
            ['9:30', '10:30'],
            ['12:00', '13:00'],
            ['13:30', '15:00'],
            ['16:30', '18:00']
        ]
        bounds = ['11:00', '15:30']

        new_meetings = [
            ['12:00', '13:00'],
            ['13:30', '15:00']           
        ]

        self.assertEqual(clamp_meetings_by_bounds(meetings, bounds), new_meetings)

    def test_if_get_available_time_works_properly(self):
        meetings = [
            ['9:30', '10:30'],
            ['12:00', '15:00'],
            ['15:30', '18:00']
        ]
        bounds = ['8:00', '19:00']        

        self.assertEqual(
            get_available_time(meetings, bounds),
            [
                ['8:00', '9:30'],
                ['10:30', '12:00'],
                ['15:00', '15:30'],
                ['18:00', '19:00'],
            ]
        )

        meetings = [
            ['9:30', '10:30'],
            ['12:00', '15:00'],
            ['15:30', '18:00']
        ]
        bounds = ['8:00', '15:00']

        self.assertEqual(
            get_available_time(meetings, bounds),
            [
                ['8:00', '9:30'],
                ['10:30', '12:00']
            ]
        )

    def test_if_it_returns_available_time_blocks(self):
        calendar1 = {
            'meetings': [
                ['08:00', '08:30'],
                ['09:30', '10:00'],
                ['11:00', '12:00']                
            ],
            'bounds': ['8:00', '12:30']
            }

        calendar2 = {
            'meetings': [
                ['09:00', '10:00'],
                ['10:30', '12:00'],                
            ],
            'bounds': ['9:00', '13:00']
        } 

        meeting_duration = 30

        available_time_blocks = [
            ['10:00', '10:30'],
            ['12:00', '12:30']
        ]

        self.assertEqual(
            get_available_time_blocks(calendar1, calendar2, meeting_duration),
            available_time_blocks
        )

if __name__ == '__main__':
    unittest.main()
