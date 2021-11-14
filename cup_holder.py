import rhinoscriptsyntax as rs

BASE_DIAMETER = 74
TOP_DIAMETER = 76
INNER_DIAMETER = 70
HEIGHT = 45

# Build the outer shell
circle1 = rs.AddCircle((0,0,0), BASE_DIAMETER/2)
plane1 = rs.AddPlanarSrf(circle1)
circle2 = rs.AddCircle((0,0,HEIGHT), TOP_DIAMETER/2)
plane2 = rs.AddPlanarSrf(circle2)
outer_shell = rs.AddLoftSrf([circle1, circle2])

# Build our inner void
circle3 = rs.AddCircle((0,0,4), 70/2)
inner_void = rs.ExtrudeCurveStraight(circle3, (0,0,4), (0,0,HEIGHT))

# Remove the inner void from the outer shell
rs.CapPlanarHoles(outer_shell)
rs.CapPlanarHoles(inner_void)
rs.BooleanDifference(outer_shell, inner_void, delete_input=True)

# Clean up
rs.DeleteObjects([plane1, plane2, circle1, circle2, circle3])
