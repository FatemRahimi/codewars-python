# You will be given a string (map) featuring a cat "C" and a mouse "m". The rest of the string will be made up of dots (".") The cat can move the given number of moves up, down, left or right, but not diagonally.

# You need to find out if the cat can catch the mouse from it's current position and return "Caught!" or "Escaped!" respectively.

# Finally, if one of two animals are not present, return "boring without two animals".

# Examples
# moves = 5

# map =
# ..C......
# .........
# ....m....

# returns "Caught!" because the cat can catch the mouse in 4 moves
# moves = 5

# map =
# .C.......
# .........
# ......m..

# returns "Escaped!" because the cat cannot catch the mouse in  5 moves

# solution


def cat_mouse(map_, moves):
    if 'C' not in map_ or 'm' not in map_:
        return 'boring without two animals'
    
    for row, line in enumerate(map_.splitlines()):
        if 'C' in line:
            cat = row, line.index('C')
        if 'm' in line:
            mouse = row, line.index('m')
    
    distance = abs(cat[0] - mouse[0]) + abs(cat[1] - mouse[1])
    
    return 'Caught!' if distance <= moves else 'Escaped!'


# test
from textwrap import dedent

import codewars_test as test
from solution import cat_mouse


@test.describe("Sample Tests")
def sample_tests():
    @test.it("Caught!")
    def _():
        map_ = dedent(
            """\
            ..C......
            .........
            ....m...."""
        )
        moves = 5
        test.assert_equals(cat_mouse(map_, moves), "Caught!", f"map_:\n{map_}\n\nmoves:\n{moves}\n\nFailed")

    @test.it("Escaped!")
    def _():
        map_ = dedent(
            """\
            .C.......
            .........
            ......m.."""
        )
        moves = 5
        test.assert_equals(cat_mouse(map_, moves), "Escaped!", f"map_:\n{map_}\n\nmoves:\n{moves}\n\nFailed")

    @test.it("boring without two animals")
    def _():
        map_ = dedent(
            """\
            ..C......
            .........
            ........."""
        )
        moves = 5
        test.assert_equals(cat_mouse(map_, 5), "boring without two animals", f"map_:\n{map_}\n\nmoves:\n{moves}\n\nFailed")
