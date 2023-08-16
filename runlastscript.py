import idaapi
import idc


class LastScriptAH(idaapi.action_handler_t):
	def __init__(self):
		idaapi.action_handler_t.__init__(self)

	def activate(self, ctx):
		s = idaapi.reg_read_strlist("RecentScripts")
		if len(s) == 0:
			idaapi.warning("No recent scripts have been run")

		idaapi.IDAPython_ExecScript(s[0], globals())
		return 1

	def update(self, ctx):
		return idaapi.AST_ENABLE if len(idaapi.reg_read_strlist("RecentScripts")) > 0 else idaapi.AST_DISABLE


class RunLastScript(idaapi.plugin_t):
	flags = idaapi.PLUGIN_KEEP
	wanted_name = "RunLastScript"
	help = "Run previous script"
	comment = "Run previous script"

	def init(self):
		# Set up new action
		action_desc = idaapi.action_desc_t(
			"file:runlastscript",  # The action name. This acts like an ID and must be unique
			"Run Previous Script file",  # The action text.
			LastScriptAH(),  # The action handler.
			"Ctrl+Shift+F7",  # Optional: the action shortcut
			# Optional: the action tooltip (available in menus/toolbar)
			"Execute the previous script file",
			64  # Optional: the action icon (shows when in menus/toolbars)
		)
		# Register the action
		idaapi.register_action(action_desc)
		# Attach the action to a menu
		idaapi.attach_action_to_menu(
			"File/Script file...",  # The relative path of where to add the action
			"file:runlastscript",  # The action name (the ID)
			idaapi.SETMENU_APP
		)

		return idaapi.PLUGIN_KEEP

	def run(self, arg):
		pass

	def term(self):
		idaapi.detach_action_from_menu(
			"File/Run Previous Script file",
			"file:runlastscript"
		)
		idaapi.unregister_action("file:runlastscript")


def PLUGIN_ENTRY():
	return RunLastScript()
