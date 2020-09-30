import sublime
import sublime_plugin


class ToSlashCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				selected_text = self.view.substr( region )
				selected_text = selected_text.replace( "\\\\", "/" )
				selected_text = selected_text.replace( "\\", "/" )
				selected_text = selected_text.replace( "//", "/" )
				self.view.replace( edit, region, selected_text )

class ToDoubleBackslashCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				selected_text = self.view.substr( region )
				selected_text = selected_text.replace( "\\\\", "\\" )
				selected_text = selected_text.replace( "\\", "\\\\" )
				selected_text = selected_text.replace( "//", "\\\\" )
				selected_text = selected_text.replace( "/", "\\\\" )
				self.view.replace( edit, region, selected_text )

class ToSingleBackslashCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				selected_text = self.view.substr( region )
				selected_text = selected_text.replace( "\\\\", "\\" )
				selected_text = selected_text.replace( "//", "\\" )
				selected_text = selected_text.replace( "/", "\\" )
				self.view.replace( edit, region, selected_text )

