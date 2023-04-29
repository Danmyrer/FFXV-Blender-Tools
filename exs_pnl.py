import bpy

from bpy.types import Panel

class EXS_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Object Tools"
    bl_category = "Exsomnium"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.operator("object.join_by_common_gmdl", text="Join by common GMDL")

        col = row.column()
        col.operator("object.rename_by_gmdl", text="Rename by GMDL")