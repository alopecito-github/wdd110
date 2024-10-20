from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings,reynolds_number,pressure_loss_from_pipe_reduction

from pytest import approx
import pytest

def test_water_column_height():
    assert water_column_height(0.0,0.0) == 0.0
    assert water_column_height(0.0,10.0) == 7.5
    assert water_column_height(25.0,0.0) == 25.0
    assert water_column_height(48.3,12.8) == 57.9

def test_pressure_gain():
    # test of first part of the assignment
    # assert pressure_gain_from_water_height(30.2) == approx(295.628, 0.001)
    # assert pressure_gain_from_water_height(50.0) == approx(489.450, 0.001)
    #exciding requirements test
    assert pressure_gain_from_water_height(0,9.80665,998.2) == approx(0.00, 0.001)
    assert pressure_gain_from_water_height(30.2,9.80665,998.2) == approx(295.628, 0.001)
    assert pressure_gain_from_water_height(50,9.80665,998.2) == approx(489.450, 0.001)


def test_pressure_loss():
    assert pressure_loss_from_pipe(0.048692,0.00,0.018,1.75) == approx(0.000,0.001)
    assert pressure_loss_from_pipe(0.048692,200.0,0.000,1.75) == approx(0.000,0.001)
    assert pressure_loss_from_pipe(0.048692,200.0,0.018,0.00) == approx(0.000,0.001)
    assert pressure_loss_from_pipe(0.048692,200.00,0.018,1.75) == approx(-113.008,0.001)
    assert pressure_loss_from_pipe(0.048692,200.00,0.018,1.65) == approx(-100.462,0.001)
    assert pressure_loss_from_pipe(0.286870,1000.00,0.013,1.65) == approx(-61.576,0.001)
    assert pressure_loss_from_pipe(0.286870,1800.75,0.013,1.65) == approx(-110.884,0.001)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00,3) == approx(0.000,0.001)
    assert pressure_loss_from_fittings(1.65,0) == approx(0.000,0.001)
    assert pressure_loss_from_fittings(1.65,2) == approx(-0.109,0.001)
    assert pressure_loss_from_fittings(1.75,2) == approx(-0.122,0.001)
    assert pressure_loss_from_fittings(1.75,5) == approx(-0.306,0.001)

def test_reynolds_number():
    #previous assigment test
    # assert reynolds_number(0.048692,0.00) == approx(0,1)
    # assert reynolds_number(0.048692,1.65) == approx(80069,1)
    # assert reynolds_number(0.048692,1.75) == approx(84922,1)
    # assert reynolds_number(0.286870,1.65) == approx(471729,1)
    # assert reynolds_number(0.286870,1.75) == approx(500318,1)
    assert reynolds_number(0.048692,0.00,0.0010016) == approx(0,1)
    assert reynolds_number(0.048692,1.65,0.0010016) == approx(80069,1)
    assert reynolds_number(0.048692,1.75,0.0010016) == approx(84922,1)
    assert reynolds_number(0.286870,1.65,0.0010016) == approx(471729,1)
    assert reynolds_number(0.286870,1.75,0.0010016) == approx(500318,1)


def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687,0.00,1,0.048692 ) == approx(0.000,0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.65,471729,0.048692) == approx(-163.744,0.001)
    assert pressure_loss_from_pipe_reduction(0.28687,1.75,500318,0.048692) == approx(-184.182,0.001)


     
	
	

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])