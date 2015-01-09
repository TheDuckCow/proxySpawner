"""
This code is open source under the MIT license.


Source code available on github:
https://github.com/TheDuckCow/proxySpawner.git

Created as an entry to the BlenderMarket addon competition

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

###### verbose, how much gets printed to the console
v = True 
#v = False


def getAssetsList():
	
	assetPath = bpy.context.scene.proxyspawn_assets_path
	if not(os.path.isdir(assetPath)):
		#extract actual path from the relative one
		assetPath = bpy.path.abspath(assetPath)
	
	assets = []
	for file in os.listdir(assetPath):
		if file.endswith(".blend"):
			if v:print("file found: ",file)
			with bpy.data.libraries.load(assetPath+file, link=bpy.context.scene.proxylinkGroup) as (data_from, data_to):
				data_to.groups = data_from.groups
	
	return


def unLinkAssetsList():
	
	assetPath = bpy.context.scene.proxyspawn_assets_path
	if not(os.path.isdir(assetPath)):
		#extract actual path from the relative one
		assetPath = bpy.path.abspath(assetPath)
	
	assets = []
	# check through each asset, see if it was from this folder, then
	# if number of users is zero, remove it; if not, keep it?
	

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
	
		if v:print("hello world, ")
		self.report({'ERROR'}, "Feature not implemented yet")
		return {'FINISHED'}



### update proxy?

#######
# Class for spawning/proxying a new asset for animation
class updateAssets(bpy.types.Operator):
	"""Link/append all groups in all library files in asset folder"""
	bl_idname = "object.update_assets"
	bl_label = "Update list of assets"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
	
		#if v:print("hello world, ")
		#self.report({'ERROR'}, "Feature not implemented yet")
		list = getAssetsList() #should return to some property list thing
		if v:print("assets: ",list)
		return {'FINISHED'}


# class for the UI list..... idk what I'm doing
class groupListing(bpy.types.UIList):
    bool    = bpy.props.BoolProperty(default=False)
    integer = bpy.props.IntProperty()
    string  = bpy.props.StringProperty()
    # A list of identifiers (colon-separated strings) which property’s controls should be displayed
    # in a template_list.
    # Note that the order is respected.
    template_list_controls = bpy.props.StringProperty(default="integer:string:bool", options={"HIDDEN"})


#######
# panel for these declared tools
class proxyPanel(bpy.types.Panel):
	"""MCprep addon panel"""
	bl_label = "Proxy Spawner"
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = "Relations"

	def draw(self, context):
		
		layout = self.layout
		split = layout.split()
		
		col = split.column(align=True)
		row = col.row(align=True)
		row.label(text="Directory:")
		row.prop(context.scene,"proxyspawn_assets_path",text="")
		
		
		#list section (just ripped from list of vertex groups script, make specific to this
		split = layout.split()
		#group = ob.vertex_groups.active #getAssetsList()
		groups = bpy.data.groups
		
		### stopped development here, couldn't figure out UI lists

		row = layout.row()
		row.template_list("UI_UL_list", "", bpy.data,
							"groups", bpy.data, "active_index", rows=2)
		"""
		col = row.column(align=True)
		col.operator("object.vertex_group_add", icon='ZOOMIN', text="")
		col.operator("object.vertex_group_remove", icon='ZOOMOUT', text="").all = False
		"""
		# create custom menu for these things?
		#col.menu("MESH_MT_vertex_group_specials", icon='DOWNARROW_HLT', text="")
		
		"""
		if ob.vertex_groups and (ob.mode == 'EDIT' or (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex)):
			row = layout.row()

			sub = row.row(align=True)
			sub.operator("object.vertex_group_assign", text="Assign")
			sub.operator("object.vertex_group_remove_from", text="Remove")

			sub = row.row(align=True)
			sub.operator("object.vertex_group_select", text="Select")
			sub.operator("object.vertex_group_deselect", text="Deselect")

			layout.prop(context.tool_settings, "vertex_group_weight", text="Weight")
		"""
		split = layout.split()
		col = split.column(align=True)
		row = col.row(align=True)
		row.operator("object.proxy_spawn", text="Spawn Proxy")
		row.operator("object.update_assets", text="Update list")
		
		split = layout.split()
		col = split.column(align=True)
		col.label(text="Link groups")
		col.prop(context.scene,"proxylinkGroup")


########################################################################################
#	Above for the class functions
#	Below for registration stuff
########################################################################################


def register():
	bpy.utils.register_class(proxySpawn)
	bpy.utils.register_class(proxyPanel)
	bpy.utils.register_class(updateAssets)
	#bpy.utils.register_class(groupListing)
	
	#properties
	bpy.types.Scene.proxyspawn_assets_path = bpy.props.StringProperty(
		name="Folder of asset files",
		description="Path to the folder with assets for group linking",
		default="//assets/",subtype="DIR_PATH")
	bpy.types.Scene.proxylinkGroup = bpy.props.BoolProperty(
		name="Link library groups",
		description="Links groups imported, otherwise groups are appended",
		default=True)
	#bpy.types.Scene.my_settings = bpy.props.CollectionProperty(type=groupListing)
	# Unused, but this is needed for the TemplateList to work…
	#bpy.types.Scene.my_settings_idx = bpy.props.IntProperty()

def unregister():
	bpy.utils.unregister_class(proxySpawn)
	bpy.utils.unregister_class(proxyPanel)
	bpy.utils.unregister_class(updateAssets)
	#bpy.utils.unregister_class(groupListing)
	
	#properties
	del bpy.types.Scene.proxyspawn_assets_path
	del bpy.types.Scene.proxylinkGroup
	#del bpy.types.Scene.my_settings
	#del bpy.types.Scene.my_settings_idx

if __name__ == "__main__":
	register()

