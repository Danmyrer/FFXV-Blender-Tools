import bpy

from bpy.types import Operator

class EXS_OT_Joint_By_Common_GMDL(Operator):
    bl_idname = "object.join_by_common_gmdl"
    bl_label = "Join by common GMDL"
    bl_description = "Join all selected objects that have the same GMDL as a custom property"

    # Returns boolean that decides if operator should be enabled
    @classmethod
    def poll(cls, context):
        obj = context.object

        # Check if object is in object-mode
        if obj is not None:
            if obj.mode == "OBJECT":
                return True
            
        return False
    
    def execute(self, context):
        selected_obj = context.selected_objects
        grouped_obj = {}

        for obj in selected_obj:
            # Get URI if avaliable
            mod_uri = obj.get('Model URI')
            if mod_uri is None: continue

            # Check for existing gmdl
            if grouped_obj.get(mod_uri) is None:
                grouped_obj[mod_uri] = [ obj ]
            else:
                grouped_obj[mod_uri].append(obj)

        # Deselect everything
        bpy.ops.object.select_all(action='DESELECT')

        for key, value in grouped_obj.items():
            if len(value) <= 1: continue

            for obj in value:
                obj.select_set(True)
            joiner = value[0]

            bpy.context.view_layer.objects.active = joiner
            bpy.ops.object.join()

            # Deselect before next iteration
            bpy.ops.object.select_all(action='DESELECT')

        return { 'FINISHED' }
