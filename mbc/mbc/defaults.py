from mezzanine.conf import register_setting

register_setting(
    name="MAPS_API_KEY",
    label="Google Maps API Key",
    description="The API Key used to call Google Maps",
    editable=True,
    default="Foo",
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    append=True,
    default=("MAPS_API_KEY",),
    )
