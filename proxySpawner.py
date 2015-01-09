"""
This code is open source under the MIT license.


Source code available on github:
https://github.com/TheDuckCow/proxySpawner.git

Created as an entry to the BlenderMarket addon competition, 

"""

########
bl_info = {
	"name": "Proxy Spawner",
	"category": "Object",
	"version": (0, 1, 0),
	"blender": (2, 72, 0),
	"location": "3D window > tools > relations",
	"description": "Button-access to link in assets in an asset folder and auto-proxy armatures",
	"warning": "",
	"wiki_url": "https://github.com/TheDuckCow/MCprep",
	"author": "Patrick W. Crawford"
}

import bpy,os,mathutils,random,math

###### verbose, how much gets printed to the consol
#v = True 
v = False


########################################################################################
#	Above for helper functions
#	Below for operators and key functions
########################################################################################


#######
# Class for spawning/proxying a new asset for animation
class proxySpawn(bpy.types.Operator):
	"""Link in an external group and proxy any armatures"""
	bl_idname = "object.proxy_spawn"
	bl_label = "Spawn linked group and proxy"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
	
		if v:print("hello world, solidify those pixels!")
		self.report({'ERROR'}, "Feature not implemented yet")
		return {'FINISHED'}


### update proxy?


#######
# panel for these declared tools
class proxyPanel(bpy.types.Panel):
	"""MCprep addon panel"""
	bl_label = "Proxy Spawner Panel"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = "Relations" #or "Relations"?

	def draw(self, context):
		
		layout = self.layout
		split = layout.split()
		
		col = split.column(align=True)
		col.operator("object.proxy_spawn", text="Proxy Spawn", icon='LIBRARY_DATA_DIRECT')


########################################################################################
#	Above for the class functions
#	Below for registration stuff
########################################################################################



def register():
	bpy.utils.register_class(proxySpawn)
	bpy.utils.register_class(proxyPanel)
	
	#properties
	bpy.types.Scene.proxyspawn_assets_path = bpy.props.StringProperty(
		name="Folder of asset files",
		description="Path to the folder with assets for group linking",
		default="//assets/",subtype="DIR_PATH")
	bpy.types.Scene.MCprep_linkGroup = bpy.props.BoolProperty(
		name="Link library groups",
		description="Links groups imported, otherwise groups are appended",
		default=True)



def unregister():
	bpy.utils.unregister_class(proxySpawn)
	bpy.utils.unregister_class(proxyPanel)
	
	#properties
	del bpy.types.Scene.proxyspawn_assets_path

if __name__ == "__main__":
	register()

