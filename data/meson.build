# Compiling the resources
# about_dialog is defined in data/ui/meson.build to generate the output file in that directory
res = gnome.compile_resources(
  PROJECT_RDNN_NAME,
  PROJECT_RDNN_NAME + '.gresource.xml',
  gresource_bundle: true,
  source_dir: meson.current_build_dir()
)

schema_src = PROJECT_RDNN_NAME + '.gschema.xml'
#gnome.compile_schemas(build_by_default: true, depend_files: files(schema_src))

# Installing the schema file
#install_data(
#  schema_src,
#  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
#)