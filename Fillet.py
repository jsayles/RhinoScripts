import rhinoscriptsyntax as rs

circle1 = rs.AddCircle((0,0,0), 10)

circle2 = rs.AddCircle((0,0,50), 10)
top = rs.AddPlanarSrf(circle2)

outer_shell = rs.AddLoftSrf([circle1, circle2])

rounded_edge = rs.FilletSurfaces(outer_shell, top, 5.0, [0,0], [0,0])
rs.JoinSurfaces([outer_shell, rounded_edge])
rs.DeleteObjects([circle1, circle2, top])
