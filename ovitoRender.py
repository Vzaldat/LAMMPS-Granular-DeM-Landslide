import os
from ovito.io import import_file
from ovito.vis import Viewport, TachyonRenderer
from ovito.modifiers import ComputePropertyModifier, ColorCodingModifier

os.mkdir("frames")
pipeline = import_file("slope.dump", input_format="lammps/dump")

pipeline.modifiers.append(ComputePropertyModifier(output_property="VelocityMagnitude",
expressions=["sqrt(Velocity.X^2 + Velocity.Y^2)"]))

pipeline.modifiers.append(ColorCodingModifier(
    property="VelocityMagnitude", start_value=0.0,
    end_value=3.0
))

pipeline.add_to_scene()

vp = Viewport(type=Viewport.Type.Front)

vp.zoom_all()

n = pipeline.source.num_frames

print("frames:", n)

for f in sorted({0, n // 5, n // 2, n-1}):
    vp.render_image(filename=f"frames/frame_{f:03d}.png",
    frame=f, renderer=TachyonRenderer())

    print("wrote", f"frame_{f:03d}.png")