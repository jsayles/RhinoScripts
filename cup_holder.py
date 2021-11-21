import rhinoscriptsyntax as rs

BASE_DIAMETER = 74
TOP_DIAMETER = 76
INNER_DIAMETER = 70
HEIGHT = 45

# Build the outer shell
circle1 = rs.AddCircle((0,0,0), BASE_DIAMETER/2)
# plane1 = rs.AddPlanarSrf(circle1)
circle2 = rs.AddCircle((0,0,HEIGHT), TOP_DIAMETER/2)
# plane2 = rs.AddPlanarSrf(circle2)
outer_shell = rs.AddLoftSrf([circle1, circle2])
rs.CapPlanarHoles(outer_shell)

# Build our inner void
circle3 = rs.AddCircle((0,0,4), 70/2)
circle4 = rs.AddCircle((0,0,HEIGHT), 70/2)
# inner_void = rs.ExtrudeCurveStraight(circle3, (0,0,4), (0,0,HEIGHT))
inner_void = rs.AddLoftSrf([circle3, circle4])
rs.CapPlanarHoles(inner_void)

# Remove the inner void from the outer shell
rs.BooleanDifference(outer_shell, inner_void, delete_input=True)

# Clean up
rs.DeleteObjects([circle1, circle2, circle3, circle4])
