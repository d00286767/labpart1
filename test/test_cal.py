from typing import Literal

import part1
import pytest

def test_calculate_inputs():
    #Test invalid inputs
    with pytest.raises(ValueError):
        part1.calculate_interest("jai")  
    with pytest.raises(ValueError):
        part1.calculate_interest(True)   
    with pytest.raises(ValueError):
        part1.calculate_interest(False)
    with pytest.raises(ValueError):
        part1.calculate_interest(-3)
    with pytest.raises(ValueError):
        part1.calculate_interest(-3.4)

#test interest calculations for various deposit amounts
@pytest.mark.parametrize("deposit, expected_interest", [
    (1000, 30.0),  
    (10000, 345.0), 
    (100000, 3940.0), 
    (150000, 5190.0)
])
def test_calculate_interest(deposit, expected_interest):
    assert part1.calculate_interest(deposit) == f"{expected_interest:.2f}"

